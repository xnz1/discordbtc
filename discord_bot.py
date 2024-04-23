# Complete and corrected code for the Bitcoin price check Discord bot as a Python file


import discord
from discord.ext import commands
import requests
from datetime import datetime

BOT_TOKEN = ''  # Add your Discord bot token here
COINGECKO_API_URL_USD = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
COINGECKO_API_URL_BRL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

price_history_usd = {}
price_history_brl = {}

def fetch_bitcoin_priceUSD():
    response = requests.get(COINGECKO_API_URL_USD)
    data = response.json()
    price = data['bitcoin']['usd']
    price_history_usd[datetime.now()] = price
    return price

def fetch_bitcoin_priceBRL():
    response = requests.get(COINGECKO_API_URL_BRL)
    data = response.json()
    price = data['bitcoin']['brl']
    price_history_brl[datetime.now()] = price
    return price

def calculate_trend_and_percentage_change(price_history):
    if len(price_history) < 2:
        return "Not enough data to determine the trend."
    sorted_timestamps = sorted(price_history.keys())
    latest_timestamp = sorted_timestamps[-1]
    previous_timestamp = sorted_timestamps[-2]
    latest_price = price_history[latest_timestamp]
    previous_price = price_history[previous_timestamp]
    if previous_price != 0:
        percentage_change = ((latest_price - previous_price) / previous_price) * 100
    else:
        percentage_change = 0
    trend = "up" if latest_price > previous_price else "down" if latest_price < previous_price else "stable"
    return f"Bitcoin price is {trend} by {abs(percentage_change):.2f}% since the last check."

def bitcoinusd_command(price_history_usd):
    current_price = fetch_bitcoin_priceUSD()
    if len(price_history_usd) > 1:
        trend_message = calculate_trend_and_percentage_change(price_history_usd)
        message = f"The current Bitcoin price is ${current_price:.2f}. {trend_message}"
    else:
        message = f"The current Bitcoin price is ${current_price:.2f}."
    return message

def bitcoinbrl_command(price_history_brl):
    current_price = fetch_bitcoin_priceBRL()
    if len(price_history_brl) > 1:
        trend_message = calculate_trend_and_percentage_change(price_history_brl)
        message = f"The current Bitcoin price is R${current_price:.2f}. {trend_message}"
    else:
        message = f"The current Bitcoin price is R${current_price:.2f}."
    return message

@bot.command(name='bitcoinusd', help='Displays the current price of Bitcoin in USD and trend information.')
async def bitcoinusd(ctx):
    message = bitcoinusd_command(price_history_usd)
    await ctx.send(message)

@bot.command(name='bitcoinbrl', help='Displays the current price of Bitcoin in BRL and trend information.')
async def bitcoinbrl(ctx):
    message = bitcoinbrl_command(price_history_brl)
    await ctx.send(message)



    
    bot.run(BOT_TOKEN)



