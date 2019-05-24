import colorlover
import numpy as np
import random


"""
This tool is designed to generate distinct color list for plotting
"""


def colorlover_pool(n, light=True):
    """refer https://plot.ly/ipython-notebooks/color-scales/"""
    if n <= 8:
        if n <= 3:
            n = 3
        style = 'Set2' if light else 'Set1'
        return colorlover.scales[str(n)]['qual'][style]
    if n <= 12:
        style = 'Set3' if light else 'Paired'
        return colorlover.scales[str(n)]['qual'][style]


def continuous_color_pool(n):
    from colorsys import hls_to_rgb
    color_pool = []
    for i in np.arange(60., 360., 360. / n):
        hue = i / 300.
        rand_num = np.random.random_sample()
        additive = rand_num * 10
        lightness = (50 + additive) / 100.
        saturation = (85 + additive) / 100.
        rgb = hls_to_rgb(hue, lightness, saturation)
        color_pool.append(tuple([int(x * 255) for x in rgb]))
    return colorlover.to_rgb(color_pool)


def get_random_color(pastel_factor=0.5):
    random_tuple = [random.uniform(0, 1) for _ in [1, 2, 3]]
    return np.array([(x + pastel_factor) / (1 + pastel_factor) for x in random_tuple])


def color_distance(c1, c2):
    # return np.sqrt(np.sum(np.square(c1 - c2)))
    return np.linalg.norm(c1 - c2)


def generate_new_color(existed_colors, pastel_factor=0.5, cutoff=0.1):
    max_dist = None
    best_color = None
    while True:
        for i in range(0, 255):
            color = get_random_color(pastel_factor=pastel_factor)
            # exclude some colors
            if color_distance(color, np.array([1, 1, 1])) < 0.1:
                continue
            if color_distance(color, np.array([0, 0, 0])) < 0.15:
                continue
            if not existed_colors:
                return color
            min_dist = min(np.linalg.norm(color-existed_colors, ord=2, axis=1))
            if not max_dist or min_dist > max_dist:
                max_dist = min_dist
                best_color = color
        if max_dist > cutoff:
            break
    return best_color


def get_color_pool(n, bright=0.5, continuous=False):
    """
    :param n: expected color number
    :param bright: brightness of color
    :param continuous: if to generate a continuous color list
    :return: color list, in rgb mode
    """
    random.seed(666)
    np.random.seed(666)
    if bright > 1 or bright < 0:
        raise Exception('pastel_factor should be in range [0, 1]')
    if continuous:
        return continuous_color_pool(n)
    if n < 13:
        if bright < 0.5:
            style = False
        else:
            style = True
        return colorlover_pool(n, light=style)
    color_pool = []
    if n < 20:
        cutoff = 0.2
    elif n < 50:
        cutoff = 0.15
    elif n < 100:
        cutoff = 0.9
    elif n < 200:
        cutoff = 0.02
    else:
        cutoff = 0.0001
    for i in range(0, n):
        color_pool.append(generate_new_color(color_pool, pastel_factor=bright, cutoff=cutoff))
    color_pool = [(int(x * 255), int(y * 255), int(z * 255)) for x, y, z in color_pool]
    color_pool = sorted(color_pool, key=lambda x: (x[0], x[1], x[2]))
    return colorlover.to_rgb(color_pool)

