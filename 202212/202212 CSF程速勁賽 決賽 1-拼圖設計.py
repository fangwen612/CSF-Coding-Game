input_list = input().split(' ')
input_list = [int(x) for x in input_list]

height = input_list[0]
width = input_list[1]
min_height = input_list[2]
min_width = input_list[3]

row_n = int(height/min_height)
col_n = int(width/min_width)

puzzle_height = height / row_n
puzzle_width = width / col_n

print(round(puzzle_height, 3), round(puzzle_width, 3))
