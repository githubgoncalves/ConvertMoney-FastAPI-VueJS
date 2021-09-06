from decimal import Decimal
from typing import List
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter


class ConvertCurrencyService():

    def convert_currency(from_: str, to_: str, amount_: Decimal) -> Decimal:
        from_ = from_.upper()
        to_ = to_.upper()
        price = Decimal(0.0)
        b = BtcConverter()
        c = CurrencyRates()

        """condições para conversão"""
        if(from_ == "BTC"):
            price = b.convert_btc_to_cur(Decimal(amount_),to_)
        elif(to_ == "BTC"):
            price = b.convert_to_btc(Decimal(amount_),from_)
        else:
            price = c.convert(from_, to_, Decimal(amount_))
        
        return price

   
