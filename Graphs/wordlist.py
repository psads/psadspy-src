#!/usr/bin/env python3
"""Solving Wordladder problem"""

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


def build_graph(filename):
    buckets = {}
    the_graph = Graph()
    with open(filename, "r", encoding="utf8") as file_in:
        all_words = file_in.readlines()
    # create buckets of words that differ by 1 letter
    for line in all_words:
        word = line.strip()
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i + 1 :]}"
            buckets.setdefault(bucket, set()).add(word)

    # connect different words in the same bucket
    for similar_words in buckets.values():
        for word1 in similar_words:
            for word2 in similar_words - {word1}:
                the_graph.add_edge(word1, word2)
    return the_graph


g = build_graph("Graphs/words_small")
print(len(g))

from pythonds3.basic import Queue
from pythonds3.graphs import Graph


def bfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current = vert_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vert_queue.enqueue(neighbor)
        current.color = "black"


bfs(g.get_vertex("fool"))


def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key)
        current = current.previous


traverse(g.get_vertex("sage"))
