from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    old_server = client.get_server('old_server_id')
    new_channel = client.get_channel('new_server_id')

    if message.server == old_server:
        await client.send_message(new_channel, message.content + ' - ' + message.author.nick)

client.run('token')