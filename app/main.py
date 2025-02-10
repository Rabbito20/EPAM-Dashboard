from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "EPAM PROJECT START"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Union[str, int] | None]:
    return {"item_id": item_id, "q": q}
