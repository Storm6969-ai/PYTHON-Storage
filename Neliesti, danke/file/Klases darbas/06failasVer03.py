def viskas(a, b):
    with open('06dataVer03.txt', 'a+', encoding='utf-8') as f: # 
        f.write(str(a)+'\n')
        f.write(str(b)+'\n')
        f.seek(0) # keliaujam i failo pradzia
        x1 = int(f.readline())
        x2 = int(f.readline())  
        suma = x1 + x2
        f.write(f'{x1} + {x2} = {suma}\n')      


viskas(14, 17)