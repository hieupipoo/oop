"""
Think Python - Chapter 1
Exercise 1.2
Author: Hieu Tran
"""

# 1. How many seconds are there in 42 minutes 42 seconds?

minutes = 42
seconds = 42
total_seconds = minutes * 60 + seconds

print("1. Total seconds in 42 minutes 42 seconds:", total_seconds)


# 2. How many miles are there in 10 kilometers?
# Given: 1 mile = 1.61 kilometers

kilometers = 10
miles = kilometers / 1.61

print("2. Miles in 10 kilometers:", miles)


# 3. Average pace and average speed
# Running 10 km in 42 minutes 42 seconds

time_seconds = total_seconds
time_hours = time_seconds / 3600

# Average speed (miles per hour)
average_speed = miles / time_hours

# Average pace (minutes per mile)
pace_seconds = time_seconds / miles
pace_minutes = int(pace_seconds // 60)
pace_remaining_seconds = pace_seconds % 60

print("3. Average speed:", average_speed, "miles per hour")
print("   Average pace:", pace_minutes, "minutes", round(pace_remaining_seconds, 2), "seconds per mile")