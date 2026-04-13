with open('02byla.txt', 'w', encoding='utf-8') as f:
    sar = [1, 2, 3, 4]
    f.writelines(str(sar))
    # f.writelines(sar)
    f.writelines('Labas rytas')
    eil = ['Labas', 'rytas', 'suraitytas']
    f.writelines(eil)
    f.writelines(str(eil))
