import os
from utils import *
import networkx as nx
import torch
import torch.nn.functional as F
from torch_geometric.data import Data, DataLoader
from torch_geometric.nn import GCNConv
from sklearn.preprocessing import LabelEncoder


# Load dataset
graph = load_graphml("dataset/airportsAndCoordAndPop.graphml")
print(graph)  # Graph with 3363 nodes and 13547 edges

data = convert_data(graph)

# Encode labels
encoder = LabelEncoder()
data.country_int = encoder.fit_transform(data.country)
data.city_int = encoder.fit_transform(data.city_name)

print(f"Number of classes: {data.num_classes}")
print(f"Target tensor: \n\t{data.y}")
print(f"Original labels: \n\t{encoder.inverse_transform(data.y)}")

# Define model
class GCN(torch.nn.Module):
    def __init__(self, dim_in, dim_h, dim_out):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(dim_in, dim_h)
        self.conv2 = GCNConv(dim_h, dim_out)
        
    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)
    
    
# Create model and optimizer
dim_in = data.num_features
dim_h = 16
dim_out = data.num_classes
model = GCN(dim_in, dim_h, dim_out)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.CrossEntropyLoss()

# Train model
model.train()
for epoch in range(1000):
    optimizer.zero_grad()
    out = model(data)
    loss = loss_fn(out, data.y)
    loss.backward()
    optimizer.step()
    
    loss_val = loss.item()
    acc_val = int(out.argmax(dim=1).eq(data.y).sum().item()) / data.num_nodes
    print(f"Epoch: {epoch + 1:03d}, Loss: {loss_val:.4f}, Accuracy: {acc_val:.4f}")
    
