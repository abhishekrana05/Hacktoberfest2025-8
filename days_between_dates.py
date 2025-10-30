# ------------------------------------------------------------
# Days Between Two Dates
# Description:
#   Calculates the number of days between two given dates.
# Author: Abhishek Rana
# ------------------------------------------------------------

from datetime import datetime

def days_between(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

if __name__ == "__main__":
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")
    print(f"Days between: {days_between(date1, date2)}")
