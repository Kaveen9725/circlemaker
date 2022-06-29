from lib import imagepack


def test_image_size(create_image):
    assert (400,400) == imagepack.get_image_size(create_image[2]), 'Image sizes are varying'
    print('Test Passed')

