# val_in = "1 22 3".split()
val_in = input().split()
# print(*val_in[::-1])  # also works here
val_in.reverse()
print(" ".join(val_in))