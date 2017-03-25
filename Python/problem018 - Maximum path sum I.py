#
# Created by 14chanwa on 2017.03.18
#

# Project Euler - Problem 18
# Maximum path sum I

f = open('p018_triangle.txt', 'r')

# Parse file and create a list of lists (each list depicts a row in the triangle)
triangle = f.read()
triangle_list = list(map(str, triangle.split("\n")))
triangle_array = []
for i in range(0, len(triangle_list)):
    t = list(map(int, [s for s in list(map(str, triangle_list[i].split(" "))) if s != '']))
    if len(t) > 0:
        triangle_array.append(t)

# For each row beginning from the base of the pyramid, set the weight to the max of
# the 2 roads below. Each weight is the max weight of the roads taken from the base
# to the top of the triangle.
for i in range(len(triangle_array) - 1, 0, -1):
    # Set the elements in the preceding line
    for j in range(0, len(triangle_array[i - 1])):
        triangle_array[i - 1][j] += max(triangle_array[i][j], triangle_array[i][j + 1])

print(triangle_array[0])
