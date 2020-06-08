from PIL import Image, ImageDraw

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
        self.point_color = 'red'

    def save(self, filepath, format_='PNG'):
        self.im.save(filepath, format_)

    def __raw_draw_point(self, x, y, color=None):
        draw = ImageDraw.Draw(self.im)
        if color is not None:
            # change color
            self.color, color = color, self.color
        draw.ellipse((x - self.point_size, y - self.point_size, \
                x + self.point_size, y + self.point_size), \
                fill=self.point_color, outline=self.point_color)
        if color is not None:
            # reset color
            self.color = color

    def plot(self, x, y, color=None):

        if x < 0 or y < 0:
            raise ValueError("x, y cannot be less than Zero.")
        if x > self.limits[0] or y > self.limits[1] :
            raise ValueError("value x, y is greater than lim ({})".\
                    format(limits))

        raw_x = self.margins[0] + (x * self.cell_width[0])
        raw_y = self.im.size[1] - self.margins[1] - (y * self.cell_width[1])
        self.__raw_draw_point(raw_x, raw_y)

    def show(self):
        self.im.show()


# Profiles
graph_file_mm = 'GraphPapers/Graph_paper_mm_green_A4.png'
GRAPH_MM = (graph_file_mm, (95, 80), (9.53, 9.53), (190, 280))
