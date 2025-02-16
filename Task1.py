f = open("27-168b.txt")
n, k = map(int, f.readline().split())
a = [int(x) for x in f]
first = 0
second = 0
third = 0
for i in range(2 * k, n):
    first = max(first, a[i - 2 * k])
    second = max(second, first * a[i - k])
    third = max(third, second * a[i])
print(third)

