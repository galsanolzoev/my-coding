class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    def ins_data(self, value):
        if value < self.value:
            if self.left is None: # - what if !=
                self.left = BSTNode(value)
            else:
                self.left.ins_data(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.ins_data(value)

    def search_data(self,target):
        if self.value == target:
            return True

        if target < self.value and self.left:
            return self.left.search_data(target)

        if target > self.value and self.right:
            return self.right.search_data(target)

        return False

bst = BSTNode(260)
with open('random_numbers_large.txt', 'r') as f:
    nums = list(map(int, f.read().split()))

for num in nums:
    bst.ins_data(num)
print("Несортированный txt файл\n")

print(bst.left.right) # -1058
print(bst.right.right.right.right.right) # 9965 - наибольшее число
print(bst.search_data(10001)) # вне диапазона - False
print(bst.search_data(2)) # в диапазоне, но не попал в список - False
print(bst.search_data(-1)) # в списке - True

print("\nСортированный txt файл\n")
with open('random_numbers_sorted.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
for num in nums:
    bst.ins_data(num)

print(bst.left.right) # -1058
print(bst.right.right.right.right.right) # 9965 - наибольшее число
print(bst.search_data(10001)) # вне диапазона - False
print(bst.search_data(2)) # в диапазоне, но не попал в список - False
print(bst.search_data(-1)) # в списке - True
# значения при операторе print одинаковы, хотя в txt файле порядок разный
