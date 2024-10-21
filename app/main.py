import uvicorn
from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

from api import router

templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()
app.include_router(router, prefix="/api")


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return {"user_id": user_id}


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post('/register')
async def create_user(user: User):
    return user

users_salary = [{"max": 100000}, {"darina": 200000}, {"vova": 1000}]

@app.get('/read_user/{user_name}')
async def read(user_name: str, count: int = 0):
    return users_salary[count][user_name]


@app.get('/user_salary')
async def get_salary(user_id: int = 0, lyuba: bool = False):
    if lyuba:
        users_salary.append({"lyuba": 100000})
    return users_salary[user_id]

@app.post('/new_name')
async def update_name(new_name: Annotated[str, Query(min_length=3, max_length=20)] = 'max'):
    return {'new_name': new_name}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
