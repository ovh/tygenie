import datetime

from tygenie.notification import format_alert_line, is_recent, max_alert_age

UTC = datetime.timezone.utc
NOW = datetime.datetime(2026, 11, 12, 10, 0, 0, tzinfo=UTC)


def test_max_alert_age_default_factor():
    assert max_alert_age(60) == 600
    assert max_alert_age(300, 10) == 3000


def test_recent_alert_is_notified():
    created = NOW - datetime.timedelta(seconds=120)
    assert is_recent(created, NOW, 600) is True


def test_old_alert_is_not_notified():
    created = NOW - datetime.timedelta(hours=3)
    assert is_recent(created, NOW, 600) is False


def test_boundary_is_inclusive():
    created = NOW - datetime.timedelta(seconds=600)
    assert is_recent(created, NOW, 600) is True


def test_missing_created_at_is_notified():
    assert is_recent(None, NOW, 600) is True
    assert is_recent("not a date", NOW, 600) is True


def test_naive_created_at_is_notified():
    assert is_recent(datetime.datetime(2020, 1, 1), NOW, 600) is True


def test_format_alert_line_with_date():
    created = datetime.datetime(2026, 11, 12, 9, 58, tzinfo=UTC)
    line = format_alert_line("disk full", created, "%d/%m %H:%M")
    assert line.startswith("- [12/11 ")
    assert line.endswith("] disk full")


def test_format_alert_line_without_date():
    assert format_alert_line("disk full", None, "%H:%M") == "- disk full"
