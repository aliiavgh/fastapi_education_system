from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Enum, Boolean, sql, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


metadata = MetaData()


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('experience', Enum('лично, частным образои', 'лично, профессионально', 'онлайн', 'другое',
                                   name='experience_user_enum'), nullable=True),
    Column('audience', Enum('лично, частным образои', 'лично, профессионально', 'онлайн', 'другое',
                                   name='experience_user_enum'), nullable=True),
    Column('type', Enum('admin', 'mentor', 'student', name='type_user_enum')),
    Column('password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_mentor', Boolean, default=False, nullable=False),
    Column('first_name', String(50)), 
    Column('last_name', String(50))
)



profile = Table(
    'profile',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), index=True),
    Column('competence', Integer),
    Column('language', String(50)),
    Column('site_url', String(180)),
    Column('twitter_url', String(180), nullable=True),
    Column('facebook_url', String(180), nullable=True),
    Column('linkedin_url', String(180), nullable=True),
    Column('image', Text),
    Column('is_hidden', Boolean),
)
