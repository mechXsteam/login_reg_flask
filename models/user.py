# Define your models

from config import db


class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(120), nullable=False)

        def __repr__(self):
                return '<User %r>' % self.username

        @classmethod
        def return_users(cls):
                return cls.query.all()

        @classmethod
        def create_user(cls, username, password):
                new_user = cls(username=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                return new_user

        @classmethod
        def get_user_by_uname(cls, uname):
                return cls.query.filter_by(username=uname).first()
