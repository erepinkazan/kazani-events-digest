#!/usr/bin/env python3
"""
Digest formatter for Kazan Events
Formats events into a nice Telegram message
"""

from datetime import datetime
import pytz


class DigestFormatter:
    """Formats events into digest message"""
    
    # Emoji for different channel types
    CHANNEL_EMOJIS = {
        'delovorot': '💼',
        'sport_y_doma_kzn': '⚽',
    }
    
    CHANNEL_NAMES = {
        'delovorot': 'Деловой Оборот',
        'sport_y_doma_kzn': 'Спорт У Дома',
    }
    
    @staticmethod
    def format_digest(events: list, tz_name: str = 'Europe/Moscow') -> str:
        """
        Format events into a digest message
        
        Args:
            events: List of events from channels
            tz_name: Timezone name
        
        Returns:
            Formatted message text
        """
        if not events:
            return "📭 <b>Еженедельный дайджест</b>\n\n" \
                   "На этой неделе новых событий не найдено 🤔"
        
        # Group events by channel
        events_by_channel = {}
        for event in events:
            channel = event.get('channel', 'unknown')
            if channel not in events_by_channel:
                events_by_channel[channel] = []
            events_by_channel[channel].append(event)
        
        # Build message
        tz = pytz.timezone(tz_name)
        now = datetime.now(tz)
        
        message = f"📬 <b>Еженедельный дайджест событий Казани</b>\n"
        message += f"<i>{now.strftime('%d.%m.%Y %H:%M')}</i>\n\n"
        
        # Add events grouped by channel
        for channel, channel_events in events_by_channel.items():
            emoji = DigestFormatter.CHANNEL_EMOJIS.get(channel, '📌')
            name = DigestFormatter.CHANNEL_NAMES.get(channel, f'@{channel}')
            
            message += f"\n{emoji} <b>{name}</b> ({len(channel_events)})\n"
            message += "─" * 40 + "\n"
            
            # Show first 5 events from each channel
            for i, event in enumerate(channel_events[:5], 1):
                event_date = event['date'].astimezone(tz)
                text = event['text'][:100]  # First 100 chars
                
                if len(event['text']) > 100:
                    text += "..."
                
                message += f"{i}. {text}\n"
                message += f"   <a href='{event['url']}'>→ Читать далее</a>\n\n"
            
            if len(channel_events) > 5:
                message += f"   <i>+ ещё {len(channel_events) - 5} событий</i>\n"
        
        message += "\n" + "=" * 40 + "\n"
        message += "🤖 <i>Автоматический дайджест Казани</i>"
        
        return message
    
    @staticmethod
    def format_event_short(event: dict) -> str:
        """Format single event for short view"""
        text = event['text'][:80]
        if len(event['text']) > 80:
            text += "..."
        return f"• {text}"
