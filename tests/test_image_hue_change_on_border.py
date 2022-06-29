from lib import imagepack
from testdata import Testdata
import matplotlib.pyplot as plt
    
def test_image_hue_change_on_border():
    print(imagepack.get_pixel_color(Testdata.image_paths[0]))
    print(imagepack.get_pixel_color(Testdata.image_paths[2]))
    assert imagepack.get_pixel_color(Testdata.image_paths[0]) !=  imagepack.get_pixel_color(Testdata.image_paths[2]), \
        'Image border hue value has not changed'
    print('Test Passed')