import pytest
from lib import imagepack
from testdata import Testdata

def test_image_negative_circle(create_image_neg):
    assert imagepack.check_if_circle_present(Testdata.negative_circle_path), 'Image does not have circle in it'
    print('Test Passed')

def test_image_positive_circle(create_image):
    assert imagepack.check_if_circle_present(Testdata.image_paths[0]), 'Image does not have circle in it'
    print('Test Passed')