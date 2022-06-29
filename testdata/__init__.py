import os
import definition


class Testdata():
    root_dir = definition.ROOT_DIR
    python_path = os.path.join(root_dir, r'venv\scripts\python')
    circle_maker = os.path.join(root_dir, r'SDETcirclemaker\circlemaker.py')
    circle_sizes = [300, 250, 200, 150]
    hues = [100, 150, 200, 250]
    image_paths = [root_dir + r'\output_files\test1.png',
                   root_dir + r'\output_files\test2.png',
                   root_dir + r'\output_files\test3.png',
                   root_dir + r'\output_files\test4.png']
    negative_circle_path = root_dir + r'\output_files\negtest1.png'
    negative_circle_maker = os.path.join(root_dir, r'SDETcirclemaker\negativecirclemaker.py')
    pixel_plot = {"400x400": (76, 399)}
