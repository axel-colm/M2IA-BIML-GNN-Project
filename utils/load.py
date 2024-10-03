import networkx as nx

def load_dataset():
    """
    Load the dataset
    :return: the graph
    """    
    FILE_PATH = "dataset/airportsAndCoordAndPop.graphml"
    return nx.read_graphml(FILE_PATH)


if __name__ == "__main__":
    graph = load_dataset()
    