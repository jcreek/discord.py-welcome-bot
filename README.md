# discord.py-welcome-bot

A simple bot that can be used to welcome new users to a discord server, sending them a custom private message and adding them to a role.

A video explaining how to set up everything except adding the user to a role can be found [here](https://youtu.be/N0NP7BfUFxA).

**Update November 2019** - Now set up as a docker container to ensure full compatibility as I will not be maintaining this. Specific versions of Python and Discord.py are required for this script to work.

## How to install the welcome-bot as a docker container on a server (raspberrypi)

### Building the image

Copy the folder containing the Dockerfile onto the server. Go to the directory that has the Dockerfile and run the following command to build the Docker image from the source code:

`docker build -t welcome-bot .`

The image will now be listed by Docker. You can confirm this by running:

`docker images`

### Create a writeable container from the image

`docker create --name welcome-bot welcome-bot`

### Run the image

`docker start welcome-bot`

### Set up a cronjob

Run the command below to edit the cronjobs:

`crontab -e`

Then add the below line to it:

`*/10 * * * * docker stop welcome-bot && docker start welcome-bot`

This will run the service every ten minutes. To change this use [Crontab Guru](https://crontab.guru)
