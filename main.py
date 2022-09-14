import discord

from discord.ext import commands

TOKEN=''

client = discord.Client()

bot = commands.Bot(command_prefix="!", description="ogrole")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def cannainvite(ctx): #!upgrade
    person= ctx.message.author
    user = ctx.message.author.id
    
    rolelist=[]
    for role in person.roles:
        rolelist.append(role.name)
    #print(rolelist)
    x = await ctx.guild.invites()
    #print(x)
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            #print(i.inviter)
            totalInvites += i.uses
    #print(totalInvites)        
    if totalInvites > 2:
        if "___________" not in rolelist:
            ogrole = discord.utils.get(person.guild.roles, name = "")
            await person.add_roles(ogrole, atomic=True)
            embed = discord.Embed(title = person, description = str(person) + ", congrats! You are now an ______________")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
            
        else:
            embed = discord.Embed(title = person, description = str(person) + ", you already have ______________ role.")
            embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
            await ctx.channel.send(embed = embed)
        
    else:     
        embed = discord.Embed(title = person, description= 'Not enough invites!')
        embed.add_field(name = 'Invites: ',value = str(totalInvites), inline = False)
        await ctx.channel.send(embed = embed)
        


    
#client.run(TOKEN)
bot.run(TOKEN)   
