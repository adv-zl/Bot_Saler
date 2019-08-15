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
    start_timer = Column('start_timer', VARCHAR(5), nullable=False)
    end_timer = Column('end_timer', VARCHAR(5), nullable=False)
    last_post_time = Column('last_post_time', VARCHAR(200), nullable=False)
    post_iteration_counter = Column('post_iteration_counter', INTEGER, nullable=False)
    post_iteration = Column('post_iteration', INTEGER, nullable=False)

    PrimaryKeyConstraint(id, name='PK_User_Id')
    UniqueConstraint(login, name="UQ_User_Login")
    UniqueConstraint(vk_token, name="UQ_User_Vk_token")
    UniqueConstraint(epn_token, name="UQ_User_Epn_token")


class Group(Base):
    __tablename__ = 'group'

    id = Column('id', INTEGER, autoincrement=True)
    vk_group_id = Column('vk_group_id', VARCHAR(50), nullable=False)
    user_id = Column('user_id', INTEGER, ForeignKey("user.id"), nullable=False)

    PrimaryKeyConstraint(id, name='PK_Group_Id')
    UniqueConstraint(vk_group_id, name="UQ_Group_Group_id")


class Link(Base):
    __tablename__ = "link"

    id = Column('id', INTEGER, autoincrement=True)
    image = Column('image', VARCHAR(1000), nullable=False)
    title = Column('title', VARCHAR(1000), nullable=False)
    url = Column('url', VARCHAR(1000), nullable=False)
    price = Column('price', FLOAT, nullable=False)
    sale = Column('sale', INTEGER, nullable=False)
    group_id = Column('group_id', INTEGER, ForeignKey("group.id"), nullable=False)

    PrimaryKeyConstraint(id, name="PK_Link_Id")
    UniqueConstraint(url, name="UQ_Link_Url")


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import json

    with open('config.json') as json_file:
        db_data = json.load(json_file)["postgresql"]

    engine = create_engine(f"postgresql://{db_data['user']}:{db_data['password']}@{db_data['host']}:{db_data['port']}/"
                           f"{db_data['db']}")
    Base.metadata.create_all(bind=engine)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    #
    # session.add(User(login='admin', password="admin", tg_channel="@channel", vk_token="vk_token", epn_token="epn_token",
    #                  start_timer='9', end_timer="21", last_post_time="2321432545", post_iteration_counter=21,
    #                  post_iteration=2))
    # session.add(Group(vk_group_id="-34567", user_id=1))
    # session.add(Link(image="image", title="easy_image", url="simple_url", price=254.24, sale=24, group_id=1))
    # session.commit()
    # session.close()




