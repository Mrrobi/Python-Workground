import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")
map_list = ["haven","split","bind","ascent"]
team_member = []
member_list = []
team_one = []
team_two = []

@client.event
async def on_ready():
    print("bot ready.")

@client.command()
async def imin(ctx):
    if team_member is None:
        team_member.append(ctx.message.author.id)
        member_list.append(ctx.message.author)
    else:
        test = True
        for x in team_member:
            if(x == ctx.message.author.id):
                test = False
        if(test):
            team_member.append(ctx.message.author.id)
            member_list.append(ctx.message.author)
    #print(team_member)
    #print(ctx.message.author.mention)
    await ctx.send(f'<@{ctx.message.author.id}> you are added')
@client.command()
async def PLAY(ctx):
    red = client.get_channel(724892876730793984)
    blue = client.get_channel(724892920527847436)
    random.shuffle(team_member)
    global team_one
    team_one = team_member[0:len(team_member)//2]
    global team_two
    team_two = team_member[len(team_member)//2:len(team_member)]
    print(team_one)
    print(team_two)
    msg1 = ""
    msg2 = ""
    for x in team_one:
        msg1 += f"<@{x}> "
    await ctx.send(f'Team One: {msg1}')
    for x in team_two:
        msg2 += f"<@{x}> "
    await ctx.send(f'Team Two: {msg2}')

@client.command()
async def map(ctx):
    random.shuffle(map_list)
    await ctx.send(f'Map choosen: {map_list[0]}')

def get_member(id):
    for x in member_list:
        if(id == x.id):
            return x
@client.command()
async def cshift(ctx):
    global team_two
    global team_one
    red = client.get_channel(717770511161229414)
    blue = client.get_channel(717770772722221097)
    print(team_one)
    print(team_two)
    for i in team_one:
        print("team one")
        for xx in member_list:
            if (i == xx.id):
                member = xx
        print(member)
        await member.move_to(blue, reason=None)
    for j in team_two:
        print("team two")
        for xx in member_list:
            if (j == xx.id):
                member = xx
        print(member)
        await member.move_to(red, reason=None)
@client.command()
async def clrq(ctx):
    global team_member
    global team_one
    global team_two
    global member_list

    team_member = []
    member_list = []
    team_one = []
    team_two = []
@client.command()
async def showq(ctx):
    msg = ""
    for x in member_list:
        msg += x.name+"\n"
    await ctx.send(msg)
@client.command()
async def HELP(ctx):
    await ctx.send(".imin: join in game queue\n"
                   ".PLAY: split existing queue members in 2 team\n"
                   ".map: choose a random map\n"
                   ".cshift: transfer team members in red and blue channel\n"
                   ".showq: Show existing queue\n"
                   ".clrq: clear existing queue")

client.run("NzI0NzAxNjkzNTI2MTQ3MjAz.XvEBDA.2U3O_AlpHA6JEwUspLBwNX72Sbo")