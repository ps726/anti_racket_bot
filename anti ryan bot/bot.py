from random import *
import hikari, lightbulb

list = {'😳', '💀', '🤓', '😡', '🤡', '🗿', '🤮', '🐟', '🤨', '😐', '😬', '👺', '😼', '🙅‍♂️', '🧍‍♂️', '🎱', '🔇', '☢', '⬇', '❌'}
target = ''

#connects bot to discord API
bot = lightbulb.BotApp(
    token="token"
    )


#prints "bot is ready" when bot was connected to all shards and is ready for use
@bot.listen()
async def on_bot_started(event: hikari.StartedEvent):
    print("Bot is ready.")
#sets bots status
    await bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name="ur mum lmao"))
    
#listens for messages being sent
@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
    print(event.content)
    
    if str(event.author_id) == target:
        #adds reactions to message 
        for i in list:
            await event.message.add_reaction(i)
        #picks what to do
        var = randrange(1,3)
        
        #sends a message telling person to shut up
        if var == 1:
            await event.message.respond("https://cdn.discordapp.com/attachments/994877167638941756/1038724207833526314/unknown.png")
            print(event.content)
       
        #repeats message followed by nerd emoji
        elif var == 2:
            await event.message.respond(f'"{event.content}" - :nerd:')
            print(event.content)

@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
    print(event.content)
    try:
        if event.content.startswith('?add target') == True:
            user = (str(event.content))
            i = len(user)
            user = user[14:i].strip('>')
            global target
            target = user
            print(f"{user} has been made the target" )
    except:
        print('error')

bot.run()
