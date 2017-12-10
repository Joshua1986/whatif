from . import db


class TagList(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
    __tablename__ = "tag_list"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    tag_name = db.Column(db.String(100), nullable=False)
    tag_status = db.Column(db.Integer, nullable=False)
    tag_status_name = db.Column(db.String(50), nullable=False)

    def __init__(self, tag_name="", tag_status=0):
        self.tag_name = tag_name
        self.tag_status = tag_status
        self.tag_status_name = {0: "无效", 1: "有效"}.get(tag_status, "unknown")

    def __repr__(self):
        return '<tag_name {} | tag_status {} >'.format(self.tag_name, self.tag_status_name)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
