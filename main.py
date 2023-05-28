from fastapi import FastAPI
from toaster import Toaster

app = FastAPI()
toaster_list = [
    {
        "id": 1001,
        "brand": "NONAME_BRAND",
        "price": 3241.23
    }
]


@app.get("/")
def toaster_shop():
    print(f"inside toaster_shop")
    return {"message": "Welcome to the Toaster Shop"}


@app.post("/new-toaster")
def add_new_toaster(toaster: Toaster):
    toaster_list.append(toaster.dict())
    return toaster_list


@app.get("/toasters")
def get_all_toasters():
    return toaster_list
