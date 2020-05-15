import argparse
from random import random, seed

# Author: Kristijan Ceple

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output_file", type=str,
                    help="Name of file where the hypotheses will be saved to. Defaults to HD_out.txt",
                    default="HD_out.txt")
parser.add_argument("-hp", "--hypotheses_number", type=int,
                    help="Number of hypotheses. Defaults to 771",
                    default=771)
parser.add_argument("-n", "--hypothesis_length", type=int,
                    help="Number of nums in each hypothesis/row. Defaults to 100",
                    default=100)
parser.add_argument("-b", "--boundary", type=int,
                    help="Upper distance boundary. Defaults to 20",
                    default=20)
args = parser.parse_args()

seed()

hypotheses = []
with open(args.output_file, 'w') as file:
    for i in range(args.hypotheses_number):
        to_add = []
        for _ in range(args.hypothesis_length):
            val = random() * args.boundary
            to_add.append(round(val, 2))

        hypotheses.append(to_add)

    # Got them, time to write them to a file
    for hypothesis in hypotheses:
        to_output_line = ' '.join(map(str, hypothesis))
        file.write(to_output_line)
        file.write('\n')
