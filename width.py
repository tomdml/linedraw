import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from itertools import cycle


def draw_image(filepath, out_rows=50, out_points=1000, color=['black'], bgcolor='white', contrast=3):
    """
    Create the point drawing.
    Args:
        filepath    (str):      Path to the image.
    KWargs:
        out_rows    (int):      Number of rows in output image. Suggested 30-70.
        out_points  (int):      Number of dots in output image.
                                Suggested 1000 for smooth lines, or equal to out_rows for cool dots.
        color       (list -> pyplot.color):
                                Cycle of pyplot.colors for each line.
        bgcolor     (pyplot.color):
                                Background colour of the plot.
        contrast    (int):      Flatten blacks and increase whites separation. Suggested 3.
    """
    # Convert mode 'L': ITU-R 601-2 luma transform (L = R * 299/1000 + G * 587/1000 + B * 114/1000)
    im = Image.open(filepath).convert('L')
    imwidth, imheight = im.size
    im = im.resize((out_points, out_rows))

    # Normalize values inside array: (0, 255) -> (1, 0)
    im = 1 - (np.asarray(im) / 255)

    # Increase contrast by squashing black pixels and increasing white ones
    im = im**contrast

    # Emulate a line drawing with many plt.scatter points
    x = np.linspace(0, out_points, out_points)
    for (offset, row), col in zip(enumerate(im), cycle(color)):
        yOffset = np.full(out_points, 10 * offset)
        sin1 = np.sin(x / np.random.randint(20, 50))
        sin2 = np.sin(x/np.random.randint(50, 70))

        plt.scatter(
            x,
            yOffset + sin1 * sin2,
            s=3 * row,
            color=col
        )

    ax = plt.gca()
    ax.set_axis_off()
    ax.invert_yaxis()

    fig = plt.gcf()
    fig.set_facecolor(bgcolor)
    fig.set_size_inches(10, 10*(imheight / imwidth))

    plt.show()


if __name__ == '__main__':
    draw_image('typ.jpg')
