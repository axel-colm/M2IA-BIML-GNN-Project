import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph, **kwargs):
    """
    Plot a graph
    :param graph: the graph
    """
    nx.draw(graph, **kwargs)
    plt.show()
    
def plot_data(data, **kwargs):
    """
    Plot a torch_geometric.data.Data object
    :param data: the data
    """
    graph = data.to_networkx()
    plot_graph(graph, **kwargs)
    