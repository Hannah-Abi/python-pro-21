# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, another):
        return float(f"{self._euros}.{self._cents:02d}") == float(f"{another._euros}.{another._cents:02d}")
    
    def __gt__(self, another):
        return float(f"{self._euros}.{self._cents:02d}") > float(f"{another._euros}.{another._cents:02d}")
    
    def __lt__(self, another):
        return float(f"{self._euros}.{self._cents:02d}") < float(f"{another._euros}.{another._cents:02d}")

    def __ne__(self, another):
        return float(f"{self._euros}.{self._cents:02d}") != float(f"{another._euros}.{another._cents:02d}")
    
    def __add__(self, another):
        val = float(f"{self._euros}.{self._cents:02d}") + float(f"{another._euros}.{another._cents:02d}")
        val = f"{val:.2f} eur"
        return val
    def __sub__(self, another):
        val = float(f"{self._euros}.{self._cents:02d}") - float(f"{another._euros}.{another._cents:02d}")
        if val < 0:
            raise ValueError("a negative result is not allowed")
        val = f"{val:.2f} eur"
        return val

if __name__=="__main__":
    e1 = Money(1, 0)
    e2 = Money(1, 0)
    print(e1 == e2)
        


