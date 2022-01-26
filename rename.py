import os
from configs import *

def main():
    i = 1
    
    for file in sorted(os.listdir(raw_dir)):
        
        old_file = os.path.join(raw_dir, file)
        new_file = os.path.join(raw_dir, f'pg_{i}.jpg')
        os.rename(old_file, new_file)
        i+=1
#    os.mkdir(os.path.join(dirname, 'out'))

if __name__ == '__main__':
    main()
