import clipboard
import numpy as np
from sys import argv
import math
import os

########### Settings #############
                                                            # defaults
extend_fraction_x = 0.1 # fraction between [0..1]                0.1
extend_fraction_y = 0.1 # fraction between [0..1]                0.1
no_of_div_x = 160 # (small divisions in graph paper (x))         160
no_of_div_y = 200 # (small divisions in graph paper (y))         200


##################################

if (len(argv) >= 2) and (argv[1] == '--clip'):
    print("Reading From clipboard")
    with open('data.dat', 'w') as f:
        f.write(clipboard.paste())
    file_name = 'data.dat'
else:
    file_name = argv[1] if len(argv) >= 2 else 'data.dat'

if not os.path.isfile(file_name): raise FileNotFoundError(file_name + 'not found')

x_array, y_array = np.loadtxt(file_name).transpose()

# calculate ranges
max_fraction_x = 1 + extend_fraction_x
min_fraction_x = 1 - extend_fraction_x
max_fraction_y = 1 + extend_fraction_y
min_fraction_y = 1 - extend_fraction_y


x_max, x_min = max(x_array), min(x_array)
y_max, y_min = max(y_array), min(y_array)

x_range = (x_max * max_fraction_x if x_max > 0 else x_max * min_fraction_x), \
        (x_min * min_fraction_x if x_min > 0 else x_min * max_fraction_x)
y_range = (y_max * max_fraction_y if y_max > 0 else y_max * min_fraction_y),\
        (y_min * min_fraction_y if y_min > 0 else y_min * max_fraction_y)


# calculate scale
scale_x = (x_range[0] - x_range[1]) / no_of_div_x
scale_y = (y_range[0] - y_range[1]) / no_of_div_y

origin = x_range[1], y_range[1]


# print basic info
print(f"Origin: { ['%.2E' % i for i  in origin]}")
print(f"Scale x: {'%.2E' % scale_x} <Units>")
print(f"Scale y: {'%.2E' % scale_y} <Units>")

print('\n')
print("X axis points \tY axis points")
for i in range(1, math.ceil(max(no_of_div_x, no_of_div_y) / 10) + 1):
    if i * 10 <= no_of_div_x:
        print("{}: {:.2E}".format(i * 10, origin[0] + (i * 10) * scale_x), end='')
    else:
        print('\t', end='')
    if i * 10 <= no_of_div_y:
        print("\t{}: {:.2E}".format(i * 10, origin[1] + (i * 10) * scale_y), end='\n')

print("\n\n##### Points #####")
for x, y in zip(x_array, y_array):
    x_ = (x - origin[0]) / scale_x
    y_ = (y - origin[1]) / scale_y
    print(f"{x, y}: [{int(round(x_))}, {int(round(y_))}]")
