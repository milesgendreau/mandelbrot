import random, math, pygame

### -----GLOBAL CONSTANTS----- ###
LN_2 = math.log(2)


def create_color_scheme():
    scheme = [10,
              round(6.28*random.random(), 3), round(6.28*random.random(), 3), round(6.28*random.random(), 3),
              round(3.00*random.random(), 3), round(3.00*random.random(), 3), round(3.00*random.random(), 3)]

    print(f"({scheme[1]},{scheme[2]},{scheme[3]}) // {scheme[4]},{scheme[5]},{scheme[6]}")

    return scheme

def get_color(iterations, squared_norm, scheme):
    #pow2 = (1 << iterations)
    #v = math.log(norm)/pow2
    v = math.log(squared_norm)

    #x = math.log(v)/5
    x = (math.log(v) - (iterations*LN_2))/scheme[0]

    o1, o2, o3 = 4.71, 4.71, 4.71 # scheme[1], scheme[2], scheme[3]
    a, b, c = scheme[4], scheme[5], scheme[6]
    r = (math.sin(a*x + o1) + 1)/2
    g = (math.sin(b*x + o2) + 1)/2
    b = (math.sin(c*x + o3) + 1)/2

    color = (255 * r, 255 * g, 255 * b)

    return color

def render_mandelbrot(mandelbrot_pixel_data, width, height, ITERATIONS, color_scheme=create_color_scheme()):
    pygame.init()
    im = pygame.Surface((width, height))
    pxarray = pygame.PixelArray(im)

    for i in range(height):
        for j in range(width):
            data = mandelbrot_pixel_data[i*width + j]
            color = (0, 0, 0)
            if data[0] < ITERATIONS:
                color = get_color(data[0], data[1], color_scheme)

            pxarray[j, i] = color

    im = pxarray.make_surface()
    pygame.image.save(im, "mandelbrot.png")
    print("Image Saved!")
