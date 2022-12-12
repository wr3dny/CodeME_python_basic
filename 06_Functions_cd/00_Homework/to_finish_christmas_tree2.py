def print_segment(n, total_width):
    print('*')
    for size in range(1, n+1):
        print((size * " * ").center(total_width))
        for size in range(n+1, 2):
            print((size * " * ").center(total_width))
#
# def print_tree(size):
#     for i in range(3, size+1, 2):
#         print_segment(i, size)
#
print("Choose size of the Christmas tree:")
nn = int(input())
print(print_segment(nn, 4))
# print_tree(n)


n = int(input())
print(('*').center(n + 4))
for size in range(1, n+1):
    print('/','|','\\')
    print('/', ''*n, '|', ''*n, '\\')
    print('/', '_'*n, '|', '_'*n, '\\')
    print('/','|','\\')
    print('/', ''*(n), '|', ''*(n), '\\')
    print('/', '_'*(n), '|', '_'*(n), '\\')
print(('|').center(n + 4))