def dow(d):
    weekday = ["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    return weekday[(d+1) % 7]