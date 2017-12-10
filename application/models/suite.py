from . import db
from datetime import datetime


class Suite(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
    __tablename__ = "suite"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    suite_title = db.Column(db.String(100), nullable=False)
    suite_source = db.Column(db.Integer, nullable=False)
    suite_source_name = db.Column(db.String(50), nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    retry_times = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DATETIME, nullable=False)
    update_time = db.Column(db.DATETIME, nullable=False)

    def __init__(self, suite_title="", suite_source=0, creator="", retry_times=3):
        self.suite_title = suite_title
        self.suite_source = suite_source
        self.suite_source_name = {1: "web", 2: "excel", 3: "log", 4: "xml"}.get(suite_source, "unknown")
        self.creator = creator
        self.retry_times = retry_times
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '< suite_title {} | suite_source_name {} | creator {} | retry_times {} >'.format(
            self.suite_title, self.suite_source_name, self.creator, self.retry_times)

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
