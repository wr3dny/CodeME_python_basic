hobbits=['Frodo', 'Bilbo', 'Sam']
grades =[2,3,4]
print(hobbits + grades)
print(hobbits[1])

print(grades.append('Sam'))
print(grades.insert(1,'Bilbo'))
elem = grades.pop(1)
print(elem)
grades.remove('Sam')
del hobbits [1]
print(hobbits)

list(range(10))