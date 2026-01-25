temp_arr = []
def merge(nums1:list, nums2:list, m:int, n:int):
    temp_arr = nums1[:m]
    for i in range(n):
        temp_arr.append(nums2[i])
    temp_arr.sort()
    for j in range(len(temp_arr)):
        nums1[j] = temp_arr[j]
    nums1.sort()
    print(nums1)

merge([1,2,3,0,0,0], [2,5,6], 3, 2)
        


# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# python types 