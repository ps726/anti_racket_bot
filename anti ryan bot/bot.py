from subprocess import STARTF_USESHOWWINDOW
import hikari, lightbulb

bot = lightbulb.BotApp(
    token="Token"
    )

@bot.listen()
async def on_bot_started(event: hikari.StartedEvent):
    print("Bot is ready.")
    await bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name="ur mum lmao"))
    
@bot.listen()
async def on_message(event: hikari.MessageCreateEvent):
    if str(event.author_id) == "829239020114280449":
        await event.message.respond("https://media.discordapp.net/attachments/820047473392877591/990479302963372042/rearendFDVIKFDOFOF.gif")
    else:
        print("told ryan to shut up lol")


bot.run(
    
)
