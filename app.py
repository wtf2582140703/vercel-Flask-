从 flask 导入 Flask

app = 烧瓶(__name__)

@app.route()'/'
定义 你好，世界():
    返回 '你好，世界!'

如果 __name__ == "__main__":
    app.运行(调试=True, 主机=)"0.0.0.0", 端口=5000
