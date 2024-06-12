def square_meters_to_square_kilometers(square_meters):
    return square_meters / 1_000_000

square_meters = 1000000
print(f"{square_meters} square meters is {square_meters_to_square_kilometers(square_meters)} square kilometers")