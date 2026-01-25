# Array Implmentation
class Array:
    def __init__(self,capacity):
        self.capacity=capacity 
        self.arr = [0]*capacity
        self.length = 0
    def __str__(self):
        return str(self.arr[0:self.length])
    def __len__(self):
        return self.length
    def __getitem__(self, index):
        if index<0 or index>self.length:
            raise IndexError("Index is out of range!")
        return self.arr[index]
    def __setitem__(self, index, value):
        if index<0 or index>self.length:
            raise IndexError("Index is out of range!")
        self.arr[index] = value
    
    def resize(self):
        self.capacity *= 2
        new_arr = [0]*self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr # Copying old array to new array
    
    def append(self, value):
        if self.length == self.capacity:
            resize()
        self.arr[self.length] = value
        self.length += 1
    
    def insert(self, index, value):
        if index<0 or index>self.length:
            raise IndexError("Index is out of range")
        if self.length == self.capacity:
            resize()
        for i in range(self.length, index, -1):
            self.arr[i] = self.arr[i-1]  # Left shift
        self.arr[index] = value
        self.length += 1

    def remove(self, value):
        for i in range(self.length):
            if self.arr[i] == value:
                for j in range(i, self.length-1):
                    self.arr[j] = self.arr[j+1]  # Right Shift
                self.length -= 1
                return
        raise ValueError("Value is not found")
    def pop(self, index= None):
        if self.length == 0:
            raise IndexError("Array is empty!")
        if index is None:
            index = self.length-1
        if index < 0 or index >= self.length:
            raise IndexError("Array out of range")
        
        value = self.arr[index]
        for i in range(index, self.length-1):
            self.arr[i] = self.arr[i+1]
        self.length -=1
        return value

arr = Array(5)
print(arr)

arr.append(3)
arr.append(4)
arr.append(7)
print(arr)

arr.insert(2, 8)
print(arr)

arr.remove(7)
print(arr)
    
arr.pop()
print(arr)
arr.append(18)
print(arr)

arr.pop(1)
print(arr)
                    

        

