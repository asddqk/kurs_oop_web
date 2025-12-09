a,b,c=map(int, input().split())
B=max(a,b)*c
A=min(a,b)
while B-A>1:
    M=(B+A)//2
    m=(M//a)*(M//b)
    if m< c:
        A=M
    else:
        B=M
print(B)