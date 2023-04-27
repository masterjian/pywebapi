from pydantic import BaseModel
from typing import Union
from fastapi import Query


class StudentBase(BaseModel):
    """
        定义的Pydantic的模型类，用于Api和客户端之间的交互

        这是一个基础模型类，可以通过它，扩展传面向查询、更新、插入的模型类
    """

    # 使用【：】是为了实现属性的类型定义
    studentname: str = Query(default=None, max_length=50)
    batchno: Union[int, None] = None  # 如果一个字段不是必选的，可以给予None的默认值
    new_batchno: Union[int, None] = None


class StudentSchema(StudentBase):
    """
    学生实体类
    """
    pass

    class Config:
        # 有了这个，Pydantic模型与 ORM 兼容，您只需在路径操作response_model的参数中声明它即可
        orm_mode = True  # 设置配置值，而不是声明类型，orm_mode将告诉 Pydantic模型读取数据，即它不是一个dict，而是一个 ORM 模型


class StudentSchemaCreate(StudentSchema):
    """
    用于创建学生信息的时候，从客户端接收数据，并返回创建完的数据
    """
    id: int
    class Config:
        orm_mode = True  # 设置配置值，而不是声明类型，orm_mode将告诉 Pydantic模型读取数据，即它不是一个dict，而是一个 ORM 模型
