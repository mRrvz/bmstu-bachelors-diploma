import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description='generate [page_size,entropy,compressed_size] format csv file')
parser.add_argument('--sizef', type=str, help='path to file which contains compressed pages sizes', required=True)
parser.add_argument('--entropyf', type=str, help='path to file which contains pages entropy', required=True)
parser.add_argument('--out', type=str, help='path to outfile', required=True)
args = parser.parse_args()


def main():
    sizes_list = list()
    entropy_list = list()
    csv_data = list()

    if not os.path.exists(args.sizef):
        print(f">>>>> file {args.sizef} doesn't exists")
        exit(1)

    if not os.path.exists(args.entropyf):
        print(f">>>>> file {args.entropyf} doesn't exists")
        exit(1)

    print(f">>>>> processing {args.sizef}...")
    with open(args.sizef, 'r') as f:
        while (num := f.readline()):
            sizes_list.append(float(num))

    print(f">>>>> processing {args.entropyf}...")
    with open(args.entropyf, 'r') as f:
        while (num := f.readline()):
            entropy_list.append(float(num))

    print(f">>>>> generating {args.out}...")
    for s, e in zip(sizes, entropy):
        csv_data.append([4096, e, s])

    df = pd.DataFrame(data, columns = ['page_size', 'entropy', 'compressed_size'])
    df.to_csv(args.out, sep='\t')
    print(f">>>>> Done!")


if __name__ == "__main__":
    main()
