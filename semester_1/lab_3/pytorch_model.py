import torch
import torch.nn as nn
from torch.nn.functional import relu
from torch.optim import Adam
import torch.utils.data as data
from tqdm import tqdm
import numpy as np


class PyTorchModel(nn.Module):
    def __init__(self, dg):
        super().__init__()

        device = torch.device('cuda:0')

        self.__train_dataset = data.TensorDataset(torch.from_numpy(dg.train_x.transpose(0, 3, 1, 2)).to(device),
                                                  torch.from_numpy(dg.train_y).to(device))
        self.__test_dataset = data.TensorDataset(torch.from_numpy(dg.test_x.transpose(0, 3, 1, 2)).to(device),
                                                 torch.from_numpy(dg.test_y).to(device))

        self.__conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
        self.__pool = nn.MaxPool2d(kernel_size=2)
        self.__drop = nn.Dropout(p=0.25)
        self.__conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.__conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.__fc1 = nn.Linear(in_features=64 * 4 * 4, out_features=128)
        self.__fc2 = nn.Linear(in_features=128, out_features=10)

        self.__loss = nn.CrossEntropyLoss()
        self.__optimizer = Adam(self.parameters(), lr=0.001)

        self.to(device)

    def forward(self, x):
        f = lambda a: self.__drop(self.__pool(relu(a)))
        x = f(self.__conv1(x))
        x = f(self.__conv2(x))
        x = f(self.__conv3(x))
        x = x.view(-1, 64 * 4 * 4)
        x = self.__drop(relu(self.__fc1(x)))
        x = self.__fc2(x)
        return x

    def fit(self, epochs, batch_size):
        loader = data.DataLoader(self.__train_dataset, batch_size=batch_size)
        n = len(self.__train_dataset)
        for i in range(epochs):
            loss, acc = 0, 0
            for x, y in tqdm(loader, desc='Epoch {0}'.format(i + 1)):
                self.__optimizer.zero_grad()
                prediction = self(x)
                loss = self.__loss(prediction, torch.argmax(y, 1))
                loss.backward()
                self.__optimizer.step()
                loss += loss.item()
                acc += (torch.argmax(prediction, 1) == torch.argmax(y, 1)).sum().item()
            print('loss: {}, acc: {}'.format(loss, acc / n))

    def predict(self):
        loader = data.DataLoader(self.__test_dataset, batch_size=256)
        prediction = []
        with torch.no_grad():
            for x, y in loader:
                p = self(x).cpu().numpy()
                prediction.append(p)
        prediction = np.vstack(prediction)
        return prediction
