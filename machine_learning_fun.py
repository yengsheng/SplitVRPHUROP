# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:22:16 2020

@author: Yong Sheng
"""

import numpy as np
import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
x_values = [[i for i in range(11)], [j for j in range(11)]]
x_train = np.array(x_values*3, dtype = np.float32)
x_train = x_train.reshape(-1, 1)

y_values = [2*i + i for i in x_values]
y_train = np.array(y_values, dtype = np.float32)
y_train = y_train.reshape(-1, 1)


class linearRegression(torch.nn.Module):
  def __init__(self, inputSize, outputSize):
    super(linearRegression, self).__init__()
    self.linear = torch.nn.Linear(inputSize, outputSize)

  def forward(self, x):
    out = self.linear(x)
    return out
inputDim = 1
outputDim = 1
learningRate = 0.01
epochs = 100
model = linearRegression(inputDim, outputDim)

if torch.cuda.is_available():
  model.cuda()

criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

for epoch in range(epochs):
  if torch.cuda.is_available():
    inputs = Variable(torch.from_numpy(x_train).cuda())
    labels = Variable(torch.from_numpy(y_train).cuda())
  else:
    inputs = Variable(torch.from_numpy(x_train))
    labels = Variable(torch.from_numpy(y_train))

  optimizer.zero_grad()
  outputs = model(inputs)
  loss = criterion(outputs, labels)
  print(loss)
  loss.backward()

  optimizer.step()
  print('epoch {}, loss{}'.format(epoch, loss.item()))

  with torch.no_grad():
    if torch.cuda.is_available():
      predicted = model(Variable(torch.from_numpy(x_train).cuda())).cpu().data.numpy()
    else:
      predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()
    print(predicted)

plt.clf()
plt.plot(x_train, y_train, 'go', label='True data', alpha = 0.5)
plt.plot(x_train, predicted, '--', label='Predictions', alpha=0.5)
plt.legend(loc='best')
plt.show()

