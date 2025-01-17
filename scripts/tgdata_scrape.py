import pandas as pd
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.types import InputChannel, InputPeerChannel
import asyncio
import os
import nest_asyncio

 # load environmental variable from .env file
load_dotenv()

api_id = os.getenv("api_id")
api_hash= os.getenv("api_hash")

# Replace with your API ID, hash, and session file
api_id = api_id
api_hash = 'api_hash'
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