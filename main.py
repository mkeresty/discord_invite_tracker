import discord

from discord.ext import commands
import time

TOKEN=''

client = discord.Client()


@client.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"{ctx.author.mention}, you've invited {totalInvites} member{'' if totalInvites == 1 else 's'}!")
    
    
@bot.command(pass_context=True)
async def upgrade(ctx): #!upgrade
    person= ctx.message.author
    user = ctx.message.author.id
    ref = db.reference(f"/"+str(user))    
    status = ref.get()
    print("status: "+ str(status))

    rolelist=[]
    for role in person.roles:
        rolelist.append(role.name)
    print(rolelist)

    if status == "nope":
        await ctx.channel.send(str(person) + ", you haven't reached the score threshold!")
    if int(status) <50:
        await ctx.channel.send(str(person) + ", you haven't reached the score threshold!")
    if int(status) >=50:
        if "Doodle Gene Expert" not in rolelist:
            ogrole = discord.utils.get(person.guild.roles, name = "Doodle Gene Expert")
            await person.add_roles(ogrole, atomic=True)
            await ctx.channel.send(str(person) + ", congrats! Your role is now Doodle Gene Expert.")
        else:
            await ctx.channel.send(str(person) + ", You already have Doodle Gene Expert role")
    else:        
        await ctx.channel.send(str(person)+ ", please use the !play command to get your game code.")    
    
    
    
client.run(TOKEN)
