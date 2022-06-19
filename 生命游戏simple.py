import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, ImageMagickWriter
import numpy as np

class matrix:
    init_matrix=[(i,j) for i in [-1,0,1] for j in [-1,0,1]]
    def __init__(self, matrix_input):
        self.matrix = matrix_input.copy()
        self.shape = matrix_input.shape

    def neighbor_number(self,i,j):
        m, n = self.shape
        res = sum([self.matrix[(i+k)%m,(j+l)%n] for (k,l) in matrix.init_matrix])
        res = res - self.matrix[i,j]
        return res

    def __next__(self):
        x = self.matrix
        y = self.matrix.copy()
        m,n = self.shape
        for i in range(m):
            for j in range(n):
                neighbor = self.neighbor_number(i,j)
                now = self.matrix[i,j]
                if now == 0 and neighbor == 3:
                    y[i,j] = 1
                if now == 1 and (neighbor <2 or neighbor > 3):
                    y[i,j] = 0
        self.matrix = y
        return x

b = np.zeros((20,20),dtype='int8')
b[3,4] = 1
b[4,5] = 1
b[5,3] = 1
b[5,4] = 1
b[5,5] = 1

test = matrix(b)

m, n = b.shape
fig, ax = plt.subplots(figsize = (10*m/n,10))
ax.set_xlim([-0.5,m-0.5])
ax.set_ylim([-0.5,n-0.5])
ax.set_xticks(np.arange(-0.5,m-0.5,1))
ax.set_yticks(np.arange(-0.5,n-0.5,1))
ax.invert_yaxis()
ax.grid(True)
def init():
    return ax.imshow(1-next(test),cmap='gray')
def update(frame):
    return ax.imshow(1-next(test),cmap='gray')
ani = FuncAnimation(fig, update, frames = np.arange(100), init_func=init)
writer = ImageMagickWriter(fps = 5)
plt.show()
#ani.save('animation.gif', writer = writer)



