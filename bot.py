import discord
from discord.ext import commands
import sys
from config import Config


config = Config()
token = config.botToken

if not token:
    print("Are you sure, that you set Discord bot token in the config.ini?")
    sys.exit()

client = commands.Bot(command_prefix='CustomVoiceBot')

@client.event
async def on_command_error(ctx, error):
    pass

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'Your beatiful face'))
    print(f'{client.user.name} is ready.')
    customChannelID = config.customChannelID

startup_extensions = ['CustomChannel']

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(f'cogs.{extension}')
        except Exception as e:
            print(f'Failed to load extension: {extension}')
            print(f'\tError: {e}')
            continue
        print(f'Succesfully loaded extension: {extension}')

    client.run(token)
