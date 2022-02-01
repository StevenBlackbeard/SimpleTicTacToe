# n = "12345"
n = input()
n = [int(x) for x in n]
x = [(n[x] + n[x + 1]) / 2 for x in range(len(n) - 1)]
print(x)

# n = input()
# n = [int(x) for x in n]
# x = []
# for i in range(len(n)-1):
#     x.append((n[i] + n[i+1]) / 2)
# print(x)