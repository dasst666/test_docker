from pydantic import BaseModel, Field, field_validator, model_validator, HttpUrl, EmailStr
from typing import Literal, Optional
import random
class Address(BaseModel):
    country: str
    city: str

def generate_random_name():
    NAMES = ['Dastan', 'Saken']
    return random.choice(NAMES)

class User(BaseModel):
    name: str = Field(default_factory=generate_random_name)
    age: int = Field(gt=0, lt=120)
    password: str
    password2: str
    non_required_param: Optional[str] = None
    non_required_python_new: str | None = None
    addresses: list[Address] | None = None
    locale: Literal['ru-RU', 'en-US']
    avatar_url: HttpUrl
    email: EmailStr | None = None

    @field_validator('password')
    def validate_password(cls, password, values, **kwargs):
        if '!' in password:
            raise ValueError('not ! in password')
        return password
    
    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password2 != self.password:
            raise ValueError('passwords not equal')
        return self
    


address = Address(city='ALmaty', country='Kazakhstan')

user = User(age=27, 
            password="12345", 
            password2="12345", 
            addresses=[address], 
            locale='ru-RU', 
            avatar_url='http://asdjjklas.com',
            email='asdasd@mail.ru'
            )
user.addresses.append(address)

print(user.model_dump_json())