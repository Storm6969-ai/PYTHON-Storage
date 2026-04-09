skar = [5, 2, 7, 2, 2, 10, 9]

kiek = len(skar)
for i in range(len(skar)):
    print(skar[i])
print()

for paz in skar:
    if paz == 2:
        paz = 10
    print(paz)
print(skar)
print() # tik paema tam tikrus elemntus

for i in range(len(skar)):
    if skar[i] == 2:
        skar[i] = 10
print(skar) # pakeicia tam tikrus elemntus

did = skar[0]
for i in range(1, len(skar)):  # pradeda nuo 2o elemnto tai netikrina pirmo nes pirmas jau priskirtas
    if skar[i] > did:
        did = skar[i]