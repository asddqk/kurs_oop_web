X=int(input())
T= list(input().split())
T.append(T[0])
T.append(T[1])
Max=0
for i in range(X):
    if Max< int(T[i]) + int(T[i+1]) + int(T[i+2]):
        Max= int(T[i]) + int(T[i+1]) + int(T[i+2])
print(Max)