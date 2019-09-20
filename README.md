# Data-Loss-Preventation

This is a Data Loss Preventation system user Django Rest Framework and Slack's API to retrieve messages posted in the home-assignment channal.

# Set up sets

1) Clone the this repo to any folder

2) Go into the folder that container the docker-compose.yml file. Docker version 3 is used!

3) Run docker-compose up -d. Running in detach mode is necessary for the next step

4) In order for our server to retrieve Event Subscriptions from Slack, the request url needs to be a public url. Ngrok is used to tunnel our localhost to a randomly generated url. When the containers are successfully running, run the command curl $(docker port ngrok 4040)/api/tunnels.

5)Find the key:value as followed "public_url":"http://3a03c35f.ngrok.io".

6) Go to the Data Loss Prevention App on the Slack platform and go to Event Subscriptions tab (under features)

7) In the Request URL input the url you found in step 5 http://3a03c35f.ngrok.io and add the subdirectory /DSL/. The full url should be http://3a03c35f.ngrok.io/DSL/

