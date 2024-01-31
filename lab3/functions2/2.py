from movies import movies

def sublist(movies):
    subl = [movie for movie in movies if movie["imdb"]>= 5.5]
    return subl

print(sublist(movies))