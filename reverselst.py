def reverse_list(l):
    rev = []
    for i in range(len(l)):
        pop_item = l.pop()
        rev.append(pop_item)
    return rev

numbers=[1,2,3,6,5,4]
print(reverse_list(numbers))