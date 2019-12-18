from pymatgen.analysis.graphs import StructureGraph
import networkx as nx
from pymatgen.analysis.dimensionality import get_dimensionality_larsen
from pymatgen.analysis.local_env import CrystalNN


def is_3D(struct):
    cnn = CrystalNN()
    bonded = cnn.get_bonded_structure(struct)
    dimensionality = get_dimensionality_larsen(bonded)
    is_3D = dimensionality == 3
    return(is_3D)


def has_floating_species(struct):
    struc_graph = StructureGraph.with_local_env_strategy(struct, CrystalNN())

    g = nx.Graph(struc_graph.graph)
    components = nx.connected_components(g)
    print(components)
    n_components = len(list(components))

    if n_components == 1:
        return(False)

    return(True)
