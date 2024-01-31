from movies import movies
from statistics import mean

def average_of_all(movies):
    movies_rates = [x["imdb"] for x in movies]
    return mean(movies_rates)

print(round(average_of_all(movies),2))