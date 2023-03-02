# Convolutional Neural Networks
Required files for repeating "Investigating the impact of convolutional neural networks through distance-weighted atomic contact features on binding affinity prediction" paper.

Steps:
 1. Download **PDBbind** 2016 dataset from this [site](http://www.pdbbind.org.cn/).
 2. Use `delete_excessive_files.py` to delete `.sdf` an `_pocket.pdb` files from PDBbind 2016 (both refined and general sets).
 3. Use `generate_features.py` script to generate features for your data. Output is saved in `.pkl` format.
 4. Finally, use `train_and_analysis.ipynb` for training and analyzing your results.
