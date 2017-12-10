from . import db
from datetime import datetime
import json


class CaseResult(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    __tablename__ = "case_result"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    task_id = db.Column(db.INTEGER, nullable=False)
    case_id = db.Column(db.INTEGER, nullable=False)
    actual_result = db.Text
    retry_time = db.Column(db.INTEGER, nullable=False)
    result_status = db.Column(db.INTEGER, nullable=False)
    result_status_name = db.Column(db.String(50), nullable=False)
    fail_reason = db.Text
    duration = db.Column(db.INTEGER, nullable=False)
    create_time = db.Column(db.DATETIME, nullable=False)
    update_time = db.Column(db.DATETIME, nullable=False)

    def __init__(self, task_id=0, case_id=0, actual_result="", retry_time=0, result_status=0, fail_reason="",
                 duration=0):
        self.task_id = task_id
        self.case_id = case_id
        self.actual_result = json.dumps(actual_result)
        self.retry_time = retry_time
        self.result_status = result_status
        self.result_status_name = {0: "未开始", 1: "进行中", 2: "执行成功", 3: "执行失败", 4: "执行中断"}.get(result_status, "unknown")
        self.fail_reason = json.dumps(fail_reason)
        self.duration = duration
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<task_id {} | case_title {} | case_status {} | method_name {} | request_url {} | request_body {} | actual_response {} >'.format(
            self.task_id, self.case_title, self.case_status, self.method_name, self.request_url, self.request_body,
            self.actual_response)

    def save(self):
        self.create_time = datetime.now()
        self.update_time = datetime.now()
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        self.update_time = datetime.now()
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
