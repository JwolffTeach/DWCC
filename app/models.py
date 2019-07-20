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
    hero_stats = db.relationship('Hero_Stats', backref='hero', lazy='dynamic')
    # Something with hero_looks is causing a problem- not iterable?

    def __repr__(self):
        return '<id {}, owner_id {}, name {}, hero_class {}, race {}, alignment {}.>'.format(self.id, self.owner_id, self.hero_name, self.hero_class, self.hero_race, self.hero_alignment)


class Hero_Looks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    eyes = db.Column(db.String(100))
    hair = db.Column(db.String(100))
    clothing = db.Column(db.String(100))
    body = db.Column(db.String(100))
    skin = db.Column(db.String(100))
    symbol = db.Column(db.String(100))
    # Code to use in Query:
    # my_hero_eyes = Hero_Looks.query.join(Hero, Hero_Looks.hero_id == Hero.id).group_by(Hero_Looks.id).first().<PROPERTY>
    # That query will actually JOIN the two tables together and pull all the hero_looks for each hero.

    def __repr__(self):
        return '<id {}, hero_id {}, eyes {}, hair {}, clothing {}, body {}, skin {}, symbol {}.>'.format(self.id, self.hero_id, self.eyes, self.hair, self.clothing, self.body, self.skin, self.symbol)

class Hero_Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    hp = db.Column(db.Integer)

    def __repr__(self):
        return '<id {}, hero_id {}, strength {}, dexterity {}, constitution {}, intelligence {}, wisdom {}, charisma {}.>'.format(self.id, self.hero_id, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)

class LKUPLooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    look_type = db.Column(db.String(4096))
    look_details = db.Column(db.String(4096))

    def __repr__(self):
        return '<id {}, class_name {}, look_type {}, look_details {}.>'.format(self.id, self.class_name, self.look_type, self.look_details)

class LKUPRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100))
    race_name = db.Column(db.String(100))

    def __repr__(self):
        return '<id {}. class_name {}, race_name {}.>'.format(self.id, self.class_name, self.race_name)

class LKUPAlignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    alignment_name = db.Column(db.String(4096))
    
    def __repr__(self):
        return '<id {}, class_name {}, alignment_name {}.>'.format(self.id, self.class_name, self.alignment_name)

class LKUPHp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    base_hp = db.Column(db.Integer)

    def __repr__(self):
        return '<id {}, class_name {}, base_hp {}.>'.format(self.id, self.class_name, self.base_hp)

class BasicMoves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    move_name = db.Column(db.String(4096))
    move_description = db.Column(db.String(4096))
    move_details = db.Column(db.String(4096))

class SpecialMoves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    move_name = db.Column(db.String(4096))
    move_description = db.Column(db.String(4096))
    move_details = db.Column(db.String(4096))

class LKUPRaceMoves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(4096))
    move_name = db.Column(db.String(4096))
    move_description = db.Column(db.String(4096))
    move_details = db.Column(db.String(4096))