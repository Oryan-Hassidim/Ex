
from cartoonify import (
    separate_channels,
    combine_channels,
    RGB2grayscale,
    blur_kernel,
    apply_kernel,
    bilinear_interpolation,
    resize,
    rotate_90,
    get_edges,
    quantize,
    add_mask,
    cartoonify
)


def test_separate_channels():
    assert separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    assert separate_channels([[[1, 2, 3]] * 3] * 4) == [
        [[1] * 3] * 4,
        [[2] * 3] * 4,
        [[3] * 3] * 4,
    ]


def test_combine_channels():
    assert combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert (
        combine_channels([[[1] * 3] * 4, [[2] * 3] * 4, [[3] * 3] * 4])
        == [[[1, 2, 3]] * 3] * 4
    )


def test_RGB2grayscale():
    assert RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert RGB2grayscale([[[200, 0, 14], [15, 6, 50]]]) == [[61, 14]]


def test_blur_kernel():
    assert blur_kernel(3) == [
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
    ]


def test_apply_kernel():
    assert apply_kernel([[0, 128, 255]], blur_kernel(3)) == [[14, 128, 241]]
    assert apply_kernel(
        [
            [10, 20, 30, 40, 50],
            [8, 16, 24, 32, 40],
            [6, 12, 18, 24, 30],
            [4, 8, 12, 16, 20],
        ],
        blur_kernel(5),
    ) == [
        [12, 20, 26, 34, 44],
        [11, 17, 22, 27, 34],
        [10, 16, 20, 24, 29],
        [7, 11, 16, 18, 21],
    ]

    
def test_bilinear_interpolation():
    assert bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0
    assert bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160 

    
def test_resize():
    assert resize([[0, 10], [10, 0]], 2, 2) == [[0, 10], [10, 0]]
    assert resize([[0, 10], [10, 0]], 3, 3) == [[0, 5, 10], [5, 5, 5], [10, 5, 0]]
    assert resize([[0, 5, 10], [5, 5, 5], [10, 5, 0]], 2, 2) == [[0, 10], [10, 0]]
    

def test_rotate_90():
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]]
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]]
    assert rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') == [[[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]] 
    

def test_get_edges():
    assert get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]]

    
def test_quantize():
    assert quantize([[0, 50, 100], [150, 200, 250]], 8) == [[0, 36, 109], [146, 219, 255]] 
    

def test_add_mask():
    assert add_mask([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]], [[[250,250,250], [0,0,0]],[[250,250,100],[1,11,13]]],  [[0, 0.5, 1]]*2) == [[[250, 250, 250], [2, 2, 3]], [[250, 250, 100], [6, 11, 12]]]
    assert add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]) == [[200, 125, 50]] 
  

def test_cartoonify():
    assert cartoonify([[[50, 150, 250]]],3,3,20,8) == [[[36, 146, 255]]]
    
