# Tuples are immutable array-like structures
coordinates = (5, 2)

x = coordinates[0]
y = coordinates[1]

def calculate_square_properties(side_length):
    area = side_length * side_length
    perimeter = 4 * side_length
    
    return (area, perimeter)

print(f'area: {calculate_square_properties(5)[0]}, perimeter: {calculate_square_properties(5)[1]}')