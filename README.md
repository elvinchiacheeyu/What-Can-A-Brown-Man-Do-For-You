# What-Can-A-Brown-Man-Do-For-You
## What is the maximum  grid dimension can be executed by the code
| Grid  | Output Display |
| ------------- | ------------- |
| 20x20  | ![image](https://github.com/user-attachments/assets/ac639415-9077-4f2d-a972-7f378230510e)  |
| 30x30  | ![image](https://github.com/user-attachments/assets/c6b8f1df-c970-4fd6-a58e-970e300ac903)  |
| 50x50  | ![image](https://github.com/user-attachments/assets/fa41166d-63fb-415f-9c1b-9dcba260d5e2)  |

But when i run a 100x100 grid, the output only display the grid only no path is found so I could said that the maximum grid dimension is 50x50
## What is A* algorithm

The A* algorithm is a powerful and widely used graph traversal and path finding algorithm. It finds the shortest path between a starting node and a goal node in a weighted graph. 

There are two heuristic function in A* algorithm which are manhattan distance and euclidean distance. In another word, manhattan distance only allow vertical and horizontal movement but euclidean distance allow vertical, horizontal and diagonal movement which i think is more practical in robot application.

Given the grid 20x20 below, we can compare the output display from using manhattan distance and euclidean distance.
| Heuristic function  | Output Display |
| ------------- | ------------- |
| Manhattan distance  | ![image](https://github.com/user-attachments/assets/595d2eda-62e5-439b-91aa-5b19615560ff)  |
| Euclidean distance  | ![image](https://github.com/user-attachments/assets/ac639415-9077-4f2d-a972-7f378230510e)  |

The reason why using manhattan distance cannot find path to the endpoint is that the path is blocked by obstacles unless it can move in diagonal direction.

![image](https://github.com/user-attachments/assets/420de3b0-27ca-4ae4-b0e3-b867c1a91a91)

This is why initially I was using manhattan distance but after Tash given me a new grid to try with my code , I found out that manhattan distance cannot be used in this grid then I switched to using euclidean distance.

## Time Complexity
Instead of measuring actual time required in executing each statement in the code, Time Complexity considers how many times each statement executes. 

## Time Complexity for A* algorithm
Two things need to  be considered for time complexity which are grid size and heap operation
| Grid Size  | Heap operate |
| ------------- | ------------- |
|The grid size represents the number of cells the algorithm may potentially process. In the worst case, all cells are processed at least once. | The algorithm uses a priority queue (min-heap) to store cells to be processed, with each insertion/removal taking O(logV) time, where V is the number of elements in the heap.In the worst case, the heap can grow to contain all cells, i.e. V=n×m.  |
|This gives a base complexity of O(n×m) for processing all nodes.   |Therefore, every insertion or removal takes O(log(n×m)).  |

```
Total time complexity = O(n×mlog(n×m))
```
## Worse time complexity
The grid below with 30x30 dimension is said to have the worst time complexity

![image](https://github.com/user-attachments/assets/5a9ebaf8-be92-4b8e-bcc3-c3676b60d04e)

There are many obstacles, forcing the algorithm to check multiple paths before finding a valid one. \
The heuristic is ineffective or too small, making the algorithm behave like Dijkstra's algorithm (which explores all cells with increasing distance). \

## Best time complexity
The grid below with 30x30 dimension has the best time complexity

![image](https://github.com/user-attachments/assets/e0189e92-4e0d-4072-bf4f-7de051032d4a)

This is because only a few obstacles in the grid so the start and end points are very close or even adjacent, allowing A* to find the shortest path with minimal exploration. \
The heuristic is admissible and highly accurate, meaning A* only explores the direct path to the goal without unnecessary detours.

### Output
| Time Complexity  | Output Display |
| ------------- | ------------- |
| Worse Time Complexity | ![image](https://github.com/user-attachments/assets/ad3f909c-6887-4aa4-8cb3-8447cf504cec)  |
| Best Time Complexity  | ![image](https://github.com/user-attachments/assets/7b38ef97-8f4b-4229-8531-d5489364078c)  |


## Two End points

![image](https://github.com/user-attachments/assets/db0c2978-779b-473b-9e0f-610ca3d50faa)

The starting point will move to closer end point and ignore the other end point.

## Two Start points

![image](https://github.com/user-attachments/assets/c6788e8a-d232-4f54-9bea-9e0ceb06f5d9)

Only one of the starting point will find its path to the end point, the other one doesn't move at all.

## When the path is blocked

![image](https://github.com/user-attachments/assets/5f421f9f-641e-4d76-9370-7228a5ce4c84)

Since the Start point is being blocked by obstacle, the output will be as shown below : \

![image](https://github.com/user-attachments/assets/75dabe52-c934-4998-a6a6-49e727ab3c5b)

