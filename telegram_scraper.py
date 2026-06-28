#!/usr/bin/env python3
"""
Telegram channel scraper for Kazan Events Digest
Fetches recent messages from specified channels
"""

import asyncio
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class MockScraper:
    """Mock scraper for testing - returns sample events"""
    
    @staticmethod
    async def get_sample_events() -> list:
        """Get sample events for testing"""
        now = datetime.now()
        
        return [
            {
                'text': '💼 Конференция "Цифровая трансформация бизнеса" - начало в 10:00',
                'date': now,
                'channel': 'delovorot',
                'message_id': 1,
                'url': 'https://t.me/delovorot/1'
            },
            {
                'text': '💼 Вебинар по маркетингу и продажам для предпринимателей',
                'date': now - timedelta(hours=1),
                'channel': 'delovorot',
                'message_id': 2,
                'url': 'https://t.me/delovorot/2'
            },
            {
                'text': '⚽ Футбольный матч: "Рубин" vs "Локомотив" - 19:00 на стадионе "Центральный"',
                'date': now - timedelta(hours=2),
                'channel': 'sport_y_doma_kzn',
                'message_id': 3,
                'url': 'https://t.me/sport_y_doma_kzn/3'
            },
            {
                'text': '⚽ Тренировка по волейболу каждый вторник в 18:00, спортзал №5',
                'date': now - timedelta(hours=3),
                'channel': 'sport_y_doma_kzn',
                'message_id': 4,
                'url': 'https://t.me/sport_y_doma_kzn/4'
            },
            {
                'text': '💼 Семинар для фрилансеров: как найти первых клиентов',
                'date': now - timedelta(hours=4),
                'channel': 'delovorot',
                'message_id': 5,
                'url': 'https://t.me/delovorot/5'
            },
        ]


async def get_events_from_channels(channels: dict) -> list:
    """
    Main function to get events from channels
    Currently returns mock data for testing
    
    Args:
        channels: List of channel configs (not used in mock version)
    
    Returns:
        List of events
    """
    logger.info("Fetching sample events (mock mode)...")
    events = await MockScraper.get_sample_events()
    logger.info(f"Retrieved {len(events)} sample events")
    return events
