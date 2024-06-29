immutable_var = (1, 2, 3, 'string', True)
print(immutable_var)

# immutable_var[0] = 10
# print(immutable_var)
# Значения элементов кортежа нельзя изменить, потому что они не изменяемые)))

mutable_list = [1, 2, 3, 'string', True]
mutable_list[0], mutable_list[3], mutable_list[4] = 0, 'line', False
mutable_list.remove(2)
mutable_list.append(2)
print(mutable_list)