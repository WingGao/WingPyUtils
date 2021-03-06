# coding=utf-8
__author__ = 'wing'
from django.utils import timezone
import datetime
from ..time_ import get_datetime_milliseconds


def get_local_day_min(dt=None, year=None, month=None, day=None, utc=True):
    """讲时间转换成 本地时0点 并转换成UTC
    :param dt:
    :param navie:
    :return:
    """
    if dt is None:
        tm = timezone.now()
    elif timezone.is_aware(dt):
        tm = timezone.make_naive(dt)
    else:
        tm = dt
    if year is not None:
        tm = tm.replace(year=year)
    if month is not None:
        tm = tm.replace(month=month)
    if day is not None:
        tm = tm.replace(day=day)
    tm = datetime.datetime.combine(tm, datetime.time.min)
    # 计算后的tm没有tzinfo
    tm = timezone.make_aware(tm)
    if utc:
        tm = timezone.make_naive(tm, timezone.utc)
        return tm.replace(tzinfo=timezone.utc)
    else:
        return tm


def next_day(daytime):
    return daytime + datetime.timedelta(days=1)


def get_now_milliseconds(utc=True):
    return get_datetime_milliseconds(timezone.now(), utc=utc)
