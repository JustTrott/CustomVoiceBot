import os
import configparser as cp

configFile = 'config.ini'
discordGroup = 'Discord'
tokenKey = 'token'
CustomChannelKey = 'custom channel id'


class Config:
    def __init__(self):
        self.cp = cp.ConfigParser()
        self.check_config()

    def check_config(self):
        if os.path.isfile(configFile):
            self.cp.read(configFile)
            return
        print('No config.ini file. Creating a default one.')
        self.create_config()

    def create_config(self):
        self.cp[discordGroup] = {}
        self.cp[discordGroup][tokenKey] = ''
        self.cp[discordGroup][CustomChannelKey] = ''

        with open(configFile, 'w') as file:
            self.cp.write(file)

    @property
    def botToken(self):
        return self.cp[discordGroup][tokenKey]


    @property
    def custom_channel_id(self):
        return int(self.cp[discordGroup][CustomChannelKey])



