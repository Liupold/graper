def get_range(data_x, data_y, e_fraction=0.1):

    max_fraction_x = 1 + e_fraction
    min_fraction_x = 1 - e_fraction
    max_fraction_y = 1 + e_fraction
    min_fraction_y = 1 - e_fraction

    x_max, x_min = max(data_x), min(data_x)
    y_max, y_min = max(data_y), min(data_y)

    # calculate ranges
    x_range = (x_max * max_fraction_x if x_max > 0 else x_max * min_fraction_x), \
            (x_min * min_fraction_x if x_min > 0 else x_min * max_fraction_x)
    y_range = (y_max * max_fraction_y if y_max > 0 else y_max * min_fraction_y),\
            (y_min * min_fraction_y if y_min > 0 else y_min * max_fraction_y)
    return x_range, y_range


def auto_scale(x_range, y_range, divs):
    scale_x = (x_range[0] - x_range[1]) / divs[0]
    scale_y = (y_range[0] - y_range[1]) / divs[1]
    return (scale_x, scale_y)


def transform(data_x, data_y, scale, origin):
    """
    This transforms values to graph paper coordinate.
    data_x: values along X axis
    data_y: values along Y axis
    """
    x_out, y_out = [], []
    for x, y in zip(data_x, data_y):
        x_ = round((x - origin[0]) / scale[0])
        y_ = round((y - origin[1]) / scale[1])
        x_out.append(x_); y_out.append(y_)

    return x_out, y_out
