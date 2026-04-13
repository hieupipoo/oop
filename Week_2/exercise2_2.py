"""
Exercise 2.2
Author: Tran Ngoc Hieu
MSSV: 25112045
"""

import math

# 1. Volume of a sphere with radius = 5
r = 5
volume = (4/3) * math.pi * r**3

print("1. Volume of sphere with radius 5:", volume)


# 2. Total wholesale cost for 60 books
cover_price = 24.95
discount = 0.40
price_after_discount = cover_price * (1 - discount)

first_copy_shipping = 3
additional_shipping = 0.75
copies = 60

shipping_cost = first_copy_shipping + (copies - 1) * additional_shipping
total_cost = copies * price_after_discount + shipping_cost

print("2. Total wholesale cost for 60 books:", total_cost)


# 3. Running time calculation
start_time_minutes = 6 * 60 + 52  # 6:52 AM in minutes

easy_pace = 8 * 60 + 15  # seconds per mile
tempo_pace = 7 * 60 + 12 # seconds per mile

# Run distances
easy1 = easy_pace
tempo = 3 * tempo_pace
easy2 = easy_pace

total_run_seconds = easy1 + tempo + easy2
total_run_minutes = total_run_seconds / 60

finish_time_minutes = start_time_minutes + total_run_minutes

hours = int(finish_time_minutes // 60)
minutes = int(finish_time_minutes % 60)

print("3. Time you get home for breakfast:", f"{hours}:{minutes:02d} AM")