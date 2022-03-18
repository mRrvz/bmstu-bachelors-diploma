import argparse
import os
import pandas as pd
from scipy.stats import entropy

parser = argparse.ArgumentParser(description='calculate entropy for every page in swapfile and save this to file')
parser.add_argument('--swap', type=str, help='path to swapfile', required=True)
parser.add_argument('--out', type=str, help='path to outfile', required=True)
args = parser.parse_args()

# 1
def shannon_entropy(data):
    pd_series = pd.Series(list(data))
    counts = pd_series.value_counts()
    return entropy(counts)


def main():
    if not os.path.exists(args.swap):
        print(f">>>>> file {args.swap} doesn't exists")
        exit(1)

    entropy_list = list()
    with open(args.swap, 'rb') as f:
        page_n = 0
        print(f">>>>> processing {args.swap}...")

        while (byte := f.read(4096)):
            page_n += 1
            entropy_list.append(shannon_entropy(byte))
            if page_n % 10000 == 0:
                print(f">>> current page: {page_n}")

    with open(args.out, 'w') as f:
        for entr in entropy_list:
            f.write(f"{entr }\n")

    print(f">>>>> Done!")


if __name__ == "__main__":
    main()
