def minimumLargestDeliveryTime(delivery_times, k):
    left = max(delivery_times)
    right = sum(delivery_times)
    print(f"left {left}, right {right}")

    while left < right:
        mid = (left + right) // 2
        print(f"mid {mid}")

        partitions = 1
        current_sum = 0

        for time in delivery_times:
            print(f"current sum {current_sum} \n")
            if current_sum + time > mid:
                partitions += 1
                current_sum = time
            else:
                current_sum += time
        

        if partitions <= k:
            right = mid
        else:
            left = mid + 1

    return left

print(minimumLargestDeliveryTime([7,2,5,10,8], 2))
print(minimumLargestDeliveryTime([1,4,4], 3))