from telegram import Bot

async def main():
    bot = Bot(token="6367719855:AAGaBiARqE2P6WqwPeNbFJaaQFcrOnrvZGo")
    updates = await bot.get_updates()

    if updates:
        chat_id = updates[0].message.chat.id
        print("Owner's Chat ID:", chat_id)

# Run the asyncio event loop to execute the coroutine
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
