import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='generate [compressor_time,entropy_time,entropy,compress] format csv file and generate compress/entropy graph')
parser.add_argument('--logsf', type=str, help='path to dmesg logs', required=True)
parser.add_argument('--out', type=str, help='path to outfile', required=True)
args = parser.parse_args()

def main():
    if not os.path.exists(args.logsf):
        print(f">>>>> file {args.logsf} doesn't exists")
        exit(1)

    print(f">>>>> processing {args.logsf}...")

    data = list()
    with open(args.logsf, 'r') as f:
        while (line := f.readline()):
            line = line[line.find(":")+2:]
            compress_time, entropy_time, entropy, new_page_size = list(map(int, line.split('|')))
            # if new_page_size > 4096:
                # print(compress_time, entropy_time, entropy, new_page_size)
            data.append([compress_time, entropy_time, entropy, 4096 / new_page_size])

    print(f">>>>> generating {args.out}...")
    df = pd.DataFrame(data, columns = ['compressor_time', 'entropy_time', 'entropy', 'compress'])
    df.to_csv(args.out, sep='\t')
    print(f">>>>> Done!")

    compress = list()
    entropy = list()
    for el in data:
        entropy.append(el[2])
        compress.append(el[3])

    plt.plot(compress, entropy, '^g', markersize=0.3)
    plt.ylabel('Энтропия')
    plt.xlabel('Коэффициент сжатия')
    plt.show()


if __name__ == "__main__":
    main()
