#!/bin/python3 

import os
from argparse import ArgumentParser

parser = ArgumentParser(description='Rename files to pg1, pg2, ...')
parser.add_argument('dir',
                    type=str,
                    help='directory of the files to be renamed')

args = parser.parse_args()

os.chdir(args.dir)

i = 1

for file in sorted(os.listdir()):
    ext = file.split('.')[-1]
    if len(ext) < 2 or ext not in ['png', 'jpg', 'webp', 'gif']:
        continue
    os.rename(file, f'pg{i}.{ext}')
    i += 1

