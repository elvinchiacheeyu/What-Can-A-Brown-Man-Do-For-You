# What-Can-A-Brown-Man-Do-For-You
## What is the maximum  grid dimension can be executed by the code
| Grid  | Output Display |
| ------------- | ------------- |
| 20x20  | ![image](https://github.com/user-attachments/assets/ac639415-9077-4f2d-a972-7f378230510e)  |
| 30x30  | ![image](https://github.com/user-attachments/assets/c6b8f1df-c970-4fd6-a58e-970e300ac903)  |
| 50x50  | ![image](https://github.com/user-attachments/assets/fa41166d-63fb-415f-9c1b-9dcba260d5e2)  |

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
