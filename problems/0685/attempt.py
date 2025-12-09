A1,A2,A3,S1,S2,S3=map(int, input().split())
print(max(A1,A2,A3)*max(S1,S2,S3) + min(S1,S2,S3)*min(A1,A2,A3) + (A1+A2+A3 - max(A1,A2,A3) -min(A1,A2,A3))*(S1+S2+S3 - max(S1,S2,S3) -min(S1,S2,S3)))