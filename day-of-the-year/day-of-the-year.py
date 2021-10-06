class Solution:
    def dayOfYear(self, date: str) -> int:
        cumulativeDays = {
            '01': 0,
            '02': 31,
            '03': 59,
            '04': 90,
            '05': 120,
            '06': 151,
            '07': 181,
            '08': 212,
            '09': 243,
            '10': 273,
            '11': 304,
            '12': 334,
        }
        
        date = date.split('-')
        days = 0
        
        # leap year
        if int(date[0]) % 4 == 0 and int(date[1]) > 2:
            days += 1
        
        days += cumulativeDays[date[1]] + int(date[2])
        
        return days