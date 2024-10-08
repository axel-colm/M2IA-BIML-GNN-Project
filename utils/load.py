import networkx as nx
import torch_geometric.utils


def load_graphml(file_path: str) -> nx.Graph:
    """
    Load a graph from a file
    :param file_path: the path to the file
    :return: the graph
    """
    return nx.read_graphml(file_path)

def convert_data(graph: nx.Graph) -> torch_geometric.data.Data:
    """
    Convert a graph to a torch_geometric.data.Data object
    :param graph: the graph
    :return: the torch_geometric.data.Data object
    """
    data = torch_geometric.utils.from_networkx(graph)
    return data

def load_data():
    graph = load_graphml("dataset/airportsAndCoordAndPop.graphml")
    data = convert_data(graph)
    return data

    
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    graph = load_graphml("dataset/airportsAndCoordAndPop.graphml")
    print(graph)
    data = convert_data(graph)
    print(data)