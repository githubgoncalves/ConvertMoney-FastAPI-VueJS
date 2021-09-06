from fastapi import APIRouter,status
from services.convert_currency_service import ConvertCurrencyService

route = APIRouter()

@route.get('/convert-currency', status_code=status.HTTP_200_OK,response_model=dict)
async def convert_currency(from_: str, to_:  str, amount_= 1):
    price = ConvertCurrencyService.convert_currency(from_,to_,amount_)
    convert =  {"from_": from_.upper(),"amount_": amount_,"to_": to_.upper(), "price":price}
    return convert


