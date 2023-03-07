#!/bin/python3

import os
from argparse import ArgumentParser

parser = ArgumentParser(description='Rename files to pg_1, pg_2, ..., pg_n')
parser.add_argument('--dir', '-d',
                    type=str,
                    help='directory of the files to be renamed',
                    required=True)

args = parser.parse_args()

for i, file in enumerate(sorted(os.listdir(args.dir)), 1):
    
    old_file = os.path.join(args.dir, file)
    new_file = os.path.join(args.dir, f'pg_{i}.jpg')
    os.rename(old_file, new_file)

