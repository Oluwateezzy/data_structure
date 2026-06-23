from typing import List
def minimumLargestDeliveryTime(delivery_times:List, k:int):
    x = len(delivery_times) // k
    newArr = []
    res = []

    if x == 1:
        return max(delivery_times)

    for i in range(x):
        res = delivery_times[i + x : x]
        newArr.append(sum(res))

    return max(res)


minimumLargestDeliveryTime([7,2,5,10,8], 2)
minimumLargestDeliveryTime([1, 4, 4], 3)