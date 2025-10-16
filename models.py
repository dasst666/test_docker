from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Address(BaseModel):
    country: str
    city: str

class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0, lt=120)
    password: str
    non_required_param: Optional[str] = None
    non_required_python_new: str | None = None
    addresses: list[Address] | None = None

    @field_validator('password')
    def validate_password( )

address = Address(city='ALmaty', country='Kazakhstan')

user = User(name='Dastan', age=130, password="12345", addresses=[address])
user.addresses.append(address)

print(user.model_dump_json())