from ui import get_info, paint, print_for_user


def method_updated_euler(fun, a, b, h, y0, e, n_max=-1):
    n_max -= 1
    y_arr = []
    x_arr = []
    yi = y0
    xi = a
    x_arr.append(xi)
    y_arr.append(yi)
    i = 0
    updated_Eyler_fun = lambda y, x, h, fun: y + h / 2 * (fun(x, y) + fun(x + h, y + h * fun(x, y)))

    while xi < b and i != n_max:
        yi_next = updated_Eyler_fun(yi, xi, h, fun)
        yi_next_half_h = updated_Eyler_fun(updated_Eyler_fun(yi, xi, h / 2, fun), xi + h / 2, h / 2, fun)
        if abs(yi_next - yi_next_half_h) > e:
            h /= 2
            continue
        yi = yi_next
        xi = round(xi + h, 5)
        x_arr.append(xi)
        y_arr.append(yi)
        i += 1
    return x_arr, y_arr, h


def method_miln(fun, a, b, h, y0, e):
    x_arr, y_arr, h = method_updated_euler(fun, a, b, h, y0, e, 4)
    f_arr = [None,
             fun(x_arr[1], y_arr[1]),
             fun(x_arr[2], y_arr[2]),
             fun(x_arr[3], y_arr[3])]
    xi = round(x_arr[3] + h, 5)
    n = int(round((b - x_arr[3]) / h, 5) + 4)
    for i in range(4, n):
        yi_predict = y_arr[i - 4] + 4 * h / 3 * (2 * f_arr[i - 3] - f_arr[i - 2] + 2 * f_arr[i - 1])
        while True:
            yi_correct = y_arr[i - 2] + h / 3 * (f_arr[i - 2] + 4 * f_arr[i - 1] + fun(xi, yi_predict))
            if abs(yi_correct - yi_predict) >= e:
                yi_predict = yi_correct
            else:
                break
        y_arr.append(yi_correct)
        f_arr.append(fun(xi, y_arr[i]))
        x_arr.append(xi)
        xi += h
    return x_arr, y_arr


if __name__ == '__main__':
    # value_fun = lambda x_a, y_a: y_a + (1 + x_a) * y_a ** 2
    # a = 1
    # b = 1.5
    # h = 0.1
    # y0 = -1
    # e = 0.001

    value_fun, a, b, h, y0, e, correct = get_info()
    euler_x, euler_y, _ = method_updated_euler(value_fun, a, b, h, y0, e)
    milt_x, milt_y = method_miln(value_fun, a, b, h, y0, e)
    paint(a, b, correct, euler_x, euler_y, milt_x, milt_y)
    print_for_user(euler_x, euler_y, milt_x, milt_y, correct)
