import matplotlib.pyplot as plt
import numpy as np
mnist_test = open("mnist_test.csv", 'r')
line = mnist_test.readline()
mnist_test.close()
pic = line.split(',')
num = pic[0]
a = np.asarray(pic)
a = a[1:]
a = a.reshape(28, 28)
a = a.astype(np.float64)
a = a / 255

plt.imshow(a)
plt.show()
