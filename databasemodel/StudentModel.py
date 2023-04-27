from sqlalchemy import Column, Integer, String

from database import Base


class Student(Base):
    # 这个__tablename__属性是用来告诉 SQLAlchemy 要在数据库中为每个模型使用的数据库表的名称
    __tablename__ = "students"

    # 下面的每一个变量，都代表其相应数据库表中的一列
    # Integer、String和Boolean是Alchemy的类型，不是Python的
    # 用的[=]定义属性，因为要给它设置初始值
    id = Column(Integer, primary_key=True, index=True)
    studentname = Column(String)
    batchno = Column(Integer)
    new_batchno = Column(Integer)
