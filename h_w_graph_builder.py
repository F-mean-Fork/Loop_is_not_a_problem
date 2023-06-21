import glob
import os
import matplotlib as plt


# def graph (x, y):
#     plt.plot(x, y)
#     plt.show()

#File finder
x = []
y = []
for filename in glob.glob('C:\\Users\\ivanl\\Desktop\\ITMO\\Hight_width\\N050\\*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       text = f.read()
    #    x = text[:, 0] #width
    #    y = text[:, 1] #height

       
       