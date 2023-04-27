from fastapi import Depends
from sqlalchemy.orm import Session

from app import app
from databasemodel import crud
# 导入需要用到的客户端的Schema -- 开始
from requestschema.studentschema import StudentSchema


# 导入需要用到的客户端的Schema -- 结束

@app.get("/db/data/{tableName}/{skip}/{limit}",
         tags=["db"],
         # 类似于定义当前方法返回的类型
         response_model=list[StudentSchema])
def getData(q: str = "", tableName: str = "", skip: int = 0, limit: int = 10, db: Session = Depends(crud.get_db)):
    """
    可以获取指定表的所有数据，此方法主要用于演示sqlAlchemy的使用，也借助了FastAPI的自动序列化json功能

    :param q: 查询条件

    :param tablename: 数据库中的表名

    :return: 序列化json格式

    :param db: 类似于注入的方式，数据库的信息带入
    """
    # 注意，此时返回的数据是Base类型，是数据库模型
    students = crud.get_user_list(db, skip, limit)
    return students


@app.post("/db/save",
          tags=["db"],
          # 类似于定义当前方法返回的类型
          response_model=StudentSchema)
async def updateData(student: StudentSchema, db: Session = Depends(crud.get_db)):
    """
    接收json类型的字符串，直接自动反序列化为Student对象，
    *注意过多请求攻击*

    :param student: json格式的数据

    :return:
    """
    return crud.save_user(db, student)
