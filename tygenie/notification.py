"""Helpers for desktop notifications about new alerts.

Kept free of Textual / API client imports so it can be unit tested standalone.
"""

import datetime

# Multiplier applied to refresh_period to compute the maximum age of an alert
# that is still considered "new" for desktop notification purposes.
DEFAULT_MAX_AGE_FACTOR = 10


def max_alert_age(refresh_period: int, factor: int = DEFAULT_MAX_AGE_FACTOR) -> int:
    """Return the maximum age in seconds of an alert eligible for notification."""
    return max(1, int(refresh_period)) * max(1, int(factor))


def is_recent(created_at, now: datetime.datetime, max_age_seconds: int) -> bool:
    """Return True if created_at is within max_age_seconds of now.

    An alert without a usable created_at (None / Unset / naive datetime) is
    treated as recent so that we never silently drop a notification.
    """
    if not isinstance(created_at, datetime.datetime):
        return True
    if created_at.tzinfo is None:
        return True
    if now.tzinfo is None:
        now = now.replace(tzinfo=datetime.timezone.utc)
    age = (now - created_at).total_seconds()
    return age <= max_age_seconds


def format_alert_line(message: str, created_at, date_format: str) -> str:
    """Build one notification body line: '- [HH:MM] message'."""
    if isinstance(created_at, datetime.datetime):
        stamp = created_at.astimezone().strftime(date_format)
        return f"- [{stamp}] {message}"
    return f"- {message}"
