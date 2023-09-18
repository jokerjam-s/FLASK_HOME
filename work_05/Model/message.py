from enum import Enum


class _MESSAGE_TYPE(Enum):
    """Виды сообщений, соответствуют применяемым стилям сообщений пользователю."""
    INFO: 'info'
    WARNING: 'warning'
    ERROR: 'error'


class Message:
    """Структура системного сообщения клиенту."""

    def __init__(self, message_text: str, message_type: _MESSAGE_TYPE):
        text = message_text
        message_type = message_type
