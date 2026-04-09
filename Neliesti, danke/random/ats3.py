import random

# kortos = ['Karalius', 'Dama', 'Tuzas', 'Valetas']
# print(kortos)
# random.shuffle(kortos) ### sumaiso duomenis
# print(kortos)

kamuoliukai = list(range(1, 73))
# print(kamuoliukai)

kenoloto = random.sample(kamuoliukai, 6)
print(kenoloto)