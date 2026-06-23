def minimumLargestDeliveryTime(delivery_times, k):
    x = len(delivery_times) // k
    arr = []

    if x == 1:
        return max(delivery_times)
    
    for i in range(x):
        arr.append(sum(delivery_times[i : x + 1]))

    return max(arr)

print(minimumLargestDeliveryTime([7,2,5,10,8], 2))
print(minimumLargestDeliveryTime([1,4,4], 3))