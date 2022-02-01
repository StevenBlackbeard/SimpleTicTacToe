n = int(input())

matches = []
for _i in range(n):  # use underscore if not used in body of loop
    matches.append(input().split(' '))

winner = [x[0] for x in matches if x[1] == "win"]
print(winner)
print(len(winner))

# # other options - 1
# rows = int(input())
# matches = [input().split(' ') for x in range(rows)]
# winner = [x[0] for x in matches if x[1] == 'win']
# print(winner)
# print(len(winner))
#
#
# # other option - 2
# winners = [player[0] for player in [input().split(" ") for _i in range(int(input()))] if player[1] == 'win']
# print(winners)
# print(len(winners))
