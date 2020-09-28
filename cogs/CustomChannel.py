import discord
from discord.ext import commands
from config import Config

def setup(bot):
    bot.add_cog(CustomChannel(bot))

class CustomChannel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        config = Config()
        self.createdChannels = []
        self.custom_channel_id = config.custom_channel_id


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is not None and before.channel.id in self.createdChannels and len(before.channel.members) == 0:
            try:
                await before.channel.delete(reason='All users have left the channel')
            except discord.errors.NotFound as e:
                pass
            self.createdChannels.remove(before.channel.id)


        if after.channel is not None and after.channel.id == self.custom_channel_id:

            if after.channel.category is not None:
                destCategory = after.channel.category
            else:
                destCategory = member.guild
            overwrites = {
                member: discord.PermissionOverwrite(manage_channels=True, connect=True, speak=True)
            }
            new_channel = await destCategory.create_voice_channel(name = f'{member.display_name}\'s custom channel', overwrites=overwrites)
            await member.edit(voice_channel = new_channel)
            self.createdChannels.append(new_channel.id)

    @commands.Cog.listener()
    async def on_private_channel_delete(channel):
        if channel.id in self.createdChannels:
            self.createdChannels.remove(channel.id)


