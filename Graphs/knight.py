#!/usr/bin/env python3
"""Solving Knight's Tour problem"""
import importlib.util
import pathlib
import sys

try:
    importlib.util.find_spec(
        ".".join(pathlib.Path(__file__).parts[-3]),
        "pythonds3",
    )
except ModuleNotFoundError:
    sys.path.append(
        f"{pathlib.Path(__file__).parents[1]}/"
    )
finally:
    from pythonds3.graphs import Graph


def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = row * board_size + col
            new_positions = gen_legal_moves(
                row, col, board_size
            )
            for row2, col2 in new_positions:
                other_node_id = row2 * board_size + col2
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph


def pos_to_node_id(row, col, board_size):
    return row * board_size + col


def gen_legal_moves(row, col, board_size):
    new_moves = []
    move_offsets = [
        (-1, -2),  # left-down-down
        (-1, 2),  # left-up-up
        (-2, -1),  # left-left-down
        (-2, 1),  # left-left-up
        (1, -2),  # right-down-down
        (1, 2),  # right-up-up
        (2, -1),  # right-right-down
        (2, 1),  # right-right-up
    ]
    for r_off, c_off in move_offsets:
        if (
            0 <= row + r_off < board_size
            and 0 <= col + c_off < board_size
        ):
            new_moves.append((row + r_off, col + c_off))
    return new_moves


def legal_coord(row, col, board_size):
    return 0 <= row < board_size and 0 <= col < board_size


def knight_tour(n, path, u, limit):
    u.color = "gray"
    path.append(u)
    if n < limit:
        neighbors = sorted(list(u.get_neighbors()))
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].color == "white":
                done = knight_tour(
                    n + 1, path, neighbors[i], limit
                )
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.color = "white"
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.get_neighbors():
        if v.color == "white":
            c = 0
            for w in v.get_neighbors():
                if w.color == "white":
                    c = c + 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.color = "gray"
        self.time = self.time + 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        start_vertex.color = "black"
        self.time = self.time + 1
        start_vertex.closing_time = self.time


#
#  drawKnight
#
#  Created by Brad Miller on 2005-03-17.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os
from graphics import *

def main():
    
    tDat = file('tour.dat')
    win = GraphWin('tour',500,500)
    win.setCoords(0,0,8,8)
    rList = []
    for i in range(8):
        for j in range(8):
            rList.append(Rectangle(Point(i,j),Point(i+1,j+1)))
    
    for i in rList:
        i.draw(win)
    stepList = tDat.read().split()
    print(stepList)
    start = int(stepList[0])
    startSquare = rList[start]    
    i = 1
    while i < len(stepList):
        endSquare = rList[int(stepList[i])]
        l = Line(startSquare.getCenter(),endSquare.getCenter())
        l.draw(win)
        t = Text(endSquare.getCenter(),str(i))
        t.draw(win)
        startSquare = endSquare
        i = i + 1
        
        
def NodeToPos(id):
   return ((id/8, id%8))
   
   
if __name__ == '__main__':
    main()

