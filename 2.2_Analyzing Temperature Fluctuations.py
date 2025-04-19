import statistics

def analyze_temperatures(temperatures):
    if not temperatures:
        return {
            'mean': 'N/A',
            'median': 'N/A',
            'std_dev': 'N/A',
            'variance': 'N/A'
        }
    mean = statistics.mean(temperatures)
    median = statistics.median(temperatures)
    if len(temperatures) == 1:
        std_dev = 'N/A'
        variance = 'N/A'
    else:
        std_dev = statistics.stdev(temperatures)
        variance = statistics.variance(temperatures)
    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev,
        'variance': variance
    }

if __name__ == "__main__":
    m = int(input("Enter the number of temperatures: "))
    temps = []
    for i in range(m):
        temp = float(input(f"Enter temperature {i+1}: "))
        temps.append(temp)
    result = analyze_temperatures(temps)
    print("Temperature Analysis Results:")
    print(f"Mean     : {result['mean']}")
    print(f"Median   : {result['median']}")
    print(f"Std Dev  : {result['std_dev']}")
    print(f"Variance : {result['variance']}")