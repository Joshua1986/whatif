# /usr/bin/python
# coding=utf-8
import re

__author__ = 'Administrator'

exp_res_tags = ["IGNORE", "INT", "FLOAT", "STRING", "DATE", "DATETIME", "LIST", "DICT", "IN", "NOT"]
form_tags = ["INT", "FLOAT", "DATE", "DATETIME"]
method_tags = ["POST_RAW", "GET", "POST_FORM", "POST"]


def assert_ignore(v, r):
    return True


def assert_int(v, r1=-9999999999, r2=9999999999):
    return isinstance(v, int) and (v >= r1) and (v <= r2)


def assert_float(v, r1=-9999999999.00, r2=9999999999.00):
    return isinstance(v, float) and (v >= r1) and (v <= r2)


def assert_string(v, r):
    return isinstance(v, str)


def assert_date(v, r1="0000-00-00", r2="9999-99-99"):
    # 正则检查格式
    for i in [v, r1, r2]:
        m = re.match(r"^\d{4}-\d{2}-\d{2}$", i)
        if not m:
            raise RuntimeError("Date 的格式检查错误！" + v)
    return isinstance(v, str) and (v >= r1) and (v <= r2)


def assert_datetime(v, r1="0000-00-00 00:00:00", r2="9999-99-99 99:99:99"):
    # 正则检查格式
    for i in [v, r1, r2]:
        m = re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", i)
        if not m:
            raise RuntimeError("Date 的格式检查错误！" + v)
    return isinstance(v, str) and (v >= r1) and (v <= r2)


def assert_list(v, r):
    return isinstance(v, list)


def assert_dict(v, r):
    return isinstance(v, dict)


def assert_in(v, r):
    return v in r and isinstance(r, list)


def assert_not(v, r):
    return v not in r and isinstance(r, list)


if __name__ == '__main__':
    # print assert_date("2013-01-01", "2012-00-00", "2013-01-99")
    print(assert_datetime("2013-01-01 00:00:00", "2012-00-00", "2013-01-99"))

