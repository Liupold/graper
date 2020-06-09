#!/usr/bin/python
import click

from . import Calc
from . import Helper

@click.command()
@click.option('--draw/--no-draw', default=True, \
        help='make graphs [default: True]')
@click.option('--simulate/--no-simulate', default=False , \
        help='Dry dun only (Verify yaml) [default: False]')
@click.argument('filename', required=True, type=click.Path(exists=True))
def main(draw, simulate, filename):

    info, plots, graphs = Helper.get_data(filename)

    if simulate:
        exit()

    for graph_label, graph in graphs.items():
        print("Graphing: {}".format(graph_label))

        padding = Helper.get_padding(graph)

        gp = Helper.get_graph_paper(graph)
        get_color = Helper.color_palate(graph)
        divs = Helper.padding_limits(gp.limits, *padding)
        scale, origin = Helper.get_scale_origin(graph, plots, divs)

        for i, plot in enumerate(graph['plots']):
            gp_coord = Calc.transform(*plots[plot], scale, origin, padding)
            gp.plot(*gp_coord, get_color(i))

        if draw:
            gp.save(graph['save'])

main()
