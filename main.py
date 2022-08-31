import discord 
from discord.ext import commands
import os
import time
import string
import random
import discord.utils

token = os.environ['token']

prefix = "+"

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.command()
async def createserver(ctx):
  guild = ctx.message.guild
  await ctx.send("Making Server")
  channels = await ctx.guild.fetch_channels()
  for text_channel in channels:
        await text_channel.delete()
        print('deleted channel')
  await ctx.guild.edit(name="5 Invites = Nitro")
  cat1 = "Invites"
  await guild.create_category(cat1)
  cat2 = "Special"
  await guild.create_category(cat2)
  cat3 = "Giveaways"
  await guild.create_category(cat3)
  name = "📌・invites"
  await guild.create_text_channel(name)
  name1 = "🎁・claim"
  await guild.create_text_channel(name1)
  name2 = "🔎・proofs"
  await guild.create_text_channel(name2)
  name3 = "🚀・boost"
  await guild.create_text_channel(name3)
  name4 = "🎉・drop"
  await guild.create_text_channel(name4)
  name5 = "🎉・giveaway"
  await guild.create_text_channel(name5)
  name6 = "🎉・nitro-codes"
  await guild.create_text_channel(name6)
  
  bot.run(token)
  
  
