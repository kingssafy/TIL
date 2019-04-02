import sys
sys.stdin = open("5250_input.txt")

from heapq import heappush, heappop, heapify
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def djik():
    heap = [];
    heappush(heap, (0, 0, 0))
    processed = [[0 for _ in range(N)] for _ in range(N)]
    distance = [[10000000 for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    while heap:
        throw, y, x = heappop(heap)
        if processed[y][x]: continue;
        processed[y][x] = True
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if (min(ny,nx)>= 0 and max(ny, nx) < N):
                distance[ny][nx] = min(distance[ny][nx], distance[y][x]+max(0, grid[ny][nx]-grid[y][x])+1)
                if ny==N-1 and nx == N-1:
                    return distance[N-1][N-1]
                heappush(heap, (distance[ny][nx], ny, nx))
    return distance[N-1][N-1]


T = int(input())
for tc in range(T):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    results = [[0 for _ in range(N)] for _ in range(N)]
    print(f"#{tc+1}", djik())

