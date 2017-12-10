from . import db


class CaseTag(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }
    __tablename__ = "case_tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    case_id = db.Column(db.INTEGER, nullable=False)
    tag_id = db.Column(db.INTEGER, nullable=False)

    def __init__(self, case_id=0, tag_id=0):
        self.case_id = case_id
        self.tag_id = tag_id

    def __repr__(self):
        return '<case_id {} | tag_id {} >'.format(self.case_id, self.tag_id)

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
