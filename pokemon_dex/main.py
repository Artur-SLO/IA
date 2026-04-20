from src.pokemon import random_pokemon
from wordcloud import WordCloud
import matplotlib.pyplot as plt

TOTAL = 30
types_list = []
pokemon_list = []

for _ in range(TOTAL):
    pokemon = random_pokemon()
    if pokemon:
        pokemon_list.append(pokemon)
        types_list.extend(pokemon["types"])

text = " ".join(types_list)
print(text)

for pokemon in pokemon_list:
    print(f"{pokemon['name'].title()}: {', '.join(t.title() for t in pokemon['types'])}")

wc = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
