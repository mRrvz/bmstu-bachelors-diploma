import argparse
import os
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='show entropy histogram')
parser.add_argument('--file', type=str, help='path to file which contains pages entropy', required=True)
args = parser.parse_args()

def main():
    min_num = 0
    max_num = 0
    data = list()

    if not os.path.exists(args.file):
        print(f">>>>> file {args.file} doesn't exists")
        exit(1)

    with open(args.file, 'r') as f:
        print(f">>>>> processing {args.file}...")
        while (num := f.readline()):
            num = float(num)
            min_num = min(num, min_num)
            max_num = max(num, max_num)
            data.append(round(num, 1))

    print(f">>>>> Minimum entropy: {min_num}, maximum entropy: {max_num}, entropy count: {len(data)}")
    plt.hist(data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.ylabel('Количество страниц')
    plt.xlabel('Энтропия')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


if __name__ == "__main__":
    main()
