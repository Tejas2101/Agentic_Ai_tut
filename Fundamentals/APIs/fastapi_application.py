# To run - uv run fastapi dev Fundamentals/APIs/fastapi_application.py




from fastapi import FastAPI

items =[]

# Creating app
app = FastAPI()

@app.get('/')
def root():
    return {"message":"Hello World"}

@app.post('/items')
def create_item(item:str):
    items.append(item)
    return items

## adding from terminal -- curl -X POST -H "Content-type: application/json" 'http://127.0.0.1:8000/items?item=apple'

@app.get("/items/{item_id}")
def get_item(item_id:int)-> str:
    item = items[item_id]
    return item

# getting item in terminal -- curl -X GET 'http://127.0.0.1:8000/items/0' 