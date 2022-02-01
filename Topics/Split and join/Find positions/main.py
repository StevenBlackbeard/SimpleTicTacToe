# put your python code here
# first = "5 8 2 7 8 8 2 4".split(" ")
# second = "8"
# second = "10"
first = input().split(" ")
second = input()
if first.count(second) == 0:
    print("not found")
else:
    output = [str(i) for i in range(len(first)) if first[i] == second]
    print(" ".join(output))