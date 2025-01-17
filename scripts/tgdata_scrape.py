# scripts/data_scrape.py

from telethon import TelegramClient, events
from telethon.tl.types import Message

# Replace with your API ID, hash, and session file
api_id = 20471194
api_hash = '336d1c62216638c341e58775efe2c4f9'
session_file = 'my_session' 

async def scrape_messages(client, channel_username, limit=100):
    """Scrapes messages from a Telegram channel.

    Args:
        client (TelegramClient): The Telegram client instance.
        channel_username (str): The username of the channel to scrape.
        limit (int, optional): The maximum number of messages to scrape. Defaults to 100.

    Returns:
        list: A list of scraped messages.
    """

    messages = []
    async for message in client.iter_messages(channel_username, limit=limit):
        if isinstance(message, Message):
            messages.append({
                'message_id': message.id,
                'text': message.text,
                'date': message.date,
                # Add other relevant attributes as needed
            })
    return messages
with TelegramClient(session_file, api_id, api_hash) as client:
    channel_username = '@qnashcom' 
    qenash_data = data_scrape.scrape_messages(client, channel_username)

    # Process and analyze the scraped messages
    print(qenash_data)