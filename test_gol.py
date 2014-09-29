# -*- coding: utf-8 -*-

import unittest
from gol import parse_world, print_world, alive_neighbor_count, Coords

class GameOfLifeTests(unittest.TestCase):
	def assert_neighbors(self, str, p, expected):		
		rows = [s.strip() for s in str.split('\n')]
		world = parse_world(rows)
		#print_world(world)
		count = alive_neighbor_count(Coords(p[0],p[1]), world)
		self.assertEqual(expected, count)
	
	def test_alive_neighbor_case_top_left(self):
		self.assert_neighbors(
		"""##~
		   ##~
		   ~~~""", (0,0), 3)
	def test_alive_neighbor_case_top_middle(self):
		self.assert_neighbors(
		"""###
		   ###
		   ~~~""", (0,1), 5)
	def test_alive_neighbor_case_top_right(self):
		self.assert_neighbors(
		"""###
		   ###
		   ~~~""", (0,2), 3)
	def test_alive_neighbor_case_middle_left(self):
		self.assert_neighbors(
		"""##~
		   ##~
		   ##~""", (1,0), 5)
	def test_alive_neighbor_case_middle_empty(self):
		self.assert_neighbors(
		"""~~~
		   ~#~
		   ~~~""", (1,1), 0)
	def test_alive_neighbor_case_middle_full(self):
		self.assert_neighbors(
		"""###
		   ###
		   ###""", (1,1), 8)
	def test_alive_neighbor_case_middle_right(self):
		self.assert_neighbors(
		"""~##
		   ~##
		   ~##""", (1,2), 5)
	def test_alive_neighbor_case_bottom_left(self):
		self.assert_neighbors(
		"""##~
		   ##~
		   ##~""", (2,0), 3)
	def test_alive_neighbor_case_bottom_middle(self):
		self.assert_neighbors(
		"""~~~
		   ###
		   ###""", (2,1), 5)
	def test_alive_neighbor_case_bottom_right(self):
		self.assert_neighbors(
		"""~~~
		   ###
		   ###""", (2,2), 3)


	

