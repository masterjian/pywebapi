from typing import Union

from fastapi import FastAPI, status, Depends, HTTPException
# 加载中间件，实现对跨域请求的放行
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

description = """
# pyWebApi让你体验快乐的编程. 🚀

## 说明

1. 基于`FastAPI`，可以快速搭建并提供标准的`WebAPI`请求。

2. 借助`SQLAlchemy`和`Pydantic`实现ORM层和前端数据层的定义和传输

3. 并且支持`OpenAPI`提供的`OAuth2`的认证
"""

app = FastAPI(
    title="pyWebApi",
    description=description,
    version="0.2.4",
    openapi_url="/api/v1/pyWebApi.json",
    docs_url="/docs",  # 设置为none，可以关闭
    redoc_url="/redoc",  # 设置为none，可以关闭
    terms_of_service="https://fastapi.tiangolo.com/",
    contact={
        "name": "TechCity",
        # "url": "https://fastapi.tiangolo.com/",
        "email": "masterjian@outlook.com",
    },
    license_info={
        "name": "Mulan PSL v2",
        "url": "http://license.coscl.org.cn/MulanPSL2",
    }, )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 列举了允许跨域请求的url格式
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://192.168.31.111:8080"
]

# 对常用的跨域请求参数进行设置，毕竟这是一个web服务器
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SysUser(BaseModel):
    """
    定义OAuth2的用户基本信息
    """
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    hashed_password: Union[str, None] = None


def fake_hash_password(password: str):
    """
    接收当前用户的token原始信息，加密后返回给客户端用做token使用

    :param password: 不一定非得是密码，可以是当前用户加密的其他方式

    :return: 加密后的密文
    """
    return "fakehashed_" + password


def fake_decode_token(token):
    """
    根据用户的token（OAuth2的) 返回用户实体
    :param token: 每次请求传递给服务器的token
    :return: 用户实体，token认证通过了，才会返回此值
    """

    return SysUser(
        username=token + "fakedecoded",
        email="john@example.com",
        full_name="Tech City",
        hashed_password= fake_hash_password("123456")
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    自动根据请求中的 `token`，返回认证通过的用户，如果认证失败，直接抛出Http异常
    :param token: 从请求中自动获取
    :return: 认证通过的用户
    """
    sysuser = fake_decode_token(token)
    if not sysuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return sysuser


@app.post("/token",tags=["sys"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    用户凭用户名和密码获得授权通过的token信息
    :param form_data: 包含用户名和密码即可
    :return: 认证成功后的token值
    """
    user_dict = ["not empty"]
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    sysuser = fake_decode_token(form_data.username)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == sysuser.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": sysuser.username, "token_type": "bearer"}


@app.get("/sysuser/me",tags=["sys","demo"])
async def read_users_me(current_user: SysUser = Depends(get_current_user)):
    """
    测试认证通过与否的方法
    :param current_user:
    :return:
    """
    return current_user
