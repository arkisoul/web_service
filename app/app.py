from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {"success": True, "message": "Hello World", "error": None, "data": None, "resource": ""}


@app.get('/item/{item_id}')
def read_item(item_id: int):
    return {"success": True, "message": "item", "data": {"item_id": item_id}}
