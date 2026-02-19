from statistics import mean, median, mode

numbers = [i for i in range(1, 20)]
the_mean = mean(numbers)
the_median = median(numbers)
the_mode = mode(numbers)

print(f"Mean: {the_mean}")
print(f"Median: {the_median}")
print(f"Mode: {the_mode}")