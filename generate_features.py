
import pickle
import argparse
import numpy as np
from glob import glob
from pathlib import Path
from scipy import spatial
from biopandas.mol2 import PandasMol2
from biopandas.pdb import PandasPdb


atom_types = {'OE1':'O','HB1':'H','SD':'S','HE':'H','1HD1':'H','1HG1':'H','2HD2':'H','1HD2':'H','CE3':'C','OH':'O','CZ':'C',
           'HG2':'H','HN2':'H','NZ':'N','HN1':'H','3HD2':'H','CD2':'C','2HH2':'H','HH2':'H','O':'O','2HD1':'H','ND1':'N',
           'HH':'H','1HE2':'H','HB':'H','NH2':'N','3HG1':'H','ND2':'N','CZ3':'C','HA2':'H','OG':'O','CG2':'C','CE':'C',
           'SG':'S','NE':'N','CG':'C','CB':'C','HG1':'H','NH1':'N','2HE2':'H','3HD1':'H','1HH2':'H','HD2':'H','HD1':'H',
           'NE1':'N','HB2':'H','HA':'H','3HG2':'H','HN3':'H','HE1':'H','CD':'C','HZ3':'H','OD1':'O','N':'N','H':'H',
           'HA1':'H','2HH1':'H','NE2':'N','CE2':'C','C':'C','OD2':'O','2HG1':'H','CD1':'C','HE3':'H','1HH1':'H','2HG2':'H',
           'HB3':'H','CE1':'C','OXT':'O','CH2':'C','1HG2':'H','HZ1':'H','OG1':'O','HZ2':'H','CA':'C','CG1':'C','HE2':'H',
           'CZ2':'C','OE2':'O','HG':'H','HZ':'H'}

elements = ['H','C','N','O','S','P','F','Cl','Br','I']



def ligand_specific_element_coordinates(mol2_object, element):
	#return ligand's coordinates for specific element.
    
    coordinates = mol2_object.df[mol2_object.df['element_type'] == element].loc[:, ['x', 'y', 'z']]
    
    return coordinates.to_numpy()


def protein_specific_element_coordinates_modify(pdb_object, element):
	#return protein's coordinates for specific element.
    
    coordinates =  pdb_object.df['ATOM'][pdb_object.df['ATOM']['element_type'] == element].loc[:, ['x_coord', 'y_coord', 'z_coord']]

    return coordinates.to_numpy()


def sum_cutoff(distances, cutoff):
	#sperate interactions into different cutoffs
    
    sum_inverse_selected_distaces = []
    
    for item in np.arange(1, 31, cutoff):
    
        selected_distances = distances[(item <= distances) & (distances < item + 0.5)]
        sum_inverse_selected_distaces.append(sum(list(map(lambda x: 1./x, selected_distances))))
    
    return sum_inverse_selected_distaces


def generate_features_without_amino_acids(path):
	#generate distance-weighted atomic contact features for protein-ligand complexes. 
	#return pickle file contains dictionary with PDBid key and features values.
    
    data = {}
    
    entries = Path(path)
        
    for num, entry in enumerate(entries.iterdir()):
        
        
        features = np.zeros((60, 100))

        ligand_file = glob(str(entry) + '//*.mol2')
        
        protein_file = glob(str(entry) + '//*.pdb')
        
        pmol = PandasMol2().read_mol2(ligand_file[0])
        
        pmol.df['element_type'] = pmol.df['atom_type'].apply(lambda x: x.split('.')[0])
        
        ppdb = PandasPdb().read_pdb(protein_file[0])
        
        ppdb.df['ATOM']['element_type'] = ppdb.df['ATOM']['atom_name'].map(atom_types)
           
        i = 0
    
        for ligand_element in elements:
        
            for protein_element in elements:
        
        
                ligand_coords = ligand_specific_element_coordinates(pmol, ligand_element)
                protein_coords = protein_specific_element_coordinates_modify(ppdb, protein_element)
        
                distances = spatial.distance.cdist(ligand_coords, protein_coords).ravel()
        
                features[:, i] = sum_cutoff(distances, 0.5)
        
                i += 1
            
        data[entry.name] = features

    with open('data.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL) 


if __name__ == '__main__' :
    
    parser = argparse.ArgumentParser(description='generating distance-weighted atomic contact features for protein-ligand complex')
    parser.add_argument('path', help = 'files directory for protein-ligand complexes')
    args = parser.parse_args()
    
    generate_features_without_amino_acids(args.path)
    
    print('process is completed')        
