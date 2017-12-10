from . import db


class UserInfo(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    __tablename__ = "user_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_name = db.Column(db.String(100), nullable=False, default="")
    user_status = db.Column(db.INTEGER, nullable=False, default=1)
    user_status_name = db.Column(db.String(100), nullable=False, default="")

    def __init__(self, user_name="", user_status=0):
        self.user_name = user_name
        self.user_status = user_status
        self.user_status_name = {0: "无效", 1: "有效"}.get(user_status, "unknown")

    def __repr__(self):
        return '<user_id {} | user_name {} | user_status_name {}>'.format(self.id, self.user_name,
                                                                          self.user_status_name)

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
