import random
from movies import movies

def singlemovie():
    a = random.choice(movies)
    
    if a["imdb"] >= 5.5:
        print(f"True\nName of movie: {a['name']}\nImdb rate: {a['imdb']}")
        
    else:
        print(f"False\nName of movie: {a['name']}\nImdb rate: {a['imdb']}")


singlemovie()
