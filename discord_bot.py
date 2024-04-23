import discord
from discord.ext import commands
import requests
import datetime

# Constants and global variables
BOT_TOKEN = 'MTIyODE0NjE2ODQ0NjU4Mjg5Ng.GnoG5N.Oi_K4d7cx5DYHUA5lnxMOG7Ag2j4IIjvLymU9w'  # Replace with your actual Discord bot token
COINGECKO_API_URL_USD = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
COINGECKO_API_URL_BRL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"

# Define Intents
intents = discord.Intents.default()  # Defaults enable all non-privileged intents
intents.message_content = True  # Subscribe to messages for commands
intents.guilds = True    # For handling events within guilds

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Global variable to store the last checked price
last_price = None






    

def fetch_bitcoin_priceUSD():
    """Fetch the current Bitcoin price from the CoinGecko API."""
    response = requests.get(COINGECKO_API_URL_USD)
    data = response.json()
    return data['bitcoin']['usd']

def fetch_bitcoin_priceBRL():
    """Fetch the current Bitcoin price from the CoinGecko API."""
    response = requests.get(COINGECKO_API_URL_BRL)
    data = response.json()
    return data['bitcoin']['brl']
    
    

@bot.command(name='bitcoinusd', help='Displays the current price of Bitcoin and if it is up or down since the last check.')
async def bitcoin(ctx):
    global last_price
    current_price = fetch_bitcoin_priceUSD()
    if last_price is not None:
        trend = "up" if current_price > last_price else "down"
        message = f"The current Bitcoin price is ${current_price:.2f} (It's {trend}!)"
    else:
        message = f"The current Bitcoin price is ${current_price:.2f}."
    await ctx.send(message)
    last_price = current_price

@bot.command(name='bitcoinbrl', help='Displays the current price of Bitcoin and if it is up or down since the last check.')
async def bitcoin(ctx):
    global last_price
    current_price = fetch_bitcoin_priceBRL()
    if last_price is not None:
        trend = "up" if current_price > last_price else "down"
        message = f"The current Bitcoin price is R${current_price:.2f} (It's {trend}!)"
    else:
        message = f"The current Bitcoin price is R${current_price:.2f}."
    await ctx.send(message)
    last_price = current_price


def timeFormatter(time):
    currentDate = "{}/{}/{}".format(time.strftime("%Y"), time.strftime("%m"), time.strftime("%d"))
    currentTime = "{}:{}".format(time.strftime("%H"), time.strftime("%M"))

    return f"{currentDate} at {currentTime}"






# Run the bot
bot.run("MTIyODE0NjE2ODQ0NjU4Mjg5Ng.GnoG5N.Oi_K4d7cx5DYHUA5lnxMOG7Ag2j4IIjvLymU9w")  # This line must be at the root level, not inside any function or conditional
