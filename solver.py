def make_interpolater(left_min, left_max, right_min, right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min

    scaleFactor = float(right_span) / float(left_span)

    def interp_fn(value):
        return right_min + (value-left_min)*scaleFactor

    return interp_fn

def write_mandelbrot_file(file_name, mandelbrot_pixel_data):
    with open(file_name, "w") as f:
        i = 0
        while i < len(mandelbrot_pixel_data) - 1:
            f.write(str(mandelbrot_pixel_data[i][0]) + "," + str(mandelbrot_pixel_data[i][1]) + " ")
            i += 1
        f.write(str(mandelbrot_pixel_data[i][0]) + "," + str(mandelbrot_pixel_data[i][1]))
        f.close()

def read_mandelbrot_file(file_name):
    with open(file_name, "r") as f:
        data = []
        for line in f.read().split(" "):
            split_line = line.split(",")
            data.append((int(split_line[0]), float(split_line[1])))

        return data

def find_mandelbrot(width, height, xmin, xmax, ymin, ymax, ITERATIONS):
    # Make sure image is well-proportioned
    x_ratio = (xmax-xmin)/width
    y_ratio = (ymax-ymin)/height
    if x_ratio >= y_ratio:
        mapper_x = make_interpolater(0, width, xmin, xmax)
        ypad = (x_ratio * height - (ymax - ymin)) / 2
        mapper_y = make_interpolater(height, 0, ymin-ypad, ymin+ypad)
    else:
        mapper_y = make_interpolater(height, 0, ymin, ymax)
        xpad = (y_ratio * width - (xmax-xmin)) / 2
        mapper_x = make_interpolater(0, width, xmin-xpad, xmax+xpad)

    # Convert from pixel to mathematical dimensions
    mapped_y = [mapper_y(i) for i in range(height)]
    mapped_x = [mapper_x(j) for j in range(width)]

    # calculate mandelbrot set
    mandelbrot_pixel_data = []

    for i in range(height):
        for j in range(width):
            x, y = mapped_x[j], mapped_y[i]
            a, a2 = 0, 0
            b, b2 = 0, 0

            iteration = 0
            while a2 + b2 <= 1000000 and iteration < ITERATIONS:
                b = (a + a) * b + y
                a = a2 - b2 + x
                a2 = a*a
                b2 = b*b
                iteration += 1

            mandelbrot_pixel_data.append((iteration, a2 + b2))

    # cache file for later renders
    file_name = f"cache/{width},{height},{xmin},{xmax},{ymin},{ymax},{ITERATIONS}.txt"
    write_mandelbrot_file(file_name, mandelbrot_pixel_data)

    return mandelbrot_pixel_data
