w,h=map(int,input().split())
print(sum([i for i in range(w+1)])*sum([i for i in range(h+1)]))