#!/usr/bin/env python3
"""
Telegram channel scraper for Kazan Events Digest
Fetches recent messages from specified channels
"""

import asyncio
import logging
from datetime import datetime, timedelta
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os

logger = logging.getLogger(__name__)

# Telegram API credentials (you need to get these from https://my.telegram.org/apps)
API_ID = int(os.getenv('TELEGRAM_API_ID', '12345'))
API_HASH = os.getenv('TELEGRAM_API_HASH', 'your_api_hash')


class TelegramScraper:
    """Scrapes events from Telegram channels"""
    
    def __init__(self):
        self.client = TelegramClient('scraper_session', API_ID, API_HASH)
    
    async def connect(self):
        """Connect to Telegram"""
        if not self.client.is_connected():
            await self.client.connect()
    
    async def disconnect(self):
        """Disconnect from Telegram"""
        if self.client.is_connected():
            await self.client.disconnect()
    
    async def get_channel_messages(self, channel_username: str, limit: int = 10) -> list:
        """
        Get recent messages from a channel
        
        Args:
            channel_username: Channel username without @
            limit: Number of messages to fetch
        
        Returns:
            List of message objects
        """
        try:
            messages = []
            async for message in self.client.iter_messages(f'@{channel_username}', limit=limit):
                if message.text:
                    messages.append({
                        'text': message.text,
                        'date': message.date,
                        'channel': channel_username,
                        'message_id': message.id,
                        'url': f'https://t.me/{channel_username}/{message.id}'
                    })
            return messages
        except Exception as e:
            logger.error(f"Error fetching messages from @{channel_username}: {e}")
            return []
    
    async def get_events_from_channels(self, channels: dict) -> list:
        """
        Fetch events from multiple channels
        
        Args:
            channels: Dict with channel info {'name': 'delovorot', 'limit': 10}
        
        Returns:
            List of all events
        """
        await self.connect()
        all_events = []
        
        try:
            for channel_info in channels:
                username = channel_info.get('username', '').replace('@', '').replace('https://t.me/', '')
                limit = channel_info.get('limit', 10)
                
                logger.info(f"Fetching messages from @{username}...")
                messages = await self.get_channel_messages(username, limit)
                all_events.extend(messages)
            
            return sorted(all_events, key=lambda x: x['date'], reverse=True)
        finally:
            await self.disconnect()


async def get_events_from_channels(channels: dict) -> list:
    """
    Main function to get events from channels
    
    Args:
        channels: List of channel configs
    
    Returns:
        List of events
    """
    scraper = TelegramScraper()
    return await scraper.get_events_from_channels(channels)
