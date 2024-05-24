import os
from datetime import datetime, date
from pony.orm import Database, Required, PrimaryKey, Set, LongStr, Optional
from passlib.context import CryptContext


db = Database()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(str, unique=True)
    password_hash = Required(str)
    roles = Set('Role')
    reset_token = Optional(str)
    reset_token_expiration = Optional(datetime)
    profiles = Set('UserProfile')


class Role(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str, unique=True)
    users = Set(User)


class UserProfile(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    persons = Set('Person')
    theater_group = Required('TheaterGroup')
    scripts = Set('Script')
    plays = Set('Play')


class PersonType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    persons = Set('Person')


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    biography = Optional(LongStr)
    roles = Set('RoleInPlay')
    person_types = Set(PersonType)
    user_profiles = Set(UserProfile)
    location = Required('Location')
    theater_groups = Set('TheaterGroup')
    scripts = Set('Script')
    plays = Set('Play')


class RoleInPlay(db.Entity):
    id = PrimaryKey(int, auto=True)
    role = Required(str)
    persons = Set(Person)
    play = Required('Play')


class TheaterGroup(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    locations = Set('Location')
    members = Set(Person)
    plays = Set('Play')
    user_profiles = Set(UserProfile)


class Location(db.Entity):
    id = PrimaryKey(int, auto=True)
    city = Required(str, unique=True)
    country = Optional(str, unique=True)
    persons = Set(Person)
    theater_groups = Set(TheaterGroup)
    plays = Set('Play')


class Play(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str, unique=True)
    description = Optional(str)
    date = Optional(date)
    locations = Set(Location)
    theater_groups = Set(TheaterGroup)
    scripts = Set('Script')
    persons = Set(Person)
    user_profiles = Set(UserProfile)
    role_in_plays = Set(RoleInPlay)


class Script(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(LongStr)
    is_open_source = Required(bool)
    intellectual_property_rights = Required(bool)
    summary = Required(str)
    authors = Set(Person)
    plays = Set(Play)
    date = Optional(str)
    user_profiles = Set(UserProfile)


def connect_db():
    if not db.provider:
        try:
            db.bind(
                provider='mysql',
                host=os.environ['MYSQL_HOSTNAME'],
                user=os.environ['MYSQL_USER'],
                passwd=os.environ['MYSQL_PASSWORD'],
                db=os.environ['MYSQL_DATABASE']
            )
            db.generate_mapping(create_tables=True)
        except KeyError as e:
            print(f"Environment variable {e} is not found")
