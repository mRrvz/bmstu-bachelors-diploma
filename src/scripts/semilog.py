import argparse
import os
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='show semilog graph (compress coeff/entropy)')
parser.add_argument('--coeffsf', type=str, help='path to file which contains compress coeffs', required=True)
parser.add_argument('--entropyf', type=str, help='path to file which contains pages entropy', required=True)
args = parser.parse_args()


def main():
    if not os.path.exists(args.entropyf):
        print(f">>>>> file {args.entropyf} doesn't exists")
        exit(1)

    if not os.path.exists(args.coeffsf):
        print(f">>>>> file {args.coeffsf} doesn't exists")
        exit(1)

    print(f">>>>> processing {args.coeffsf}...")

    coeffs = list()
    cnt = 0
    with open(args.coeffsf, 'r') as f:
        while (num := f.readline()):
            cnt += 1
            if cnt % 100 == 0:
                coeffs.append(float(num))

    print(f">>>>> processing {args.entropyf}...")

    entropy = list()
    cnt = 0
    # dump_02.txt
    with open(args.entropyf, 'r') as f:
        while (num := f.readline()):
            cnt += 1
            if cnt % 100 == 0:
                entropy.append(float(num))

    plt.semilogx(coeffs, entropy, 'g^', markersize=0.1)
    plt.ylabel('Энтропия')
    plt.xlabel('Коэффициент сжатия')
    plt.show()


if __name__ == "__main__":
    main()
