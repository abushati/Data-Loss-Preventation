from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import re
import json
import requests
from DataListener.models import regexCombs as combs
from DataListener.models import incidentLog as logs

SLACK_VERIFICATION_TOKEN = getattr(settings, "SLACK_VERIFICATION_TOKEN", None)
SLACK_USER_BOT_TOKEN = "xoxb-766651068791-765093399216-EUPmX70Xg2vKUuy9z5ALr0wR"
USER_TOKEN = (
    "xoxp-766651068791-766651070551-760703177377-ea7bf18e758a724e8c8d111e5a5df208"
)


class DSL(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data
        """
        Checks to see if the Slack verification sent by slack is the same as the
        the one in our settings file
        """
        if slack_message.get("token") != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # If true, the request is to validate the handshake
        elif slack_message.get("type") == "url_verification":
            return Response(slack_message["challenge"])

        # True if the message is sent by user, not bot user
        if "event" in slack_message and "bot_id" not in slack_message["event"].keys():
            event = slack_message.get("event")
            messageSent = event["text"]
            leakFound = self.checker(messageSent)

            if not leakFound:
                return Response(status=status.HTTP_200_OK)
            else:
                self.updateIncidentTable(leakFound)
                self.updateMessage(slack_message["event"]["ts"],slack_message["event"]["channel"])
                return Response(data="THERE IS A LEAK", status=status.HTTP_200_OK)

            return Response(data="THERE IS A LEAK", status=status.HTTP_200_OK)
        else:

            return Response(status=status.HTTP_200_OK)

    # Function checks to see if any of the words in the message matches
    # any of the regex patterns the admin provided
    def checker(self, messageSent):

        allCombs = combs.objects.all()
        leakCombs = {comb.regexName: comb.regexPattern for comb in allCombs}
        leakedWordsCaught = {}
        for patternKey in leakCombs.keys():
            p = re.compile(leakCombs[patternKey])
            messageSentList = messageSent.lower().split(" ")

            secertWords = [word for word in messageSentList if p.match(word)]
            if secertWords:
                leakedWordsCaught[patternKey] = {
                    "Pattern": leakCombs[patternKey],
                    "WordsCaught": secertWords,
                    "MessageSent": messageSent,
                }

        return leakedWordsCaught

    # Function runs when leaked words are found in the message. Updates
    # logs table with the relevent information
    def updateIncidentTable(self, info):
        for patternName, leakMessageInfo in info.items():
            log = logs(
                pattern_name=patternName,
                pattern_string=leakMessageInfo["Pattern"],
                words_caught=(" & ".join(leakMessageInfo["WordsCaught"])),
                message_sent=leakMessageInfo["MessageSent"],
            )

            log.save()

    # Edit the message in the respective channel
    def updateMessage(self, ts, channel):
        url = "https://slack.com/api/chat.update"
        data = {
            "Content-type": "application/json",
            "text": "**This message has been blocked**",
            "ts": ts,
            "channel": channel,
            "token": USER_TOKEN,
        }
        requests.post(url, data=data)
