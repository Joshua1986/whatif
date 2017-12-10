from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct
from datetime import datetime
from .. import app

db = SQLAlchemy(app)

from .suite import Suite
from .cases import Cases
from .case_tag import CaseTag
from .tag_list import TagList
from .task import Task
from .case_result import CaseResult
from .user_info import UserInfo


def add_user_info(user_name=""):
    user = query_user_info(user_name=user_name)
    if user:
        return user
    else:
        user = UserInfo(user_name=user_name, user_status=1)
        return user.save()


def query_user_info(user_id=None, user_name=None, user_status=None):
    filters = set()
    if user_id:
        filters.add(UserInfo.id == user_id)
    if user_name:
        filters.add(UserInfo.user_name == user_name)
    if user_status:
        filters.add(UserInfo.user_status == user_status)
    return UserInfo.query.filter(*filters).all()


def add_suite(suite_title="", suite_source=0, creator="", retry_times=3):
    if not query_user_info(user_name=creator):
        return None
    s = Suite(suite_title=suite_title, suite_source=suite_source, creator=creator, retry_times=retry_times)
    return s.save()


def query_suite(suite_id=None, suite_title=None, suite_source=None, creator=None):
    filters = set()
    if suite_id:
        filters.add(Suite.id == suite_id)
    if suite_title:
        filters.add(Suite.suite_title == suite_title)
    if suite_source:
        filters.add(Suite.suite_source == suite_source)
    if creator:
        filters.add(Suite.creator == creator)
    return Suite.query.filter(*filters).all()


def add_cases(suite_id=0, title="", request_type=0, method=0, request_url="", request_body="", expect_response="",
              expect_time=0, case_status=0, retry_times=3, tags=None):
    cases = Cases(suite_id=suite_id, title=title, request_type=request_type, method=method, request_url=request_url,
                  request_body=request_body, expect_response=expect_response, expect_time=expect_time,
                  case_status=case_status, retry_times=retry_times)
    cases.save()
    if tags:
        for tag in tags:
            t = query_tag_list(tag_name=tag)
            if not t:
                tag_id = add_tag_list(tag_name=tag).id
            else:
                tag_id = t[0].id
            CaseTag(case_id=cases.id, tag_id=tag_id).save()
    return cases


def query_cases(case_id=None, suite_id=None, title=None, request_type=None, method=None, request_url=None,
                case_status=None):
    filters = set()
    if case_id:
        filters.add(Cases.id == case_id)
    if suite_id:
        filters.add(Cases.suite_id == suite_id)
    if title:
        filters.add(Cases.title == title)
    if request_type:
        filters.add(Cases.request_type == request_type)
    if method:
        filters.add(Cases.method == method)
    if request_url:
        filters.add(Cases.request_url == request_url)
    if case_status:
        filters.add(Cases.case_status == case_status)
    return Cases.query.filter(*filters).all()


def query_cases_id_by_tag(tags=None):
    cases_id = db.session.query(distinct(CaseTag.case_id)) \
        .join(TagList, TagList.id == CaseTag.tag_id) \
        .filter(TagList.tag_name.in_(tags), TagList.tag_status == 1) \
        .all()
    if cases_id:
        return [c[0] for c in cases_id]
    else:
        return []


def add_tag_list(tag_name=""):
    tag = TagList(tag_name=tag_name, tag_status=1)
    return tag.save()


def query_tag_list(tag_name=None, tag_status=None):
    filters = set()
    if tag_name:
        filters.add(TagList.tag_name == tag_name)
    if tag_status:
        filters.add(TagList.tag_status == tag_status)
    return TagList.query.filter(*filters).all()


def add_task(suite_id=0, tags="", task_status=0, case_number=0, fail_number=0, start_time=datetime.now(),
             end_time=datetime.now(), duration=0, creator=""):
    task = Task(suite_id=suite_id, tags=tags, task_status=task_status, case_number=case_number, fail_number=fail_number,
                start_time=start_time, end_time=end_time, duration=duration, creator=creator)
    return task.save()


def query_task(task_id=None, suite_id=None, task_status=None, case_number=None, fail_number=None,
               start_time=None, end_time=None, creator=None):
    filters = set()
    if task_id:
        filters.add(Task.task_id == task_id)
    if suite_id:
        filters.add(Task.suite_id == suite_id)
    if task_status:
        filters.add(Task.task_status == task_status)
    if case_number:
        filters.add(Task.case_number == case_number)
    if fail_number:
        filters.add(Task.fail_number == fail_number)
    if start_time:
        filters.add(Task.start_time == start_time)
    if end_time:
        filters.add(Task.end_time == end_time)
    if creator:
        filters.add(Task.creator == creator)
    return Task.query.filter(*filters).all()


def add_case_result(task_id=0, case_id=0, actual_result="", retry_time=0, result_status=0, fail_reason="", duration=0):
    if query_case_result(task_id=task_id, case_id=case_id):
        return None
    cr = CaseResult(task_id=task_id, case_id=case_id, actual_result=actual_result, retry_time=retry_time,
                    result_status=result_status, fail_reason=fail_reason, duration=duration)
    return cr.save()


def query_case_result(case_result_id=None, task_id=None, case_id=None, retry_time=None, result_status=None):
    filters = set()
    if case_result_id:
        filters.add(CaseResult.id == case_result_id)
    if task_id:
        filters.add(CaseResult.task_id == task_id)
    if case_id:
        filters.add(CaseResult.case_id == case_id)
    if retry_time:
        filters.add(CaseResult.retry_time == retry_time)
    if result_status:
        filters.add(CaseResult.result_status == result_status)
    return CaseResult.query.filter(*filters).all()
