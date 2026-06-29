class BookMyShow:

    def __init__(self, n: int, m: int):
        self.hall = [[0] * m for _ in range(n)]
        
    def gather(self, k: int, maxRow: int) -> List[int]:
        for i in range(0, maxRow+1):
            firstIndex = self.count_concecutive_occurrence(self.hall[i], k)
            if firstIndex != -1:
                for j in range(firstIndex, firstIndex + k):
                    self.hall[i][j] = 1
                return [i, firstIndex]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        available_seats = sum(row.count(0) for row in self.hall[:maxRow + 1])
        if available_seats < k:
            return False
        for i in range(maxRow + 1):
            for j in range(len(self.hall[i])):
                if self.hall[i][j] == 0:
                    self.hall[i][j] = 1
                    k -= 1
                    if k == 0:
                        return True
    
    def count_concecutive_occurrence(self, lis:[], k:int):
        count = 0
        max_count = 0

        for i in range(len(lis)):
            if lis[i] == 0:
                count += 1
                if count == k:
                    return i - k + 1
            else:
                count = 0
        return -1

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
