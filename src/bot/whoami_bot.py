import asyncio

from telebot.async_telebot import AsyncTeleBot

TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"

whoami_bot = AsyncTeleBot(token=TELEGRAM_BOT_TOKEN)


MESSAGE_TEMPLATE = (
    r"""👋 Hi {first_name}\!
    your user ID is:
    

    `{user_id}`
    

    *How to copy your ID 📋:*
    \- *On PC 💻:* Just click on the user ID\.
    \- *On Mobile 📱:* Simply tap the user ID with your finger\."""
)


@whoami_bot.message_handler(func=lambda msg: True)
async def handle_message(message):

    await whoami_bot.send_message(
        message.chat.id,
        MESSAGE_TEMPLATE.format(
            first_name=message.from_user.first_name,
            user_id=message.from_user.id
        ),
        parse_mode="markdownv2"
    )


def run():
    asyncio.run(whoami_bot.polling())