import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Julia: 

    def __init__(self, im_width = 500, im_height = 500, zabs_max = 10, nit_max =1000, xmin = -1.5 , xmax = 1.5, ymin = -1.5, ymax = 1.5, c = complex(0.0, 0.0)):
        self.im_width, self.im_height = im_width, im_height
        self.c = c
        self.zabs_max = zabs_max
        self.nit_max = nit_max
        self.xmin, self.xmax = xmin, xmax
        self.xwidth = self.xmin - self.xmax
        self.ymin, self.ymax = ymin, ymax
        self.yheight = self.ymin - self.ymax
        self.julia = np.zeros((self.im_width, self.im_height))
        for ix in range(self.im_width):
            for iy in range(self.im_height):
                nit = 0
                # Map pixel position to a point in the complex plane
                self.z = complex(ix / self.im_width * self.xwidth + self.xmin,
                                iy / self.im_height * self.yheight + self.ymin)
                # Do the iterations
                while abs(self.z) <= self.zabs_max and nit < self.nit_max:
                    self.z = self.z**2 + self.c
                    nit += 1
                shade = 1-np.sqrt(nit / self.nit_max)
                ratio = nit / self.nit_max
                self.julia[ix, iy] = ratio
    
    def plot(self): 
        fig, ax = plt.subplots()
        ax.imshow(self.julia, interpolation='nearest', cmap=cm.hot)
        # Set the tick labels to the coordinates of z0 in the complex plane
        xtick_labels = np.linspace(self.xmin, self.xmax, self.xwidth / 0.5)
        ax.set_xticks([(x-self.xmin) / self.xwidth * self.im_width for x in xtick_labels])
        ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
        ytick_labels = np.linspace(self.ymin, self.ymax, self.yheight / 0.5)
        ax.set_yticks([(y-self.ymin) / self.yheight * self.im_height for y in ytick_labels])
        ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
        plt.show()

Terrain = Julia(c = complex(0.65, 1.3))
Terrain.plot()





        
        