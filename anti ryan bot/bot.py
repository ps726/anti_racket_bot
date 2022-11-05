from random import *
import hikari, lightbulb

list = {'😳', '💀', '🤓', '😡', '🤡', '🗿', '🤮', '🐟'}
target = ''

#connects bot to discord API
bot = lightbulb.BotApp(
    token="OTkxNjU3NDE2NzM3NDIzNDAw.GDg88C.-MQtJN_ILPR3P9ZGujwZnE8uF2Q8-7hTnLuDm0"
    )


#prints "bot is ready" when bot was connected to all shards and is ready for use
@bot.listen()
async def on_bot_started(event: hikari.StartedEvent):
    print("Bot is ready.")
#sets bots status
    await bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name="ur mum lmao"))
    
@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
    if str(event.author_id) == target:
        for i in list:
            await event.message.add_reaction(i)
        var = randrange(1,3)
        if var == 1:
            await event.message.respond("https://media.discordapp.net/attachments/820047473392877591/990479302963372042/rearendFDVIKFDOFOF.gif")
            print(event.content)
        elif var == 2:
            await event.message.respond(f'"{event.content}" - :nerd:')
            print(event.content)
        else:
            pass


@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
    if event.content.startswith('?add target') == True:
        user = (str(event.content))
        print(user)
        i = len(user)
        user = user[14:i].strip('>')
        global target
        target = user
        print(f"{user} has been made the target" )

bot.run(
    
)
