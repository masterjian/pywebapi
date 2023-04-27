# 这是一个FastAPI提供的简易WebAPI
import uvicorn
from app import app
import db_opt
import web_opt
# 这是Python程序的入口
if __name__ == '__main__':
    # 启动独角兽服务，监听所有ip，并且自动加载变更
    # 主要是方便了debug开发，否则可以直接在命令行启动就可以
    uvicorn.run(
                "main:app",     # 通过main方法的app对象启动uvicorn
                host="0.0.0.0", # 监听的ip地址
                port=8000,      # 监听的端口号
                reload=True     # 是否在代码改变时自动重新加载
                )