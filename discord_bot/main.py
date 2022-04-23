from discord import Client
from Logs import TheLog
import logging

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(dotenv_path="config")


class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.log = TheLog()



    async def on_ready(self):
        self.log.infolog(f"{self.user} has connected to Discord!")
        
    async def on_message(self,message):
        print(message.content)
    
        fichier = open("log.txt", "a")
        fichier.write(str(message.author) + " a envoye: " + message.content +"      le  "+ str(message.created_at) + "\n")
        fichier.close()

        if message.content.lower() == "hello":
        #await permet d'assurer le bon ordre
            await message.channel.send("hola")
    
        if message.content.lower() == "help":
        #await permet d'assurer le bon ordre
            await message.channel.send("Les differentes commandes utilisables sont: help, hello, !del suivis d'un nombre (pour supprimer les messages précédents)")




#client = MyBot()
#client.run("")

my_bot = MyBot()
my_bot.run(os.getenv("TOKEN"))
