import solver, renderer
from os.path import exists

### -----SETUP----- ###

# Specify image size and mathematical size (for zoomed in renderings)
# 241, 201 / 801, 601 / 2401, 1801
width, height = 241, 201
#xmin, xmax, ymin, ymax = -2.00, 0.47, -1.12, 1.12 # default
xmin, xmax, ymin, ymax = -2.2, 0.67, -1.22, 1.22

# Specify max iterations to run
ITERATIONS = 100

# Specify which "slice" of the set to view [NON-FUNCTIONAL]
start = 0
s2 = start*start

# Color related parameters [NON-FUNCTIONAL]
color_inside = (0,0,0) # color used for the inside of the set

### -----RENDER IMAGE----- ###
file_name = f"cache/{width},{height},{xmin},{xmax},{ymin},{ymax},{ITERATIONS}.txt"
if (exists(file_name)):
    mandelbrot_pixel_data = solver.read_mandelbrot_file(file_name)
else:
    mandelbrot_pixel_data = solver.find_mandelbrot(width, height, xmin, xmax, ymin, ymax, ITERATIONS)

renderer.render_mandelbrot(mandelbrot_pixel_data, width, height, ITERATIONS)
