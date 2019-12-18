import pymatgen.core.structure as structure
def struc_to_cif(structure):
    structure.to(filename='structure.cif',fmt='cif')
