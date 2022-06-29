import pytest
from testdata import Testdata
from lib import imagepack


@pytest.fixture(scope="module")
def create_images():
    a = tuple(zip(Testdata.circle_sizes,Testdata.hues,Testdata.image_paths))
    print("*"*100+str(a))
    for i in range(0,len(a)):
        print(i)
        imagepack.create_image(a[i][0],a[i][1],a[i][2])


@pytest.fixture(scope="module")
def create_image():
    a = tuple(zip(Testdata.circle_sizes,Testdata.hues,Testdata.image_paths))[0]
    imagepack.create_image(a[0],a[1],a[2])
    return a

@pytest.fixture(scope="module")
def create_image_neg():
    imagepack.create_image_negative(Testdata.circle_sizes[0],Testdata.hues[0],Testdata.negative_circle_path)


# def precondition():
#     a = tuple(zip(Testdata.circle_sizes,Testdata.hues,Testdata.image_paths))
#     for i in range(0,len(a)):
#         imagepack.create_image(a[i][0],a[i][1],a[i][2])