import datetime
from datetime import datetime, timedelta
import pytz
from dateutil import tz


def get_current_time(*, timzon, fmt):
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    match timzon:
        case 'JST':
            jst = pytz.timezone('Asia/Tokyo')
            current_time = now_utc.astimezone(jst).strftime(f"{fmt}")
        case 'EDT':
            edt = pytz.timezone('US/Eastern')
            current_time = now_utc.astimezone(edt).strftime(f"{fmt}")
        case 'UTC':
            current_time = now_utc.strftime(f"{fmt}")
        case _:
            raise KeyError(f'timezone {timzon} is not supported.')
    return now_utc, current_time


def get_offset_time(*, timzon, fmt, base_time, offset):
    if base_time is None:
        base_time = datetime.datetime.now(datetime.timezone.utc)
    offset_time = base_time + datetime.timedelta(minutes=offset)
    match timzon:
        case 'JST':
            jst = pytz.timezone('Asia/Tokyo')
            fmt_offset_time = offset_time.astimezone(jst).strftime(f"{fmt}")
        case 'EDT':
            edt = pytz.timezone('US/Eastern')
            fmt_offset_time = offset_time.astimezone(edt).strftime(f"{fmt}")
        case 'UTC':
            fmt_offset_time = offset_time.strftime(f"{fmt}")
        case _:
            raise KeyError(f'timezone {timzon} is not supported.')
    return offset_time, fmt_offset_time


def convert_utc_to_local(*, utc_datetime, fmt):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc_datetime = utc_datetime.replace("T", " ").replace("Z", "")
    _utc_datetime = datetime.strptime(utc_datetime, fmt)
    datetime_utc = _utc_datetime.replace(tzinfo=from_zone)
    return datetime_utc.astimezone(to_zone).strftime(fmt).replace(' ', '-')


def convert_local_to_utc(local_datetime, fmt):
    utc_zone = tz.tzutc()
    local_zone = tz.tzlocal()
    local_datetime_list = list(local_datetime)
    local_datetime_list[10] = ' '
    local_datetime = ''.join(local_datetime_list)
    local_time = datetime.strptime(local_datetime, fmt)
    local_time = local_time.replace(tzinfo=local_zone)
    utc_time = local_time.astimezone(utc_zone)
    return utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')