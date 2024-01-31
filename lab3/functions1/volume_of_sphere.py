def volumesphere(radius):
    volume = (4/3) * 3.14 * radius**3
    return volume
    

radius = int(input())

print(volumesphere(radius))