import matplotlib.pyplot as plt
import numpy as np

def show_compress():
    x1 = np.arange(1, 4) - 0.2
    x2 = np.arange(1, 4) + 0.2

    y1 = [396, 327, 592]
    y2 = [395, 282, 559]

    fig, ax = plt.subplots()

    ax.bar(x1, y1, width = 0.4)
    ax.bar(x2, y2, width = 0.4)

    ax.set_facecolor('seashell')

    plt.xlabel('Тип файлов')
    plt.ylabel('Сжатый размер (МБ)')
    plt.show()


def show_time():
    x1 = np.arange(1, 4) - 0.2
    x2 = np.arange(1, 4) + 0.2

    y1 = [5.5720, 16.320, 16.461]
    y2 = [20.980, 31.1960, 21.872]

    fig, ax = plt.subplots()

    ax.bar(x1, y1, width = 0.4)
    ax.bar(x2, y2, width = 0.4)

    ax.set_facecolor('seashell')

    plt.xlabel('Тип файлов')
    plt.ylabel('Время (секунд)')
    plt.show()


def main():
    show_time()

if __name__ == "__main__":
    main()