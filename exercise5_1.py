"""
Exercise 5.1
Read the current epoch time and convert it to days, hours, minutes, and seconds.
Author: Tran Ngoc Hieu
MSSV: 25112045
"""

import time

# Get current time in seconds since epoch (Jan 1, 1970)
epoch_time = time.time()

# Calculate days
days = int(epoch_time // (24 * 3600))
remaining_seconds = epoch_time % (24 * 3600)

# Calculate hours
hours = int(remaining_seconds // 3600)
remaining_seconds %= 3600

# Calculate minutes
minutes = int(remaining_seconds // 60)

# Calculate seconds
seconds = int(remaining_seconds % 60)

print("Current time since epoch:")
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)