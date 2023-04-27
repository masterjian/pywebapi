from sqlalchemy.orm import Session

from database import SessionLocal
from databasemodel.StudentModel import Student
from requestschema.studentschema import StudentSchema


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(db: Session, stu_id: int):
    return db.query(Student).first()


def get_user_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()


def save_user(db: Session, stu: StudentSchema):
    """
    实现接收json信息，并自动传递数据库的功能
    :param db: db session
    :param stu: 客户端过来的schema
    :return: 插入成功后的数据
    """
    # 从schema到 model的转换（如果是更新的话，注意防止过多提交攻击）
    # data = Student(studentname=stu.studentname,batchno=stu.batchno,new_batchno=stu.new_batchno)
    data = Student(**stu.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
