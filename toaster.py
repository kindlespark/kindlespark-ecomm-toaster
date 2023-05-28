from pydantic import BaseModel

class Toaster(BaseModel):
    id: int
    brand: str
    price: float
