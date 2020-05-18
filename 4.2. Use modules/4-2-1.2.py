import statistics  
from statistics import mean, stdev
scores = [97, 83, 64, 29, 59, 28, 84, 72]  
mean_score = mean(scores)
standard_deviation = stdev(scores)
def standard_score(x):
    return 50 + 10 * (x - mean_score)/standard_deviation
for i in range(10, 100, 10):
    print(standard_score(i))