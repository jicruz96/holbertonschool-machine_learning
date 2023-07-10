#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

np.random.seed(5)
people = ["Farrah", "Fred", "Felicia"]
fruit = np.random.randint(0, 20, (4, 3))
fruit_colors = (
    ("apples", "red"),
    ("bananas", "yellow"),
    ("oranges", "#ff8000"),
    ("peaches", "#ffe5b4"),
)
plt.yticks(np.arange(0, 81, 10))
plt.ylim(0, 80)
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
# create one stacked bar for each person
for i, person in enumerate(people):
    # create a bar for each kind of fruit
    persons_fruit = fruit[:, i]
    bottom = 0
    for j, (fruit_name, color) in enumerate(fruit_colors):
        fruit_count = persons_fruit[j]
        # stack the bars
        plt.bar(
            x=person,
            height=fruit_count,
            width=0.5,
            bottom=bottom,
            color=color,
        )
        bottom += fruit_count
fruit_artists = [
    Rectangle((0, 0), 1, 1, fc=color) for fruit_name, color in fruit_colors
]
plt.legend(
    loc="upper right",
    labels=[fruit_name for fruit_name, color in fruit_colors],
    handles=fruit_artists,
)
plt.show()
