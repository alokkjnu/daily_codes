"""
Write a Python program to map dates (1–31) to weekdays,
 assuming the month starts on Monday.
last_date = 31
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
{
 'monday': [1, 8, 15, 22, 29],
 'tuesday': [2, 9, 16, 23, 30],
 'wednesday': [3, 10, 17, 24, 31],
 'thursday': [4, 11, 18, 25],
 'friday': [5, 12, 19, 26],
 'saturday': [6, 13, 20, 27],
 'sunday': [7, 14, 21, 28]
}
"""

class MapDate:

    def __init__(self,days,last_date):

        self.days = days
        self.last_date = last_date

    def map_dates_to_weekdays(self):

        res = {day:[] for day in self.days}
        for date in range(1,self.last_date+1):
            day_index = (date-1)%7
            res[self.days[day_index]].append(date)

        return res

if __name__ == "__main__":
    last_date = 31
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    cls_obj = MapDate(days,last_date)
    res = cls_obj.map_dates_to_weekdays()
    print(res)