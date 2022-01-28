# ChainlinkBackend

Get the backend of usdt issuance event

---

##  Installation

use **Python3.6** + 、**npm8.1.2** +

## backend
```Bash
virtualenv venv

source venv/bin/activate
# if system is windows:
# cd venv/Scripts/
# activate

pip install -r requirements.txt

cd app_backend

cp settings-example.py settings.py

# run the backend server
uvicorn main:app_backend --reload --host 127.0.0.1

check swagger document /docs

```
## front
```Bash
# run the front server
npm run dev
# Config
```

API Service Configuration

```JSON```
# Global test status
DEBUG = False

