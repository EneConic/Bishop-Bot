import discord
from discord.ext import commands
import random

class Discuss(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help="I shall answer your questions.", aliases=['q', '?'])
    async def question(self, ctx, *, message):
        Answers = [
            "Yes, ",
            "No, ",
            "Quite, ",
            "Possibly, ",
            "Of course, ",
            "Of course not, ",
            "Ah. I see. ",
            "That would be most unfortunate should it go awry, ",
            "I would recommend it, ",
            "I wouldn't recommend it, ",
            "I feel like I've talked about this before... ",
            "As I have said before, no, ",
            "As I have said before, yes, "
        ]
        Answers_Select = Answers[random.randint(0,11)]
        await ctx.send(Answers_Select + f'{ctx.message.author.mention}')

    @commands.command(help="Your local news!", aliases=['n', '@'])
    async def news(self, ctx):
        Member_List = [
            'Byleth',
            'The Archbishop',
            'Dimitri',
            'His Majesty',
            'Hilda',
            'Seteth',
            'Flayn',
            'Ingrid',
            'Sylvain',
            'Felix',
            'Dedue',
            'Mercedes',
            'Annette',
            'Ashe'
        ]
        Member_Select = Member_List[random.randint(0,13)]

        Activity_List_Solo = [
            '{} is going for a walk.',
            '{} is eating some sweets.',
            '{} is resting.',
            '{} is going to go to town.',
            'Has anyone seen {} lately? They haven\'t been reporting in today.'
        ]
        Activity_Select_Solo = Activity_List_Solo[random.randint(0,4)]

        await ctx.send(Activity_Select_Solo.format(Member_Select))

def setup(client):
    client.add_cog(Discuss(client))