from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    completed: bool = False

items = []

@app.get("/items", response_model=List[Item])
def list_items(completed: Optional[bool] = None):
    if completed is None:
        return items
    return [item for item in items if item.completed == completed]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, new_item: Item):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items[idx] = new_item
            return new_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, item in enumerate(items):
        if item.id == item_id:
            items.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Item not found")
