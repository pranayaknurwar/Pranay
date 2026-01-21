# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="  ")
#     print("\n")

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="  ")
#     print("\n")

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(i,end="  ")
#     print("\n")

for i in range(1,6):
    for j in range(0,5-i):
        print(" ",end="  ")
    for k in range(0,2*i-1):
        print("*",end="  ")
    print()
