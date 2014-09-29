#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import namedtuple
from time import sleep
import sys
import os

Coords = namedtuple('Coords', ['x', 'y'])
World = namedtuple('World', ['size_x', 'size_y', 'state'])

def get_world(size_x,size_y, seeds=[]):
	world = [[False for y in xrange(size_y)] for x in xrange(size_x)]
	for c in seeds:
		world[c[0]][c[1]] = True
	return World(size_x, size_y, state)

def print_world(world):	
	for row in world.state:
		for c in row:			
			print('#', end='') if c else print('.', end='') 
		print('')

def parse_world(rows):
	seed = []	
	size_x = len(rows)
	size_y = len(rows[0]) # take the width from first row
	for i, row in enumerate(rows):
		for j, c in enumerate(row):
			if c == '#':
				seed.append((i,j))
	return get_world(size_x, size_y, seed)

def get_first_or_default(list, default=None):
	for i in list:
		return i
	return default

def alive_neighbor_count(c, world):
	''' Determine neighbor count of the given cell '''	

	top = get_first_or_default(world[max(c.x-1,0):c.x],[]) # top row		
	bottom = get_first_or_default(world[c.x+1:c.x+2],[]) # bottom row
	left = world[c.x][c.y-1:c.y] # left
	right = world[c.x][c.y+1:c.y+2] # right	
	return sum(left + right + top + bottom)

def simulate(world):
	''' Play one round of game of life and return the new state '''	

	next = get_world(world.size_x, world.size_y)
	for x, row in enumerate(world):
		for y, c in enumerate(row):
			count = alive_neighbor_count(Coords(x,y), world)					
			if world.state[x][y]:
				if (count == 2) or (count == 3):
					next.state[x][y] = True
			else:
				if count == 3:
					next.state[x][y] = True					
	return next

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: %s SEED_FILE NO_GENERATIONS' % sys.argv[0])
		exit(0)

	no_rounds = int(sys.argv[2])	
	current = None
	with open(sys.argv[1], 'r') as f:		
		rows = [row.strip() for row in f]
		current = parse_world(rows)
		
	for i in xrange(no_rounds):	
		os.system('clear')
		print("Round %s" % i)
		print_world(current)
		current = simulate(current)
	 	sleep(0.1)