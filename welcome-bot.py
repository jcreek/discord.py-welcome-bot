# welcome-bot
## this bot will send a welcome message and assign a role

# import all necessary commands and libraries
import discord
import asyncio

client=discord.Client()

@client.event
async def on_ready():
    print('Successfully Logged In!')
    print(client.user.name)
    print(client.user.id)
    print('-----')

user_message = """<User Message Placeholder
EDIT IN CODE>"""

@client.event
async def on_member_join(member):
    print(f"Recognised that a member called {member} joined")
    await member.send(user_message)
    print(f"Sent message to {member}")

    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = discord.utils.get(member.guild.roles, name="<role_name>")
    await member.add_roles(role)
    print(f"Added role {role.name} to {member.name}")

client.run('token', bot=True)





