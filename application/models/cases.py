from . import db
import json
from datetime import datetime


class Cases(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    suite_id = db.Column(db.INTEGER, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    request_type = db.Column(db.INTEGER, nullable=False)
    request_type_name = db.Column(db.String(30), nullable=False)
    method = db.Column(db.INTEGER, nullable=False)
    method_name = db.Column(db.String(30), nullable=False)
    request_url = db.Column(db.String(500), nullable=False)
    request_body = db.Column(db.Text)
    expect_response = db.Column(db.String(500), nullable=False)
    expect_time = db.Column(db.INTEGER, nullable=False)
    case_status = db.Column(db.INTEGER, nullable=False)
    case_status_name = db.Column(db.String(30), nullable=False)
    retry_times = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DATETIME, nullable=False)
    update_time = db.Column(db.DATETIME, nullable=False)

    def __init__(self, suite_id=0, title="", request_type=0, method=0, request_url="", request_body="",
                 expect_response="", expect_time=0, case_status=0, retry_times=3):
        self.suite_id = suite_id
        self.title = title
        self.request_type = request_type
        self.request_type_name = {1:  "http", 2: "dubbo Hessian"}.get(request_type, "unknown")
        self.method = method
        self.method_name = {1: "get", 2: "post form", 3: "post raw"}.get(request_type, "unknown")
        self.request_url = request_url
        self.request_body = json.dumps(request_body)
        self.expect_response = json.dumps(expect_response)
        self.expect_time = expect_time
        self.case_status = case_status
        self.case_status_name = {0: "无效", 1: "有效"}.get(request_type, "unknown")
        self.retry_times = retry_times
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<suite_id {} | title {} | method {} | request_url {} | request_body {} | expect_response {} | expect_time {} >'.format(
            self.suite_id, self.title, self.method_name, self.request_url, self.request_body, self.expect_response,
            self.expect_time)

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
