import matplotlib.pyplot as plt


def collatz(n: int):
    list_for_plot_y = [n]
    count = 0
    list_for_plot_x = [count]
    if n == 1:
        n = 3 * n + 1
        count += 1
        list_for_plot_y.append(n)
        list_for_plot_x.append(count)

    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
            list_for_plot_y.append(n)
            count += 1
            list_for_plot_x.append(count)
        else:
            n = n // 2
            list_for_plot_y.append(n)
            count += 1
            list_for_plot_x.append(count)
    plt.text(list_for_plot_x[-1], (list_for_plot_y[-1] + 0.5),
             f'Действие {list_for_plot_x[-1]}, результат {list_for_plot_y[-1]}')
    plt.plot(list_for_plot_x, list_for_plot_y, 'r--')
    plt.show()


collatz(int(input('Введите n: ')))
