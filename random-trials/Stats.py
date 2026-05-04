import statistics as stx
from statistics import mean, median, mode, stdev
data = [3, 5, 4, 8, 9, 15, 6]

# Trying to use sums and sum for total frequncy, mens and means for mean
n=0
sum = 0
for s in data:
    sum += data[n] 
    n+=1   
    
means = sum/len(data)

print(f"No of observations: {sum}")
print(f"Manually computed mean: {means}")
print(True if sum == mean(data) * len(data) else False)
   

# actual format using Statisstics Library
print("\nTotal number of observations: ", mean(data) * len(data))
print("Mean: ", mean(data))
print("Mode: ", mode(data))
print("Standard Deviation: ", stdev(data))