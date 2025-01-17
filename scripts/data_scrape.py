import pandas as pd
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.types import InputChannel, InputPeerChannel
import asyncio
import os
import nest_asyncio

# API ID and hash (replace with your credentials)
api_id = 25986002
api_hash = '903d9d999f9a489212bbcd24075581d6'

# Define session file path
session_file = 'session_name.session'

# Delete the session file if it exists
if os.path.exists(session_file):
    os.remove(session_file)


async def get_messages_from_channel(client, channel_username):
    """
    Fetches messages from a specific Telegram channel.

    Args:
        client: The Telegram client instance.
        channel_username: The username or hash of the channel.

    Returns:
        A list of messages from the channel.
    """

    async with client:
        channel = await client.get_entity(channel_username)
        input_channel = InputChannel(channel.id, channel.access_hash)
        input_peer = InputPeerChannel(channel.id, channel.access_hash)

        messages = await client.get_messages(
            entity=input_peer,
            limit=30  # Fetch the latest 30 messages (adjust as needed)
        )

        return messages


async def main(channel_usernames):
    # Create a Telegram client instance
    client = TelegramClient(session_file, api_id, api_hash)

    # Create an empty list to store all messages
    all_messages = []

    # Loop through each channel and fetch messages
    for channel_username in channel_usernames:
        messages = await get_messages_from_channel(client, channel_username)
        all_messages.extend(messages)  # Add messages to the list
        
    # Create a DataFrame to store the messages
    data = []
    for message in all_messages:
        data.append({
            "channel_username": channel_username,  # Add channel name
            "message_text": message.message
        })

    df = pd.DataFrame(data)

    # Print or save the DataFrame
    print(df)
    df.to_csv('collected_messages.csv', index=False)  # Save to CSV (optional)

    # Return the DataFrame
    return df


if __name__ == '__main__':
    # Apply nest_asyncio patch to allow nested event loops
    nest_asyncio.apply()
    # Execute the main function in the existing event loop
    # Replace with your desired channel usernames
    channel_usernames = ['@qnashcom', '@modernshoppingcenter'] 
    asyncio.run(main(channel_usernames))