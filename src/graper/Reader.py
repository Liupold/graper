from yaml import load
import os
import numpy as np

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def verify_keys(yaml_data, must, optional=[]):
    yaml_keys = set(yaml_data.keys())

    # check for must keys
    for key in must:
        if key not in yaml_data:
            raise ValueError("`{}` option is missing!".format(key))
        yaml_keys.discard(key)

    # check for optional keys
    for key in yaml_keys:
        if key not in optional:
            raise ValueError("`{}` option not understood!".format(key))


def verify(yaml_data):
    if yaml_data is None:
        raise ValueError("Empty yaml file!")

    # top level
    verify_keys(yaml_data, ['info', 'plots', 'graphs'])
    # info level
    verify_keys(yaml_data['info'], ['name'], ['about'])

    # each plot level
    for plot in yaml_data['plots']:
        verify_keys(yaml_data['plots'][plot], ['datafile', 'delimiter'])

    # each graph level
    for graph in yaml_data['graphs']:
        verify_keys(yaml_data['graphs'][graph], \
                ['plots', 'type', 'save'], \
                ['scale', 'color', 'origin', \
                'padding_left', 'padding_right', 'padding_top', 'padding_bottom'])

def get_yaml(filename):
    with open(filename, 'r') as f:
        raw_yaml = f.read()
    yaml_data = load(raw_yaml, Loader=Loader)
    verify(yaml_data)
    return yaml_data


def parse_plots(yaml_plots, rel_path):
    """
    This parses the yaml_data['plots'],
    takes: yaml_plots, and rel_path (the path rel to which files are searched')
    """
    plots = {}
    for plot_label, plot in yaml_plots.items():
        with open(os.path.join(rel_path, plot['datafile']), 'r') as df:
            plot_data = np.loadtxt(df, delimiter=plot['delimiter'])

            # check if two rows / col is specified
            if 2 not in plot_data.shape:
                ValueError("{}: Must contain 2 and only 2 group (x, y)"\
                        .format(plot_label))

            if len(plot_data) != 2:
                plot_data = plot_data.transpose()

            plots[plot_label] = plot_data
    return plots


def parse_graphs(yaml_graphs, plots):
    """
    This parses the yaml_data['graphs'],
    takes: yaml_graphs ,yaml_plots
    """
    for graph_label, graph in yaml_graphs.items():
        g_plots = []
        for to_plot in graph['plots'].replace(' ', '').split(','):
            if to_plot not in plots:
                raise KeyError('`{}`: `{}` is never assigned!'.\
                        format(graph_label, to_plot))
            g_plots.append(to_plot)
        graph['plots'] = g_plots
    return yaml_graphs

