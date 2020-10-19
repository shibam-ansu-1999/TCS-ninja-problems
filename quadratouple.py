n = int(input("Enter count of values you are going to insert"))
A = []
res = []
print("Enter",n,"numbers")
for i in range(n):
    A.append(int(input()))

for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                res.append(A[i]*A[j]*A[k]*A[l])
if n <= 3:
    print("Invalid Input")
            
else:
    print(float(max(res)))
            
    
