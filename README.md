# CustomVoiceBot
Discord bot that creates custom voice channels.

## Installation
1. Clone repository ```git clone https://github.com/JustTrott/CustomVoiceBot.git```
2. install requirements ```pip install -r requirements.txt```
3. Run ```bot.py``` file. You will catch an error about creating the ```config.ini``` file in the directory.
4. Enter your Discord bot token and custom channel ID in ```config.ini``` file. "custom channel ID" is ID of the channel, after joining which your private channel will be created.
5. Run ```bot.py```

## How It Works
Simply enter previously chosen channel and then your custom voice channel will be created and you will be moved in automatically. In your custom channel you will be able to change general information e.g. Channel's name, user limit and bitrate. When no one is left in the channel, it will be deleted automatically.
