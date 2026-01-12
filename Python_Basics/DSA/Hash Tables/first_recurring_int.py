# for a given array of integers return the integer that occurs more than once first
# [2,3,4,5,6,7,8,2,2,4,4,1] 
# OP : 2

def first_recur(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i+1, len_lst):
            if lst[i] == lst[j]:
                return lst[i]

print(first_recur([2,3,4,5,6,7,8,2,2,4,4,1]))   # O(n) = n^2


# Dictionary method - hash table
def first_rec_dict(lst):
    count_lst = {}  # Empty dictionary
    for num in lst:     # iterating each number in list 
        if num in count_lst: # if no. in dictionary already
            return num
        else:               # if no. not in dictionary, assign value 1 to it
            count_lst[num] = 1
print(first_rec_dict([2,3,4,5,6,7,8,2,2,4,4,1]))   # O(n) = n^2
