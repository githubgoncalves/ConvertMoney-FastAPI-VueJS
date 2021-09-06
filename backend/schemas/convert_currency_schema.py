from decimal import Decimal
from pydantic import BaseModel

class ConvertCurrencySchema(BaseModel): #serializer
    from_:str
    amount_: Decimal
    to_:str 
    price: Decimal


