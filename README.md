# connect to DB
```
python -m pip install "pymongo[srv]"
```
refer to connect_example.py 

# backend
```
pip install fastapi
pip install python-jose[cryptography]

```
to run dev server
```
fastapi dev main.py
uvicorn main:app --host 0.0.0.0 --port 8001
```
