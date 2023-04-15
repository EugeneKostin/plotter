import matplotlib.pyplot as plt
import pandas as pd
from config import SOURCE_FILE_PATH


def main():
    data = pd.read_csv(SOURCE_FILE_PATH, sep='\s+', header=None)
    data = pd.DataFrame(data)

    x = data[0]
    y = data[1]

    plt.figure(figsize=(40, 10), dpi=400)
    plt.plot(x, y)
    plt.savefig("graph.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
