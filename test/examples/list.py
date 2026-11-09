names = ['James', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'

print(names)

print(names[0])

print(names[:])

print(names[:4])

print(names[2:4])

print(names[2:-2])

print(names[-2])

# list methods

numbers = [5, 2, 5, 1, 7, 4]
numbers.sort()
numbers.reverse()

numbers2 = numbers.copy()

numbers.append(22)

print(numbers)
print(numbers2)

# numbers.insert(0, 10)
# numbers.remove(5)

# print(numbers.index(5))
# print(22 in numbers)

# print(numbers.count(5))

# numbers.clear()