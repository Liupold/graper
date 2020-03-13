import io
import re

def get_key(element: str, key: str):
    if f'.{key.upper()}' in element:
        return " ".join(element.split(' ')[1:])
    return None

def graper_reader(filename):
    """
    return a structured dict with all
    the needed information
    """
    # default dict
    data_dict = {'name': 'Untitled', 'scale_x': 'auto', 'scale_y': 'auto'}
    done = []
    with open(filename) as f:
        data = f.read().strip()
        # ignore comments
        data = re.sub(r'(?m)^ *#.*\n?', '', data)

    # settings
    for line in data.split('\n'):
        line = line.strip()
        for item in data_dict.items():
            if item[0] in done:
                continue
            value = get_key(line, item[0])
            if value is not None:
                data_dict[item[0]] = value
                done.append(item[0])
    # plot
    plots = []
    for parts in data.split('.DATA'):
        if '.END_DATA' in parts:
            plots.append(parts.replace('.END_DATA', ''))

    plots = [tuple(filter(None ,i.split('\n'))) for i in plots]
    plots=  [[tuple(float(i) for i in data.split()) for \
            data in plot] for plot in plots]

    data_dict['plots'] = plots

    return data_dict


if __name__ == "__main__":
    print("Don't run this -_-")
