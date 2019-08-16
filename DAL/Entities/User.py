from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR, PrimaryKeyConstraint, UniqueConstraint, ForeignKey, FLOAT

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', INTEGER, autoincrement=True)
    login = Column('login', VARCHAR(50), nullable=False)
    password = Column('password', VARCHAR(50), nullable=False)
    tg_channel = Column('tg_channel', VARCHAR(30), nullable=False)
    vk_token = Column('vk_token', VARCHAR(200), nullable=False)
    epn_token = Column('epn_token', VARCHAR(200), nullable=False)
    start_timer = Column('start_timer', INTEGER, nullable=False)
    end_timer = Column('end_timer', INTEGER, nullable=False)
    last_post_time = Column('last_post_time', VARCHAR(200), nullable=False)
    post_iteration_counter = Column('post_iteration_counter', INTEGER, nullable=False)
    post_iteration = Column('post_iteration', INTEGER, nullable=False)

    PrimaryKeyConstraint(id, name='PK_User_Id')
    UniqueConstraint(login, name="UQ_User_Login")
    UniqueConstraint(vk_token, name="UQ_User_Vk_token")
    UniqueConstraint(epn_token, name="UQ_User_Epn_token")
