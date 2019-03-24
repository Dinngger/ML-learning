import matplotlib.pyplot as plt
import numpy as np
mnist_test = open("mnist_test.csv", 'r')
plt.ion()
plt.figure(1)
for i in range(100):
    line = mnist_test.readline()
    pic = line.split(',')
    num = pic[0]
    a = np.asarray(pic)
    a = a[1:]
    a = a.reshape(28, 28)
    a = a.astype(np.float64)
    a = a / 255
    plt.clf()
    plt.imshow(a)
    print(num)
    plt.pause(1)
mnist_test.close()
