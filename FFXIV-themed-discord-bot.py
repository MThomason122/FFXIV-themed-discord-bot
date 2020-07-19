#Nhaama Discord Bot
import os
import random
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('SECRET_TOKEN')

bot = commands.Bot(command_prefix='~')
client = discord.Client()

@client.event
#prints message when Nhaama is prepare and ready for use
async def on_ready():
        print(f'{client.user.name} has connected to discord.' )

@bot.command(name='AuRaLore')
async def au_ra_lore(ctx):
        #list of Au Ra related lore to be used by the command
        au_ra_lore_list = ['Ishgardians slaughtered mass amounts of refugee Xaela thinking they were part of the Dravanian Horde in the Sixth Astral Era.',
        'Auri Xaela are treated with suspicion and hostility compared to Auri Raen.',
        (
        'Possessed of a strong self-preservation instinct, the Au Ra believe in protecting tribe and family, though the means by which the two clans choose to do so diverges greatly.' 
        'The Raen coexist peacefully with other races to ensure the safety of their own land, while the fiercely tribal Xaela shun relations with other races,' 
        'even viewing strangers of their own kind as potential enemies.' 
        'As such, the former are viewed favorably by the outside world, while the latter are typically regarded with suspicion and hostility.'
        ), 'The Malaguld tribe is the only tribe that accepts people of the Raen, those that have been exiled, or those who have fled persecution, into their cirle.', 
        ('Auri creation myth tells of a Dawn Father and a Dusk Mother from whom all Au Ra are descended. The Xaela believe their veins run thick with the blood of the latter'
         '- their lustrous black scales and firey wills serving as proof of this divine lineage. The Raen believe their veins to run thick with the blood of the former'
         '- their brilliant white scales and iron wills serving as proof of this divine lineage.'),
        ]

        response = random.choice(au_ra_lore_list)  #randomly chooses a string from the lore list
        await ctx.send('Coming right up! \n' + response)

@bot.command(name='Ping')
#displays bot latency
async def ping(ctx):
    await ctx.send('Pong! {0}s'.format(bot.latency))

bot.run(TOKEN)