import matplotlib.pyplot as plt
import numpy as np

functions = {
    1: {
        "function": "y' = x^3 - y на [0; 2] при y(0) = 0",
        "value": lambda x, y: x ** 3 - y,
        "solution": lambda x: x ** 3 - 3 * x ** 2 + 6 * x + 6 * np.exp(-x) - 6,
        "a": 0,
        "b": 2,
        "y0": 0
    },
    2: {
        "function": "y' = y + (1 + x) * y^2 на [1; 1.5] при y(1) = -1",
        "value": lambda x, y: y + (1 + x) * y ** 2,
        "solution": lambda x: - 1 / x,
        "a": 1,
        "b": 1.5,
        "y0": -1
    },
    3: {
        "function": "y' = x + 1 - y на [1; 1.6] при y(1) = 2",
        "value": lambda x, y: x + 1 - y,
        "solution": lambda x: np.exp(1 - x) + x,
        "a": 1,
        "b": 1.6,
        "y0": 2
    }
}


def get_info():
    print("Выберите один из вариантов:")
    for key, value in functions.items():
        print(str(key), ": ", value["function"])
    num = int(input())
    selected_val = functions[num]
    h = float(input("Введите шаг: "))
    e = float(input("Введите точность: "))
    return selected_val["value"], selected_val["a"], selected_val["b"], h, selected_val["y0"], e, selected_val[
        "solution"]


def paint(a, b, correct_fun, euler_x, euler_y, milt_x, milt_y):
    x = np.arange(a, b, 0.01)
    ax = plt.gca()
    ax.plot(x, correct_fun(x), "red", linewidth=1.5, label='Точный')
    ax.plot(euler_x, euler_y, 'blue', linewidth=1.5, label='Эйлер')
    ax.plot(milt_x, milt_y, 'orange', linewidth=1.5, label='Милт')
    plt.legend()
    plt.show()


def print_for_user(x_euler, y_euler, x_milt, y_milt, correct):
    print("Метод Эйлера:")
    print("%12.4s%12.4s%12.4s" % ("X", "Y", "correct Y"))
    for i in range(0, len(x_euler)):
        print("%12.4f%12.4f%12.4f" % (round(x_euler[i], 5), round(y_euler[i], 5), round(correct(x_euler[i]), 5)))

    print("Метод Милта:")
    print("%12.4s%12.4s%12.4s" % ("X", "Y", "correct Y"))
    for i in range(0, len(x_milt)):
        print("%12.4f%12.4f%12.4f" % (round(x_milt[i], 5), round(y_milt[i], 5), round(correct(x_milt[i]), 5)))
