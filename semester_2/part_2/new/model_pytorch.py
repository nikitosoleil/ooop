import numpy as np
import torch
import torch.nn as nn
from torch.nn.functional import relu
from torch.optim import Adam

from model_abstract import AbstractModel


class PyTorchModel(nn.Module, AbstractModel):
    def __init__(self):
        super().__init__()
        self.__device = torch.device('cuda:0')

        self.__conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.__pool = nn.MaxPool2d(kernel_size=2)
        self.__drop = nn.Dropout(p=0.25)
        self.__conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.__conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.__fc1 = nn.Linear(in_features=64 * 4 * 4, out_features=128)
        self.__fc2 = nn.Linear(in_features=128, out_features=10)

        self.__loss = nn.CrossEntropyLoss()
        self.__optimizer = Adam(self.parameters(), lr=0.001)

        self.to(self.__device)

    def forward(self, x):
        f = lambda a: self.__drop(self.__pool(relu(a)))
        x = f(self.__conv1(x))
        x = f(self.__conv2(x))
        x = f(self.__conv3(x))
        x = x.view(-1, 64 * 4 * 4)
        x = self.__drop(relu(self.__fc1(x)))
        x = self.__fc2(x)
        return x

    def train_on_batch(self, x: np.ndarray, y: np.ndarray) -> (float, float):
        x = torch.from_numpy(x.transpose(0, 3, 1, 2)).to(self.__device)
        y = torch.from_numpy(y).to(self.__device)

        self.__optimizer.zero_grad()
        prediction = self(x)
        loss = self.__loss(prediction, torch.argmax(y, 1))
        loss.backward()
        self.__optimizer.step()
        loss = loss.item()
        acc = (torch.argmax(prediction, 1) == torch.argmax(y, 1)).sum().item()
        return loss, acc

    def predict_on_batch(self, x: np.ndarray) -> np.ndarray:
        x = torch.from_numpy(x.transpose(0, 3, 1, 2)).to(self.__device)
        with torch.no_grad():
            return self(x).cpu().numpy()
