class Solution():
    # Define the set which avoid duplicates

    def __init__(self):
        self.duplicates = set()

    def containsDuplicate(self, nums):
        for num in nums:
            if num in self.duplicates:
                return True
            self.duplicates.add(num) 
        return False

# Driver code 
if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,4,1]))





