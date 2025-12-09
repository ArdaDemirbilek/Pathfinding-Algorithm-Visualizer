# Pathfinding Algorithm Visualizer
### Side-by-Side Dijkstra vs. A with Perfect Maze Generation (Pygame)

This project is an interactive visualization tool that generates a perfect maze and solves it using Dijkstra’s Algorithm (left side) and A* Search (right side) simultaneously.
Its goal is to demonstrate the differences in exploration patterns, efficiency, and path optimality between the two algorithms in a clear, intuitive, and real-time manner.

## Features
### Perfect Maze Generator
Uses Iterative Backtracking (DFS-based) to create a loop-free maze with exactly one valid path between any two points.

### Dual-Grid Visualization
Dijkstra runs on the left grid, A* on the right — both operate on an identical maze for a fair comparison.

### Real-Time Exploration Rendering
Algorithms are implemented as Python generators, updating the grid step-by-step for smooth animation.

### Manhattan Heuristic for A*
A* is guided toward the goal, producing much more focused search patterns than Dijkstra.

### Clean and Modern Color Palette
Soft backgrounds, teal visited nodes, and warm final-path colors make the visualization aesthetically pleasing.

### Project Structure
```
├── main.py             # Main loop + event handling
├── Grid.py             # Maze generation, rendering, dual-grid structure
├── Node.py             # Node class, status control, Manhattan heuristic
├── algorithms.py       # A* and Dijkstra implementations (generator-based)
├── settings.py         # Visualization settings: colors, sizes, constants
└── README.md
```

The architectural separation keeps the project modular, readable, and easy to extend.

## Algorithms
### Perfect Maze Generation – Iterative Backtracking

DFS with an explicit stack

Ensures full connectivity

Guarantees no cycles

Maze layout is duplicated to both grids for unbiased comparison

### Dijkstra’s Algorithm (Unweighted)

Treats all edges as cost = 1

Explores uniformly in all directions

Produces optimal paths but tends to expand a large number of nodes

### A* Search

Uses f = g + h with Manhattan Distance

Much more directed than Dijkstra

Typically reaches the goal faster with fewer explored nodes

## How to Use

Run the program:

python main.py


Left-click once to generate the maze.

Press SPACE to start both algorithms simultaneously.

Close the window to exit.

## Color Scheme (from settings.py)
```
Element	RGB Color
Background	(35, 38, 44)
Wall	(40, 70, 115)
Walkable	(180, 200, 180)
Start	(90, 200, 160)
Goal	(220, 120, 110)
Visited	(66, 120, 80)
Frontier	(240, 200, 110)
Final Path	(215, 185, 110)
```
## Technical Highlights

Built with Pygame

Step-by-step simulation using Python generators

Priority queues via heapq

Robust grid system with precomputed neighbors

Identical maze replication for algorithm parity

Clean separation of concerns across modules
