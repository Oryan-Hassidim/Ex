##############################################################################
# FILE: cartoonify.py
# WRITER: Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE: Intro2cs2 ex6 2021-2022
# DESCRIPTION: A simple program for cartoonifying a given image.
# NOTES: In many functions I
##############################################################################

from ex6_helper import *
from typing import Optional
from math import floor, ceil
from sys import argv
from multiprocessing.pool import ThreadPool as Pool
from itertools import product


def simple_map(args):
    f, l = args
    return list(map(f, l))


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def map2D(f, l=None, multiProcess=False):  # enable carryng the function
    """
    map for 2D lists.
    """

    def inner(l):
        # 43437
        if multiProcess:
            with Pool(4) as p:
                args = [(f, x) for x in l]
                res = list(p.map(simple_map, args))
                p.close()
                p.join()
                return res
        return list(map(lambda x: list(map(f, x)), l))

    return inner(l) if l != None else inner


def sum2D(l):
    """
    sum for 2D list.
    """
    return sum(map(sum, l))


def separate_channels(image: ColoredImage) -> List[List[List[int]]]:
    """
    Seperates the given colored image to channels.
    """
    if len(image) == 0 or len(image[0]) == 0:
        return image
    depth = len(image[0][0])
    channels = [
        map2D(lambda pix: pix[channel], image, True) for channel in range(depth)
    ]
    return channels


def combine_channels(channels: List[List[List[int]]]) -> ColoredImage:
    """
    Combines the given channels to one colored image.
    """
    if len(channels) == 0 or len(channels[0]) == 0 or len(channels[0][0]) == 0:
        return channels
    depth = len(channels)
    res = map2D(lambda x: [x], channels[0])
    for channel in range(1, depth):
        for row in range(len(channels[channel])):
            for col in range(len(channels[channel][row])):
                res[row][col].append(channels[channel][row][col])
    return res


def RGB2grayscale_pixel(pix):
    """
    Converts colored pixel of RGB channels to integer of grayscle value.
    """
    return round(pix[0] * 0.299 + pix[1] * 0.587 + pix[2] * 0.114)


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    Converts colored image of RGB channels to grayscle image.
    """
    res = map2D(RGB2grayscale_pixel, colored_image, True)
    return res


def blur_kernel(size: int) -> Kernel:
    """
    Takes size as parameter and returns Kernel of the given sizes squered,
    with equal weight for each cell.
    """
    return [[1 / (size * size)] * size] * size


def get_value_or_default(image: SingleChannelImage):
    height = len(image)
    width = len(image[0])

    def inner(row, col, default):
        nonlocal height
        nonlocal width
        if 0 <= row < height and 0 <= col < width:
            return image[row][col]
        return default

    return inner


def apply_kernel_core(image: SingleChannelImage, kernel: Kernel):
    get_val = get_value_or_default(image)
    size = len(kernel)
    size -= 1
    size //= 2
    kerneler = []
    for i, row in enumerate(kernel):
        for j, pix in enumerate(row):
            kerneler.append((i - size, j - size, pix))

    def inner(row, col):
        nonlocal get_val
        nonlocal kerneler
        my_sum = 0
        default = image[row][col]
        for di, dj, pix in kerneler:
            val = get_val(row + di, col + dj, default)
            my_sum += pix * val
        return max(0, min(255, round(my_sum)))

    return inner


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    Applies the given kernel for the given image.
    Edges takes the value of *calculated cell*.
    """
    core = apply_kernel_core(image, kernel)
    indexes = product(range(len(image)), range(len(image[0])))
    with Pool(4) as p:
        res = p.map(lambda ij: core(ij[0], ij[1]), indexes)
        p.close()
        p.join()

    # res = []
    # for row in range(len(image)):
    #    new_row = []
    #    for pix in range(len(image[row])):
    #        new_row.append(core(row, pix))
    #    res.append(new_row)
    return list(chunks(res, len(image[0])))


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """
    Takes an image and x and y coordinates and returns the color scale of this point
    relativly to the image.
    """
    dx = x % 1
    dy = y % 1
    res = (
        image[floor(y)][floor(x)] * (1 - dy) * (1 - dx)
        + image[ceil(y)][floor(x)] * dy * (1 - dx)
        + image[floor(y)][ceil(x)] * (1 - dy) * dx
        + image[ceil(y)][ceil(x)] * dy * dx
    )
    return round(res)


def resize(
    image: SingleChannelImage, new_height: int, new_width: int
) -> SingleChannelImage:
    """
    Takes an image and destinition height and width,
    and returns a new image with the new size.
    """
    height_prop = (len(image) - 1) / (new_height - 1)
    width_prop = (len(image[0]) - 1) / (new_width - 1)
    new_image = [
        [(i * height_prop, j * width_prop) for j in range(new_width)]
        for i in range(new_height)
    ]
    new_image = map2D(
        lambda yx: bilinear_interpolation(image, yx[0], yx[1]), new_image, True
    )

    new_image[0][0] = image[0][0]
    new_image[0][-1] = image[0][-1]
    new_image[-1][0] = image[-1][0]
    new_image[-1][-1] = image[-1][-1]

    return new_image


def scale_down_colored_image(
    image: ColoredImage, max_size: int
) -> Optional[ColoredImage]:
    """
    Scales tge given image to to max-size.
    If the given image is smaller than max-size, returns None.
    Else, returns the scaled image.
    """
    height = len(image)
    width = len(image[0])
    if height <= max_size and width <= max_size:
        return None

    if len(image) >= len(image[0]):
        new_height = max_size
        new_width = int(ceil(width * max_size / height))
    else:
        new_height = int(ceil(height * max_size / width))
        new_width = max_size

    channels = separate_channels(image)
    channels = [resize(channel, new_height, new_width) for channel in channels]
    return combine_channels(channels)


def rotate_90(image: Image, direction: str) -> Image:
    im = image if direction == "L" else image[::-1]
    transposed = list(map(list, zip(*im)))
    return transposed[::-1] if direction == "L" else transposed


def get_edges(
    image: SingleChannelImage, blur_size: int, block_size: int, c: int
) -> SingleChannelImage:
    blurred = apply_kernel(image, blur_kernel(blur_size))
    avgs = apply_kernel(blurred, blur_kernel(block_size))
    threshhold = map2D(lambda pix: pix - c, avgs, True)
    indexes = product(range(len(image)), range(len(image[0])))
    with Pool(4) as p:
        res = p.map(
            lambda ij: 255 if blurred[ij[0]][ij[1]] > threshhold[ij[0]][ij[1]] else 0,
            indexes,
        )
        p.close()
        p.join()
    return list(chunks(res, len(image[0])))
    # for i in range(len(image)):
    #    for j in range(len(image[i])):
    #        if blurred[i][j] > threshhold[i][j]:
    #            avgs[i][j] = 255
    #        else:
    #            avgs[i][j] = 0
    # return avgs


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    return map2D(lambda pix: round(floor(pix * N / 256) * 255 / (N - 1)), image, True)


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    channels = separate_channels(image)
    with Pool(4) as p:
        channels = p.map(lambda c: quantize(c, N), channels)
    # [quantize(channel, N) for channel in channels]
    return combine_channels(channels)
    # where are F# pipes???


def add_mask_core(
    image1: SingleChannelImage, image2: SingleChannelImage, mask: List[List[float]]
) -> Image:
    res = []
    for i in range(len(image1)):
        new_row = []
        for j in range(len(image1[0])):
            new_row.append(
                round(image1[i][j] * mask[i][j] + image2[i][j] * (1 - mask[i][j]))
            )
        res.append(new_row)
    return res


def is_colored_image(image: Image):
    return isinstance(image[0][0], int)


def add_mask(image1: Image, image2: Image, mask: List[List[float]]) -> Image:
    singles = is_colored_image(image1), is_colored_image(image2)
    if singles == (True, True):
        return add_mask_core(image1, image2, mask)

    with Pool(4) as p:
        if singles == (False, True):
            channels = separate_channels(image1)
            channels = p.map(lambda c: add_mask_core(c, image2, mask), channels)
            #channels = [add_mask_core(c, image2, mask) for c in channels]
        elif singles == (True, False):
            channels = separate_channels(image2)
            channels = p.map(lambda c: add_mask_core(image1, c, mask), channels)
            #channels = [add_mask_core(image1, c, mask) for c in channels]
        else:
            channels1, channels2 = separate_channels(image1), separate_channels(image2)
            channels = p.map(
                lambda i: add_mask_core(channels1[i], channels2[i], mask),
                range(len(channels1))
            )
        p.close()

    #channels = []
    #for i in range(len(channels1)):
    #    channels.append(add_mask_core(channels1[i], channels2[i], mask))
    return combine_channels(channels)

def cartoonify(
    image: ColoredImage,
    blur_size: int,
    th_block_size: int,
    th_c: int,
    quant_num_shades: int,
) -> ColoredImage:
    gray = RGB2grayscale(image)
    edges = get_edges(gray, blur_size, th_block_size, th_c)
    quantized = quantize_colored_image(image, quant_num_shades)
    mask = map2D(lambda pix: pix / 255, edges, True)
    cartoonified = add_mask(quantized, edges, mask)
    return cartoonified


def main(args):
    if len(args) != 7:
        print(
            "Sorry, we can't apply this operation. "
            + "This application takes 7 arguments:)"
        )
        return
    im_source, cartoon_dest = args[:2]

    max_size, blur_size, block_size, th_c, quant_shades = map(int, args[2:])

    im = load_image(im_source)
    scaled = scale_down_colored_image(im, max_size)
    scaled = im if scaled is None else scaled

    cartoonified = cartoonify(scaled, blur_size, block_size, th_c, quant_shades)

    save_image(cartoonified, cartoon_dest)


from time import process_time_ns

if __name__ == "__main__":
    start = process_time_ns()
    main(argv[1:])
    print((process_time_ns() - start) / 100000)
