#!/usr/bin/python
import click
from . import Calc
from . import Helper

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-nd', '--no-draw', is_flag=True, \
        default=False, help='Do not generate graphs.')
@click.option('-d', '--dry', is_flag=True,\
        default=False, help='Dry dun only (Verify yaml)')
@click.option('-sc', '--show-calculation', is_flag=True, \
        default=False, help='Show detail calculations.')
@click.option('-sg', '--show-graphs', is_flag=True, \
        default=False, help='Show graphs. (Milage may vary)')
@click.option('-T', '--target', type=click.Path(exists=True), \
        default='.', help='Path where to save the graphs.')
@click.argument('filename', required=True, \
        type=click.Path(exists=True))
def main(no_draw, dry, show_calculation, \
        show_graphs, target, filename):

    if dry:
        print("WARN: Running in dry mode. (No Calculations will be made)")

    info, plots, graphs = Helper.get_data(filename)

    if dry:
        print("Dry run complete!.")
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

        if not no_draw:
            gp.save(graph['save'])

main(prog_name='grapher')
