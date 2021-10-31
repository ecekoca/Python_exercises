#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:04:16 2021

@author: ece

We have N planets in a row. For them to be in a stable state the sum of even 
planets' masses and odd planets' masses needs to be equal. If not, a planet 
needs to be destroyed to reach the stable state. Write a function to find the
planet that needs to destroyed, and print its index. If there are no possible
solutions print -1. if there are multiple solutions destroy the planet with 
the smallest index

"""

def getPlanetToDestroy(planets):

	tot_eve=[]
	tot_odd=[]
	for i in range(len(planets)):
		remaining_planets=planets.copy()
		remaining_planets.pop(i)
		new_even=0
		new_odd=0
		for j in range(len(remaining_planets)):
			if j%2==0:
				new_even+=remaining_planets[j]
			else:
				new_odd+=remaining_planets[j]
		tot_eve.append(new_even)
		tot_odd.append(new_odd)
	to_destroy=[]
	for i in range(len(planets)):
		if tot_eve[i]==tot_odd[i]:
			to_destroy.append(i)
	if len(to_destroy)>=1:
		print(to_destroy[0])
	elif len(to_destroy)==0:
		print(-1)
			
planets=[2,4,6,3,4]
getPlanetToDestroy(planets)