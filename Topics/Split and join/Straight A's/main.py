# put your python code here
# grade_in = "F B A A B C A D".split(" ")
grade_in = input().split(" ")
print(round(grade_in.count("A") / len(grade_in), 2))
