S = input()
arr = []

for idx in range(len(S)):
    arr.append(S[idx:len(S)])
    
# print(arr)

arr = sorted(arr)
print(*arr, sep="\n")
