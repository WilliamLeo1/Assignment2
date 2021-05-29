# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:32:28 2021

@author: bootl
"""

import matplotlib
import random
import csv
import bs4
import requests
import agentframework


#Number of particles and the start coordinates of the bomb are defined here
num_of_agents=5000
y_bomb_coord=150
x_bomb_coord=50
z_bomb_coord=75 #start height of bomb

# Create the environment
environment = []
f = open("raster.txt")
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()    
f.close()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Create the agents at the starting point
agents=[]
for i in range(num_of_agents):   
    y = y_bomb_coord
    x = x_bomb_coord
    z = z_bomb_coord
    agents.append(agentframework.Agent(i, environment, agents))
    
carry_on = True


#main run
for i in range(num_of_agents):
    while agents[i].z > 0: 
        agents[i].move()
        agents[i].land()
#print("x", agents[i].x, "y", agents[i].y, "z", agents[i].z)
print(environment)#prints number of particles at each coordinate
        

#plot points
matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
