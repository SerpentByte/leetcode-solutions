class Solution:
    # function to return the indices
    def twoSum(self, arr, add):
        idx = []

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == add:
                    return [i, j]

        return [i, j]

arr = [[13, 2, 11, 7, 12], [2, 5, 5, 11]]
add = [19, 10]
output = [[3, 4], [1, 2]]
print(Solution().twoSum(arr[1], add[1]), output[1])

# accepted.
# run time: 2s
# better than 47%
