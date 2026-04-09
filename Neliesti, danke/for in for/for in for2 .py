# for i in range(5):
#     for j in range(i+1): # 'i+1' - reikia, nes pirmam j cikle i = 0
#         print(i, end=' ')
#     print()

n = 5
for i in range(n):
    for j in range(n-i): # 'n-i' - 'n' vis mazeja, nes atimamas vis didesnis 'i' 
        print("*", end=' ')
    print()