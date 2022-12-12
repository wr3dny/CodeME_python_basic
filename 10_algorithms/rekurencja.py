
def sum_natural_recuration(n):
    if n == 1:
        return 1
    return n + sum_natural_recuration(n - 1)

print(sum_natural_recuration(10))

