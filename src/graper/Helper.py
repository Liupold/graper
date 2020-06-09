import os
import random
from . import Reader
from . import Calc
from . import GraphPapers

def get_data(filename):
    rel_dir = os.path.dirname(filename)
    yaml_data = Reader.get_yaml(filename)
    info = yaml_data['info']
    plots = Reader.parse_plots(yaml_data['plots'], rel_dir)
    graphs = Reader.parse_graphs(yaml_data['graphs'], plots)
    return info, plots, graphs

def color_palate(graph):
    color = graph['color'] if 'color' in graph else None
    def get_color(i):
        if color is None:
             return "#"+''.join([random.choice('0123456789ABCDEF') \
                    for j in range(6)])
        else:
            if ',' not in color:
                return color
            else:
                return color.replace(' ', '').split(',')[i]
    return get_color

def get_scale_origin(graph, plots, divs):
    points_x = []; points_y = []
    for plot in graph['plots']:
        for x,y in zip(*plots[plot]):
            points_x.append(x)
            points_y.append(y)

    if ('scale' not in graph) or ('origin' not in graph):
        range_ = Calc.get_range(points_x, points_y)

    if 'scale' in graph:
        scale = [float(i) for i in graph['scale'].split(',')]
    else:
        scale = Calc.auto_scale(*range_, divs)

    if 'origin' in graph:
        origin = [float(i) for i in graph['origin'].split(',')]
    else:
        origin = range_[0][1], range_[1][1]

    return scale, origin

def get_graph_paper(graph):
    if graph['type'] not in GraphPapers.GraphPapersDict:
        raise NotImplementedError("type: `{}` not understood"\
                .format(graph['type']))
    gp = GraphPapers.GraphPaper(\
            *GraphPapers.GraphPapersDict[graph['type']])
    return gp

def get_padding(graph):

    padding_left = float(graph['padding_left']) if 'padding_left' in graph else 10
    padding_right = float(graph['padding_right']) if 'padding_right' in graph else 0
    padding_top = float(graph['padding_top']) if 'padding_top' in graph else 0
    padding_bottom = float(graph['padding_bottom']) if 'padding_bottom' in graph else 10

    print(padding_bottom)
    return (padding_left, padding_right, \
            padding_top, padding_bottom)

def padding_limits(limits, left, right, top, bottom):
    limits = list(limits)
    limits[0] = limits[0] - left - right
    limits[1] = limits[1] - top - bottom
    return tuple(limits)

