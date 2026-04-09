# mama pradejo gamnti pietu hpr valandu ir pr minuciu
# pietyus gamino h.t valandu ir min.t minuciu
#kada baige gaminti pietus

hpr = int(input('Kuria valanda pradejo'))
minpr = int(input('Kuria minute pradejo'))
ht = int(input('Kiek valandu gamino'))
mint = int(input('Kiek minuciu gamino'))

#hpb = hpr+ht
#minpb = minpr+mint
baigeMin = hpr*60 + minpr + ht*60 + mint
valBaigimo = baigeMin//60
minpb = baigeMin % 60
print(f'Baige gaminti {valBaigimo}valandu {minpb}minuciu')