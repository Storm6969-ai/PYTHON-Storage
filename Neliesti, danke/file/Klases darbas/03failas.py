with open('03data.txt', 'r', encoding='utf-8') as f:
    # viskas = f.read()
    # print(viskas)
    # print(type(viskas))
    # a = f.readline()
    # b = f.readable()
    f.seek(0) #nukeliaujam i failo pradzia
    a = f.readlines()
    print(a)