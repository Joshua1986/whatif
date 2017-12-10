from . import db
from datetime import datetime


class Task(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    suite_id = db.Column(db.INTEGER, nullable=False)
    tags = db.Column(db.String(500), nullable=False)
    task_status = db.Column(db.INTEGER, nullable=False)
    task_status_name = db.Column(db.String(50), nullable=False)
    case_number = db.Column(db.INTEGER, nullable=False)
    fail_number = db.Column(db.INTEGER, nullable=False)
    start_time = db.Column(db.DATETIME, nullable=False)
    end_time = db.Column(db.DATETIME, nullable=False)
    duration = db.Column(db.INTEGER, nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DATETIME, nullable=False)
    update_time = db.Column(db.DATETIME, nullable=False)

    def __init__(self, suite_id=0, tags="", task_status=0, case_number=0, fail_number=0, start_time=datetime.now(),
                 end_time=datetime.now(), duration=0, creator=""):
        self.suite_id = suite_id
        self.tags = tags
        self.task_status = task_status
        self.task_status_name = {0: "未开始", 1: "进行中", 2: "执行成功", 3: "执行失败", 4: "执行中断"}.get(task_status, "unknown")
        self.case_number = case_number
        self.fail_number = fail_number
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.creator = creator
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<suite_id {} | tags {} | task_status {} | case_number {} | fail_number {} | start_time {} | duration {} >'.format(
            self.suite_id, self.tags, self.task_status_name, self.case_number, self.fail_number, self.start_time,
            self.duration)

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
