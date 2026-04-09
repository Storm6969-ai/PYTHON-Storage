import random

vaisiai = ["obuolys", "persimonas", "persikas", "apelsinas", "bananas"]
# kaValgom = random.choice(vaisiai) ## 'choise' - is ko rinktis
# kaValgom = random.choices(vaisiai, k=3) ## 'choiseS' - is ko rinktis, kelis dalykus (reikia nurodyti 'k =' koks kiekis)
kaValgomUnik3 = random.sample(vaisiai, 3) ## 'choiseS' - is ko rinktis, kelis dalykus

print(kaValgomUnik3)