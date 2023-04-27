from typing import Union
from fastapi import Cookie, Response, Depends

from app import app,oauth2_scheme


def print_hi(name: str):
    """
    这个方法是一个普通的python对（程序）公开的方法，不能用于webapi
    :param name:
    :return:
    """
    print(f'Hi, {name}')

    if len(name) > 4:
        print(f"{name}的长度是{len(name)}")


@app.get('/hi', tags=["web-demo"])
async def hi(res: Response):
    """
    返回一个helloworld的测试字符串，并通过Response向客户端写入cookie值
    """

    res.set_cookie("code", "1234567")
    return {"message": "hello,world"}


@app.post("/hi", tags=["web"])
def post_hi(p1: str):
    """
    从post接收一个参数，并返回回去

    :param p1: 从post接收的参数

    :return: 返回的值
    """
    return {"msg": p1}


@app.get("/hi/{id}", tags=["web"])
def get_hi_path(id: int,
                code: Union[str, None] = Cookie(default=None, max_length=50),
                token: str = Depends(oauth2_scheme)):
    """
    演示从路径参数获取传入参数，并从cookie中自动获取相关的值，并且可以使用Query类似的验证功能

    **加入了openapi的OAuth2的验证机制**

    通过在请求头中加入`Authorization` 值的类型是 `Bearer + 空格 + 获得的token`

    :param id: 要求此值必须是整型

    :return:
    """

    return {"msg": id, "data": code}
