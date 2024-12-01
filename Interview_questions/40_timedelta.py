# Time Delta:
#     Problem: Given two timestamps, calculate the absolute difference between them in seconds.
#     Example: time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000') should return 25200.

from datetime import datetime

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, format)
    time2 = datetime.strptime(t2, format)
    return abs(int((time1 - time2).total_seconds()))

# Example usage:
print(time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000'))  # Output: 25200
