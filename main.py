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
async def invite(ctx): #!upgrade
    person= ctx.message.author
    user = ctx.message.author.id
    
    rolelist=[]
    for role in person.roles:
        rolelist.append(role.name)
    print(rolelist)
    
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
            
    if totalInvites > 0:
        if "Invite Master" not in rolelist:
            ogrole = discord.utils.get(person.guild.roles, name = "Invite Master")
            await person.add_roles(ogrole, atomic=True)
            embed = discord.Embed(title = person, description = str(person) + ", congrats! You are now an Invite Master.")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
            
        else:
            embed = discord.Embed(title = person, description = str(person) + ", you already have Invite Master role.")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
        
    else:     
        embed = discord.Embed(title = person, description= 'Not enough invites!')
        embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
        await ctx.channel.send(embed = embed)
        


    
client.run(TOKEN)
