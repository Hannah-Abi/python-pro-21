# TEE RATKAISUSI TÄHÄN:
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.date = date 
        self.month = month
        self.year = year
    
    def __str__(self) -> str:
        return f"{self.date}.{self.month}.{self.year}"
    
    def __eq__(self, another) -> bool:
        return f"{self.date}.{self.month}.{self.year}" == f"{another.date}.{another.month}.{another.year}"
    
    def __ne__(self, another) -> bool:
        return f"{self.date}.{self.month}.{self.year}" != f"{another.date}.{another.month}.{another.year}"

    def __gt__(self, another) -> bool:
        if (self.year) > (another.year):
            return True
        elif (self.year) < (another.year):
            return False
        else:
            if (self.month) > (another.month):
                return True
            elif (self.month) < (another.month):
                return False
            else:
                if (self.date) > (another.date):
                    return True
                elif (self.month) <= (another.month):
                    return False
    
    def __lt__(self, another) -> bool:
        if (self.year) > (another.year):
            return False
        elif (self.year) < (another.year):
            return True
        else:
            if self.month > another.month:
                return False
            elif self.month < another.month:
                return True
            else:
                if (self.date) >= (another.date):
                    return False
                elif (self.date) < (another.month):
                    return True
    
    def __add__(self, days: int):
        day_new = self.date
        month_new = self.month
        year_new = self.year
        day_left = (30 - self.date) + (12-self.month)*30
        #print(day_left)
        if days < day_left:
            if days % 30 < 30 - self.date:
                day_new = self.date + days%30
                month_new = self.month + int(days/30)
                #year_new = self.year
            else:
                day_new = (self.date + days%30)%30
                month_new = self.month + int(days/30) + 1
                year_new = self.year
        else:
            days_more = days - day_left
            year_new = self.year + 1 + int(days_more/360)
            month_new = int((days_more % 360)/30) +1
            day_new = (days_more % 360) % 30
        return f"{day_new}.{month_new}.{year_new}"
if __name__=="__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)