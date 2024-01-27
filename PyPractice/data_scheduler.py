"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""
from datetime import datetime
def date_passed(todays_date, scheduled_date):
#    result_1 = todays_date.split(' ')
#    result_2 = scheduled_date.split(' ')
#
#    if result_1[0][-2:] == "st":
#         today = datetime.datetime.strptime(todays_date, "%dst %B")
#    if result_1[0][-2:] == "nd":
#         today = datetime.datetime.strptime(todays_date, "%dnd %B")  
#    if result_1[0][-2:] == "rd":
#         today = datetime.datetime.strptime(todays_date, "%drd %B")  
#    if result_1[0][-2:] == "th":
#         today = datetime.datetime.strptime(todays_date, "%dth %B")  
#
#    if result_2[0][-2:] == "st":
#         scheduled  = datetime.datetime.strptime(scheduled_date, "%dst %B")
#    if result_2[0][-2:] == "nd":
#         scheduled  = datetime.datetime.strptime(scheduled_date, "%dnd %B")  
#    if result_2[0][-2:] == "rd":
#         scheduled  = datetime.datetime.strptime(scheduled_date, "%drd %B")  
#    if result_2[0][-2:] == "th":
#         scheduled = datetime.datetime.strptime(scheduled_date,  "%dth %B") 



    today = datetime.strptime(todays_date, '%dth %B')
    scheduled = datetime.strptime(scheduled_date, '%dth %B')

    if today < scheduled:
        print("Scheduled date is yet to pass")
    elif today > scheduled:
        print("Scheduled date has passed")
    elif today == scheduled:
        print("Scheduled date is today")

# Test cases
date_passed("26th March", "2th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
