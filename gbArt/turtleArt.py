from svg_turtle import SvgTurtle


def draw_spiral(t):
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(20):
        d = 50 + i*i*1.5
        t.pencolor(0, 0.05*i, 0)
        t.width(i)
        t.forward(d)
        t.right(144)
    t.end_fill()


def write_file(draw_func, filename, width, height):
    t = SvgTurtle(width, height)
    draw_func(t)
    t.save_as(filename)


def main():
    write_file(draw_spiral, 'example.svg', 500, 500)
    print('Done.')


if __name__ == '__main__':
    main()