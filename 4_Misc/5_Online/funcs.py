def cube_root(val):
    """
    Given number, return the cube root of the number
    """
    return val ** (1 / 3)

print(cube_root(8.0))

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale

print(project_to_distance(2, 7, 4))

def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())

def poly(a):
    return -5*a**5 + 67*a**2 - 47
print(poly(0))
print(poly(1))
print(poly(2))

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * (1 + rate_per_period) ** periods
    

print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(500, .04, 10, 10))