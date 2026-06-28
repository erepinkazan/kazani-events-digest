#!/usr/bin/env python3
"""
Telegram bot for Kazan Events Digest
Sends a weekly digest of events happening in Kazan
"""

import asyncio
import logging
from datetime import datetime
import pytz

from telegram import Bot
from telegram.error import TelegramError

from config import BOT_TOKEN, CHAT_ID, CHANNELS, TIMEZONE
from telegram_scraper import get_events_from_channels
from digest_formatter import DigestFormatter

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class KazanEventsBot:
    """Bot for sending Kazan events digest"""
    
    def __init__(self, token: str, chat_id: str, channels: dict):
        self.bot = Bot(token=token)
        self.chat_id = chat_id
        self.channels = channels
        self.tz = pytz.timezone(TIMEZONE)
    
    async def send_digest(self):
        """Fetch events and send digest to chat"""
        try:
            logger.info("Starting digest generation...")
            
            # Get events from channels
            events = await get_events_from_channels(self.channels)
            logger.info(f"Found {len(events)} events")
            
            # Format digest
            digest_text = DigestFormatter.format_digest(events, TIMEZONE)
            
            # Send message
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=digest_text,
                parse_mode='HTML',
                disable_web_page_preview=True
            )
            
            logger.info(f"Digest sent successfully to {self.chat_id}")
            print(f"✅ Digest sent at {datetime.now(self.tz)}")
            
        except TelegramError as e:
            logger.error(f"Telegram error: {e}")
            print(f"❌ Error sending digest: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"❌ Unexpected error: {e}")
    
    async def run_scheduled(self):
        """Run bot with scheduled digest"""
        logger.info("Bot started")
        print("🤖 Kazan Events Bot started")
        print(f"📍 Chat ID: {self.chat_id}")
        print(f"📺 Channels: {len(self.channels)}")
        
        # Send digest immediately on startup (for testing)
        await self.send_digest()


async def main():
    """Main entry point"""
    bot = KazanEventsBot(BOT_TOKEN, CHAT_ID, CHANNELS)
    await bot.run_scheduled()


if __name__ == '__main__':
    asyncio.run(main())
