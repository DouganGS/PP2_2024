def solve(numheads, numlegs):
    chickens = int((numlegs - 4*numheads)/ -2)
    rabbits = int(numheads - chickens)
    return f"Chickens: {chickens}, Rabbits: {rabbits}."
    

head = 35
legs = 94

print(solve(head,legs))
# 2*x + 4*y= legs