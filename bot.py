import hikari

bot = hikari.GatewayBot(token='')

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    if event.content.startswith("!j"):
        await event.message.respond("This is a test")



bot.run()
