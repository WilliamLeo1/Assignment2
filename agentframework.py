# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:56:32 2021

@author: bootl
"""

import random

#Particle movement parameters can be changed from here
NS_movement = 0.1 #chance of moving randomly North or South
E_movement = 0.75 #chance of moving East
W_movement = 0.05 #chance of moving West
D_movement = 0.7 #chance of particle descent. Must be greater than 0.5
A_movement = 0.66 #chance of ascent

#Functions to be used in model defined here
class Agent():
    def __init__(self, i, environment, agents):
        self.x = 50
        self.y = 150
        self.z = 75
        self.environment = environment
        self.i = i
        self.agents = agents
        self.store = 0
        
    def __str__(self):
        return "id=" + str(self.i) + ", x=" + str(self.x) + ", y=" + str(self.y)
    
    #Function for particle movement
    def move(self):
        if random.random() < NS_movement:
            self.y = (self.y + random.choice((-1, 1))) % 300
        else:
            self.y = (self.y) % 300
        if random.random() < E_movement:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x) % 300
        if random.random() < W_movement:
            self.x = (self.x - 1) % 300
        else:
            self.x = (self.x) % 300    
        if random.random() < D_movement:
            self.z = (self.z - 1) 
        else:
            if random.random() < A_movement:
                self.z = (self.z + 1)
            else:
                self.z = (self.z)
               
    #function for particles landing            
    def land(self):
        if self.z == 0:
            self.environment[self.y][self.x] += 1
        
        
            
            
            
            