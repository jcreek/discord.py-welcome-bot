# welcome-bot
## this bot will send a welcome message and assign a role

# import all necessary commands and libraries
import discord
import asyncio

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """ # customise this to the message you want to send new users
You
can
put
your
multiline
message
here!
"""

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)

    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = discord.utils.get(member.server.roles, name="name-of-your-role")
    await client.add_roles(member, role)
    print("Added role '" + role.name + "' to " + member.name)

client.run('token') 





