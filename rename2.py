import os
from configs import *
from shutil import copyfile

def extract_num(filename):
    return float(filename.split('_')[1].split('.xcf')[0])

def main():
    i = 1
    
    for file in sorted(os.listdir('romcom/xcf'), key=lambda fname: extract_num(fname)):
        # if extract_num(file) <= 4:
        #     continue

        old_file = os.path.join('romcom/xcf', file)
        new_file = os.path.join('romcom/xcf2', f'pg_{i}.xcf')
        copyfile(old_file, new_file)
        i+=1
#    os.mkdir(os.path.join(dirname, 'out'))

if __name__ == '__main__':
    main()