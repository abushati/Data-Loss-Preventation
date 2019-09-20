# Data-Loss-Preventation

This is a Data Loss Preventation system using Django Rest Framework and Slack's API to retrieve messages posted in the home-assignment channal.

# Set up steps

1) Clone this repo to any folder

2) Go into the folder that contains the docker-compose.yml file. Docker version 3 is used!

3) Run docker-compose up -d. Running in detach mode is necessary for the next step

4) In order for our server to retrieve Event Subscriptions from Slack, the request url needs to be a public url. Ngrok is used to tunnel our localhost to a randomly generated url. When the containers are successfully running, run the command curl $(docker port ngrok 4040)/api/tunnels.

5) Find the key:value as followed "public_url":"http://3a03c35f.ngrok.io" in the command output.

6) Go to the Data Loss Prevention App on the Slack platform and go to Event Subscriptions tab (under features)

7) In the Request URL input the url you found in step 5 http://3a03c35f.ngrok.io and add the subdirectory /DSL/. The full url should be http://3a03c35f.ngrok.io/DSL/

8) When the handshake is successfully complete, restall the app and post to the home-assignment channel.

9) To gain access to the django admin page, use the default credentials, Username:root,Password:password,

10) To add regex pattern to be used, go to the RegexCombs table and add the pattern

11) To view all the message that have been blocked by the patterns provided, go to the Incident logs table.


Slack Link to join work space- https://join.slack.com/t/avananassignment/shared_invite/enQtNzY0Nzk3NDk1MTczLTcwYWVhYjUyZTE4MzQzYTI3ZWM2ZjFmYTg0MTUzZmNlZjNlMjkwZTU3MzdhNzc1NTA3YWIyZTAzMjkxYTcxOGQ
