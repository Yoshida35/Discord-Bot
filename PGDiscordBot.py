import discord
import random
from discord.ext import commands, tasks
#import youtube_dl
import os
import time
import pyautogui

# - To use the bot.
client = commands.Bot(command_prefix = '#')


@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Ur Mum'))
	print('Logged on as {0}!'.format(self.user))
x=' ';
#Loading cause idk.
print('██████       ]42%')
print(x)
time.sleep(1)
print('██████████   ]69%')
print(x)
time.sleep(2)
print('Bot is online stupid!')
print(x)
time.sleep(1)
print('What are you waiting for?')

#Joined the Server
@client.event
async def on_member_join(member):
	print(f'{member} has joined the server, Hello!')

#Left the Server
@client.event
async def on_member_remove(member):
	print(f'{member} has left the server, Bye!')


#Kick
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

#Ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

#Unban
@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return


#Changes the nickname of someone.
@client.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)




#Repeats the Message
@client.command(name='spam')
async def spam(ctx, amount:int, *, message):
    for i in range(amount):
        await ctx.send(message)



#Roles
@client.command('role')
@commands.has_permissions(administrator=True) #Needs Admin Permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position:
    return
  if role in user.roles:
      await user.remove_roles(role)
  else:
      await user.add_roles(role)



#Ping from the client to the bot.
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Type something as the bot.
@client.command(aliases=['s', 'speak'])
async def say(ctx, *, arg):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{arg}')

#8 ball
@client.command(aliases=['8ball', '8Ball', '8 ball', '8 Ball'])
async def _8ball(ctx, *, question):
	responses = ["It is certain.",
				"It is decidedly so.",
			"Without a doubt.",
			"Yes - definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Delets messages above.
@client.command()
async def clear10(ctx, amount=10):
	await ctx.channel.purge(limit=amount)

@client.command()
async def clear5(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
async def clear2(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

@client.command()
async def clear1(ctx, amount=1):
	await ctx.channel.purge(limit=amount)


client.run('Nzc2MTY5MjcyNzU3NzE0OTg5.X6w99w.mNTGJ_PyNAujqp0zIMxejyxfogo')
