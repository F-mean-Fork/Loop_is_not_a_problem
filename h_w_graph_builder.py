import glob
import os
import matplotlib as plt


# def graph (x, y):
#     plt.plot(x, y)
#     plt.show()

#File finder
x = []
y = []
for filename in glob.glob('file_name*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       text = f.read()
    #    x = text[:, 0] #width
    #    y = text[:, 1] #height

       
       
