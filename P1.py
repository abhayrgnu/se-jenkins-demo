flag = 0
while flag != 3:
    a = [int(a) for a in input().split(" ")]
    b = [int(b) for b in input().split(" ")]
    for i in range(len(a)):
        if a[i] <= 100 and a[i] >= 1 and b[i] <= 100 and b[i] >= 1:
            flag = flag + 1
            break
    if flag != 3:
        print("Re-enter scores in range of 1 to 100")
scoreOfA = 0
scoreOfB = 0
for i in range(len(a)):
    if a[i] > b[i]:
        scoreOfA = scoreOfA + 1
        # print("incrementing score of a")
    elif b[i] > a[i]:
        scoreOfB = scoreOfB + 1
        # print("incrementing score of b")
print(f"{scoreOfA} {scoreOfB}")
# if scoreOfA > scoreOfB:
#     print(f"Winner is Chef A with score of {scoreOfA}")
# else:
#     print(f"Winner is Chef B with score of {scoreOfB}")
