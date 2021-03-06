import sys
import itertools
sys.stdin = open("bricks_input.txt")

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)
directions = [up, right, down, left]

def getnext(center, direction):
    return tuple(map(sum, zip(center, direction)))

def tupmul(tuple, times):
    return (tuple[0]*times, tuple[1]*times)

def ingrid(center, grid):
    return 0<= center[0]< len(grid) and 0<= center[1] < len(grid[0])

def hammer(grid, center):
    frontier = [center]
    while frontier:
        next_frontier = []
        for center in frontier:
            temp = grid[center[0]][center[1]]
            grid[center[0]][center[1]] = 0
            for j in range(1, temp):
                for direction in directions:
                    next = getnext(center, tupmul(direction,j))
                    if ingrid(next, grid) and grid[next[0]][next[1]]:
                        next_frontier.append(next)

        frontier = next_frontier

def cleanup(grid):
    for c in range(W):
        for r in range(H-1,-1,-1):
            if not grid[r][c]:
                for j in range(r, -1, -1):
                    if grid[j][c]:
                        grid[r][c], grid[j][c] = grid[j][c], grid[r][c]
                        break

def recurse(grid, depth=0):
    global result
    if depth == N:
        temp = calculate(grid)
        if temp < result:
            result = temp
    else:
        for w in range(W):
            newgrid = [row[:] for row in grid]
            cleanup(newgrid)
            hammer(newgrid, getstartpoint(newgrid, w))
            cleanup(newgrid)
            recurse(newgrid, depth+1)
            del newgrid



def calculate(grid):
    result = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] >0:
                result += 1
    return result

def getstartpoint(grid, w):
    center = (H-1, w)
    value = grid[H-1][w]
    if not value:
        return (H-1, w)
    else:
        for j in range(H-1, -1, -1):
            if grid[j][w]:
                pass
            else:
                return (j+1, w)
        else:
            return (0, w)
    

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    result = 999999999999999
    recurse(grid)
    print(f"#{tc+1} {result}")
    
