# ChainlinkBackend

Get the backend of usdt issuance event

---

##  Installation

使用**Python3.6** +

```Bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

cd app

cp settings-example.py settings.py

# 启动项目
uvicorn main:app --reload --host 0.0.0.0

```

# Config

API服务配置

```JSON
# 全局测试状态
DEBUG = False
```
