from lib import imagepack
from testdata import Testdata


def test_circle_size_changes(create_images):
    sizes = [imagepack.get_circle_size(i) for i in Testdata.image_paths]
    all_values = len(sizes)
    if all_values == len(Testdata.image_paths):
        assert all_values == len(set(sizes)), 'Sizes are not matching one or two circle sizes have not changes'
    print('Test Passed')
