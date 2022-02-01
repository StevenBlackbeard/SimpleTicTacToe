# Get user input of numbers
user_input = input()
# Transform str numbers to int numbers using list comprehension
nums = [int(x) for x in user_input]
run_total = [sum(nums[:x + 1]) for x in range(len(nums))]
print(run_total)

# input_nums = list(input())
# # input_nums = [1, 5, 3, 2, 5]
# input_list = [int(num) for num in input_nums]
# new_list = [0 for num in input_nums]
# for i in range(1, len(input_list)+1):
#     new_list[i-1] = sum(input_list[0:i])
# print(new_list)