input()
T=set(input().split())
e=set(input().split())
print(1 if len(T)==len(e) and len(T&e)==len(T) else 0)