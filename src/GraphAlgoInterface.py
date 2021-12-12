from typing import List

from src import GraphInterface
from abc import ABC, abstractmethod


class GraphAlgoInterface(ABC):
    """This abstract class represents an interface of a graph."""

    @abstractmethod
    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        pass

    @abstractmethod
    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        pass

    @abstractmethod
    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        pass

    @abstractmethod
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        pass

    @abstractmethod
    def center(self) -> int:
        """
        Finds the node which minimizes the max distance to all the other nodes.
        Assuming the graph isConnected, else return None. See: https://en.wikipedia.org/wiki/Graph_center
        @return: the id of the Node to which the max shortest path to all the other nodes is minimized.
        """
        pass

    @abstractmethod
    def tsp(self) -> list:
        """
        Computes a list of consecutive nodes which go over all the nodes in cities.
        the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution -
        the lower the better.
        See: https://en.wikipedia.org/wiki/Travelling_salesman_problem
        Notes:
        The list does NOT need to be a set! It may contain multiple appearances of the same node,
        yet the pairs of consecutive nodes in the  list is  a SET of directed edges.
        """
        pass

    # @abstractmethod
    # def plot_graph(self) -> None:
    #     """
    #     Plots the graph.
    #     If the nodes have a position, the nodes will be placed there.
    #     Otherwise, they will be placed in a random but elegant manner.
    #     @return: None
    #     """
    #     pass
