from PIL import Image, ImageDraw
import os

class GraphPaper():
    """
    Works only with symmetric margins.
    """
    def __init__(self, filepath, margins: tuple, \
            cell_width: tuple, limits: tuple):

        self.im = Image.open(filepath)
        self.margins = margins
        self.cell_width = cell_width
        self.limits = limits
        self.point_size = 5
        self.color = 'red'

    def save(self, filepath, format_='PNG'):
        self.im.save(filepath, format_)

    def __raw_draw_point(self, x, y, color=None):
        draw = ImageDraw.Draw(self.im)
        if color is not None:
            # change color
            self.color, color = color, self.color
        draw.ellipse((x - self.point_size, y - self.point_size, \
                x + self.point_size, y + self.point_size), \
                fill=self.color, outline=self.color)
        if color is not None:
            # reset color
            self.color = color

    def plot_single(self, x, y, color=None):

        if x < 0 or y < 0:
            raise ValueError("x, y cannot be less than Zero.")
        if x > self.limits[0] or y > self.limits[1] :
            raise ValueError("value x, y is greater than lim ({})".\
                    format(self.limits))

        raw_x = self.margins[0] + (x * self.cell_width[0])
        raw_y = self.im.size[1] - self.margins[1] - (y * self.cell_width[1])
        self.__raw_draw_point(raw_x, raw_y, color)

    def plot(self, x_array, y_array, color=None):
        for x, y in zip(x_array, y_array):
            self.plot_single(x, y, color)

    def show(self):
        self.im.show()


# Profiles

#mm
graph_file_mm = os.path.join(os.path.dirname(__file__),\
        'GraphPapers/Graph_paper_mm_green_A4.png')
GRAPH_MM = (graph_file_mm, (95, 80), (9.53, 9.53), (190, 280))

GraphPapersDict = {'mm': GRAPH_MM}
