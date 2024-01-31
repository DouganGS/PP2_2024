from movies import movies

def categories(movies):
    category = input('Write down the category of the film\n')
    sub = [movie for movie in movies if movie["category"] == category ]
    return sub
    

print(*categories(movies), sep=", ")