from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "EPAM PROJECT START"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "") -> dict[str, str]:
    return {"item_id": f"{item_id}", "q": q}
