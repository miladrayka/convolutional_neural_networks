
import os
import argparse
from glob import glob

def delete_excessive_files(path):
    
    for dirpath, _, _ in os.walk(path):
        
        sdf_file = glob(dirpath + '//*.sdf')
        if sdf_file:
            os.remove(sdf_file[0])
            
        pdb_pocket_file = glob(dirpath + '//*_pocket.pdb')
        if pdb_pocket_file:
            os.remove(pdb_pocket_file[0])

if __name__ == '__main__' :
    
    parser = argparse.ArgumentParser(description='deleting sdf and _pocket.pdb files')
    parser.add_argument('path', help = 'files directory')
    args = parser.parse_args()
    
    delete_excessive_files(args.path)
    
    print('process is completed')
