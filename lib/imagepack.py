from lib import execute
from PIL import Image
from testdata import Testdata
import cv2


def find_circle(img):
    image = cv2.imread(img)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray image", gray)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,100,param1=50,param2=24,minRadius=15,maxRadius=0)
    return circles


def get_circle_size(img):
    image = cv2.imread(img)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray image", gray)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,100,param1=50,param2=24,minRadius=15,maxRadius=0)
    return circles.item(2)


def check_if_circle_present(img):
    val = find_circle(img)
    if val is not None:
        return True
    return False


def create_image(size, hue, path):
    execute.execute_command(r'{} {} -d {} -hue {} -path {}'.format(Testdata.python_path,
                                                                   Testdata.circle_maker, size, hue, path))


def create_image_negative(size, hue, path):
    execute.execute_command(r'{} {} -d {} -hue {} -path {}'.format(Testdata.python_path,
                                                                   Testdata.negative_circle_maker, size, hue, path))


def get_image_size(image):
    im = Image.open(image)
    return im.size


def get_pixel_color(image):
    red_image = Image.open(image)
    red_image_rgb = red_image.convert("RGB")
    h,w = get_image_size(image)
    rgb_pixel_value = red_image_rgb.getpixel(Testdata.pixel_plot["{}x{}".format(h,w)])
    return rgb_pixel_value
