# welcome-bot
## this bot will send a welcome message and assign a role

# import all necessary commands and libraries
import discord
import asyncio
intents = discord.Intents(members=True)
client=discord.Client(intents=intents)
welcomechannel = client.get_channel(channel_id) # https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
# Make sure you get the ID of your channel by right-clicking it and clicking `Copy ID`. Make sure developer mode is on!
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
 # Customise the message below to what you want to send new users!
newUserMessage = """
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
    try: 
        await member.send(newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title="Welcome "+member.name+"!"
        description="We're so glad you're here!"
        color=discord.Color.green()
    )
    await welcomechannel.send(embed=embed)
        
    role = discord.utils.get(member.guild.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await member.add_roles(member, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title="😢 Goodbye "+member.name+"!",
        description="Until we meet again old friend." # A description isn't necessary, you can delete this line if you don't want a description.
        color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    )
    await welcomechannel.send(embed=embed)
    
client.run('token') 
