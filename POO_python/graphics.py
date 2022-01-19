#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graphics_simple.html')
    fig = figure()

    total_values = int(input('How many values do you want graph? '))
    x_vals = list(range(total_values))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Value Y for {x} :'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
