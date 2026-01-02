"""
Write a Python program to map dates (1–31) to weekdays,
 assuming the month starts on Monday.

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


def test(days):
    result = {day: [] for day in days}
    
    for date in range(1, 32):   # 1 to 31
        day_index = (date - 1) % 7
        result[days[day_index]].append(date)
    
    print(result)

test(l1)
