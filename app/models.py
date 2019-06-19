from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Comment(db.Model):  # Class Card. Should find a way to rename later.
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(4096))
    content = db.Column(db.String(4096))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    heroes = db.relationship('Hero', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hero_name = db.Column(db.String(4096))
    hero_class = db.Column(db.String(4096))
    hero_race = db.Column(db.String(4096))
    hero_alignment = db.Column(db.String(4096))
    hero_looks = db.relationship('Hero_Looks', backref='hero', lazy='dynamic')

    def __repr__(self):
        return '<id {}, owner_id {}, name {}, hero_class {}, race {}, alignment {}.'.format(self.id, self.owner_id, self.hero_name, self.hero_class, self.hero_race, self.hero_alignment)


class Hero_Looks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    eyes = db.Column(db.String(4096))
    hair = db.Column(db.String(4096))
    clothing = db.Column(db.String(4096))
    body = db.Column(db.String(4096))
    skin = db.Column(db.String(4096))
    symbol = db.Column(db.String(4096))

    def __repr__(self):
        return '<id {}, hero_id {}, eyes {}, hair {}, clothing {}, body {}, skin {}, symbol {}.'.format(self.id, self.hero_id, self.eyes, self.hair, self.clothing, self.body, self.skin, self.symbol)


class LKUPLooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    look_type = db.Column(db.String(4096))
    look_details = db.Column(db.String(4096))

    def __repr__(self):
        return '<id {}, class_name {}, look_type {}, look_details {}'.form(self.id, self.class_name, self.look_type, self.look_details)


class LKUPAlignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    alignment_name = db.Column(db.String(4096))
    
    def __repr__(self):
        return '<id {}, class_name {}, alignment_name {}'.form(self.id, self.class_name, self.alignment_name)