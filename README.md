# 8-puzzle
Solve 8-puzzle, a type of sliding tile puzzle, by Classic Search Algorithms.





## Goals
The goal of this repo are:
- understand efficient state representation, including a successor state function
-  Implement iterative deepening
- Build basic heuristics
- Implement A* search


## Background
The 8-Puzzle is a type of sliding tile puzzle, the most common of which is the [15-puzzle](https://en.wikipedia.org/wiki/15_puzzle).

The 8-Puzzle consists of a 3x3 grid of numbered tiles, with one tile (#9) missing. The object of the puzzle is to get the tiles in a particular order, subject to the constraints of physically sliding one tile at a time into the open space.

For our puzzle, we will consider that the following state is our goal:
 
|   1   |   2   |   3   |
| :---: | :---: | :---: |
| **8** | **.** | **4** |
| **7** | **6** | **5** |



## Tasks
**1. State Representation**


**2. Problem Setup**
- Build a `Node` class with **state**, **parent**, **action**, and **path_cost** as `member variables`
- Create a function or method `child_node` that takes a node and an action and returns the **child** that is generated when the given action is taken
- Use the actions **Right**, **Left**, **Up** and **Down** which correspond to how a tile is moved into a blank space to generate the next state

