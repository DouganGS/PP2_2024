from movies import movies
from statistics import mean
def average_of_categories(movies):
    choiceofcat = input("Category that you want\n")
    categories = [x["imdb"] for x in movies if choiceofcat == x["category"]]
    return mean(categories)

print(average_of_categories(movies))