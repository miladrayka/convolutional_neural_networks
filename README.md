![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
# Convolutional Neural Networks
![GA](https://github.com/miladrayka/convolutional_neural_networks/blob/main/Graphical%20Abstract%20(GitHub).png)
Required files for repeating "Investigating the impact of convolutional neural networks through distance-weighted atomic contact features on binding affinity prediction" paper.

Steps:
 1. Download **PDBbind** 2016 dataset from this [site](http://www.pdbbind.org.cn/).
 2. Use `delete_excessive_files.py` to delete `.sdf` an `_pocket.pdb` files from PDBbind 2016 (both refined and general sets).
 3. Use `generate_features.py` script to generate features for your data. Output is saved in `.pkl` format.
 4. Finally, use `train_and_analysis.ipynb` for training and analyzing your results.

**Caution**: `general_set_binding_data.csv`, `refined_minus_core_set_binding_data.csv`, and `core_set_binding_data.py` files contain binding affinity data which are used during training process.

**Attribution**: The graphical abstract has been designed using images from [Flaticon](Flaticon.com).
