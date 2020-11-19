# discord.py-welcome-bot

A simple bot that can be used to welcome new users to a discord server, send them a custom private message, send a welcome message to a specific channel, and adding them to a role.

A video explaining how to set up everything except adding the user to a role can be found [here](https://youtu.be/N0NP7BfUFxA).

**Update November 2019** - Now set up as a docker container to ensure full compatibility as I will not be maintaining this. Specific versions of Python and Discord.py are required for this script to work.\
**Update November 2020** - Added basic install instructions for home computers and generic Linux distros, and how to enable Intents.

## Intents

Go to the [Discord Developer Portal](https://discord.com/developers/applications) and select your bot. Now move to the bot tab and scroll down. There you should see `Priveledged Gateway Intents`. Enable the `Members` intent.
![Enable Members Intent](https://i.imgur.com/rPePBe6.png)
## Easy: How to install the welcome-bot on a home computer:

Make sure that you've installed Python 3.6 or higher before beginning this.
### Linux

First, we want to clone the repository using `git clone`:
```
git clone https://github.com/jcreek/discord.py-welcome-bot.git

cd discord.py-welcome-bot
```
Secondly, we want to make sure we've updated our package list:

```
sudo apt update -y
```
We now want to install the `python3` package:
```
sudo apt install python3
```
Our final thing to do is run the script:
```
python3 welcome-bot.py
```
### Windows
You can download the latest python release from [here](https://www.python.org/downloads/windows/).
We now want to download and extract this repository:
![Downloading the repo](https://i.imgur.com/qe6H5Bo.png)
![Extracting the files](https://i.imgur.com/liPOy7K.png)
After extracting, you can navigate into the folder and just double-click the file.
![Running the file](https://i.imgur.com/pFdAa80.png)

## Advanced: How to install the welcome-bot as a docker container on a server (raspberrypi)


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

### View logs from inside the container

Run the below command to see the output of the bot.

`docker container logs -f welcome-bot`
***MAKE SURE THAT YOU CHANGE THE TOKEN AT THE BOTTOM OF THE FILE!!!***
