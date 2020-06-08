def transform(data_x, data_y, divs, padding=(0.1, 0.1)):
    """
    This transforms values to graph paper coordinate.
    data_x: values along X axis
    data_y: values along Y axis
    divs: no of div on graph paper (small division)
    """
    max_fraction_x = 1 + padding[0]
    min_fraction_x = 1 - padding[0]
    max_fraction_y = 1 + padding[1]
    min_fraction_y = 1 - padding[1]

    x_max, x_min = max(data_x), min(data_x)
    y_max, y_min = max(data_y), min(data_y)

    # calculate ranges
    x_range = (x_max * max_fraction_x if x_max > 0 else x_max * min_fraction_x), \
            (x_min * min_fraction_x if x_min > 0 else x_min * max_fraction_x)
    y_range = (y_max * max_fraction_y if y_max > 0 else y_max * min_fraction_y),\
            (y_min * min_fraction_y if y_min > 0 else y_min * max_fraction_y)
    # calculate scale
    scale_x = (x_range[0] - x_range[1]) / divs[0]
    scale_y = (y_range[0] - y_range[1]) / divs[1]

    origin = x_range[1], y_range[1]

    for x, y in zip(data_x, data_y):
        x_ = (x - origin[0]) / scale_x
        y_ = (y - origin[1]) / scale_y
        yield round(x_), round(y_)

