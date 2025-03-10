from pydantic import BaseModel
# A great benefit of Pydantic is that it allows you to define the structure of your data using Python type hints.
# Pydantic uses these type hints to validate the data you pass in and to convert it to the correct type if possible.
# With type hints your code is much easier to work with and you don' t have to remember. Do something like type: 'user' and '.' and it will give hints
# To create a Pydantic model, first define a class
# Then inherit from the BaseModel class
# Then define the fields of the model as class attributes
# Pydantic gives u validation out of the box. This means if you try to create the data with the wrong type, it will raise an error
# Pydantic also gives u data conversion. This means if u pass in a string where an int is expected, Pydantic will try to convert the string to an int
# Pydantic also gives u data parsing. This means if u pass in a dictionary with extra fields, Pydantic will ignore the extra fields
# A user model with 3 fields
class User(BaseModel):
    # inside the class, define the fields of the model as class attributes
    # each field is an instance of the Field class
    name: str
    email: str
    account_id: int

# Create an instance of the model
user = User(name="John", email="john@pixegami.io", account_id=12345)

user_data = {
    'name': 'John',
    'email': 'john@pixegami.io',
    'account_id': 12345
}
# u can also do this by unpacking a dictionary. this works well if you already have the data. Ie. u have
# the respose from an API call
user = User(**user_data)
# if the data u passed in is valid, the model will be created successfully
print(user)
# user2 = User(name="John", email="mikeo@mail.com", account_id="hello")
# print(user2)
from pydantic import BaseModel,EmailStr,validator
class realEmailUser(BaseModel):
    name: str
    email: EmailStr
    account_id: int

# realEmailUser will only accept valid email addresses
# realemailuser = realEmailUser(name="John", email="mike", account_id=12345)
# print(realemailuser)

# if the validation doesn't cover our needs, we can create custom validators

@validator("account_id")
def validate_account_id(cls,value):
    if value <= 0:
        raise ValueError("account_id must be greater than 0")
    return value

baduser = User(name="jack",email="jill@mail.com",account_id=-1)
print(baduser)