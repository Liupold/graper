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

def get_scale_origin(graph, plots, gp):
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
        scale = Calc.auto_scale(*range_, gp.limits)

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
