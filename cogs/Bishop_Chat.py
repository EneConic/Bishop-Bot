import discord
from discord.ext import commands
import random

class Discuss(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="I shall answer your questions.")
    async def question(self, cx, *, message):
        Answers = [
            "Yes, ",
            "No, ",
            "Quite, ",
            "Possibly, ",
            "Of course, ",
            "Of course not, "
            "Ah. I see. "
            "That would be most unfortunate should it go awry, ",
            "I would recommend it, ",
            "I wouldn't recommend it, ",
            "I feel like I've talked about this before... "
            "As I have said before, no, "
            "As I have said before, yes, "
        ]
        Answers_Select = Answers[random.randint(0,12)]
        await ctx.send(Answers_Select + f'{ctx.message.author.mention}')

def setup(client):
    client.add_cog(Discuss(client))