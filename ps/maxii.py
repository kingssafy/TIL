import sys
sys.stdin = open('maxinos.txt')

def isalready(x, y, n):
    return x == 0 or y == 0 or x == n-1 or y == n-1
def isonly(array, x, y):
    #search left, right, up, down
    result = {}
    result['left'] = 0 if sum(array[x][:y]) else 1
    result['right'] = 0 if sum(array[x][y+1:]) else 1
    result['up'] = 0 if sum(array[idx][y] for idx in range(x-1, -1, -1)) else 1
    result['down'] = 0 if sum(array[idx][y] for idx in range(x+1, len(array))) else 1
    if sum(result.values()) == 1:
        for key, value in result.items():
            if value:
                return key


def fill(x, y, array, direction, do=True):
    array[x][y] = 3 if do else 1
    putter = 2 if do else 0
    if direction == "left":
        for col in range(y-1,-1,-1):
            array[x][col] = putter
        return
    
    if direction == "right":
        for col in range(y+1,len(array)):
            array[x][col] = putter
        return

    if direction == "up":
        for row in range(x-1,-1,-1):
            array[row][y] = putter
        return

    if direction == "down":
        for row in range(x+1, len(array)):
            array[row][y] = putter
        return

def isconnectable(x, y, array, direction):
    #if direction == "left": return sum(array[x][:y]) == 0
    if direction == "left":
        for idx in range(y):
            if array[x][idx]:
                return False
        return True
    #if direction == "right": return sum(array[x][y+1:]) == 0
    if direction == "right":
        for idx in range(y+1, len(array)):
            if array[x][idx]:
                return False
        return True
    #if direction == "up": return sum(array[idx][y] for idx in range(x)) == 0
    if direction == "up":
        for idx in range(x):
            if array[idx][y]:
                return False
        return True
    #if direction == "down" : return sum(array[idx][y] for idx in range(len(array)-1,x,-1)) == 0
    if direction == "down":
        for idx in range(len(array)-1, x, -1):
            if array[idx][y]:
                return False
        return True

def recurse(array, sequence):
    global counter
    directions = ["left", "right", "up", "down"]
    for x, y in sequence:
        if array[x][y] == 3 : break
        for direction in directions:
            if isconnectable(x, y, array, direction):
                fill(x, y, array, direction, True)
                counter += 1
                connects = counter
                if connects >= max(result):
                    lines = sum(i.count(2) for i in array)
                    if connects in result:
                        if lines < result[connects]:
                            result[connects] = lines
                    else:
                        result[connects] = lines
                recurse(array, sequence)
                fill(x, y, array, direction, False)
                counter -= 1
                
        
        

for tc in range(1, int(input()) + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    sequence = [] 
    result = {0:0}
    for x in range(N):
        for y in range(N):
            arrayvalue = array[x][y]
            if arrayvalue == 1 and isalready(x,y,N):
                array[x][y] == 3
            elif arrayvalue == 1 and isonly(array,x,y):
                fill(x,y, array, isonly(array,x,y), True)
            elif arrayvalue == 1 and (isconnectable(x, y, array, "left") or isconnectable(x, y, array, "right")
                                      or isconnectable(x, y, array, "up") or isconnectable(x, y, array, "down")):
                sequence.append((x,y))
    connects = sum(i.count(3) for i in array)
    if connects >= max(result):
        lines = sum(i.count(2) for i in array)
        if connects in result:
            if lines < result[connects]:
                result[connects] = lines
        else:
            result[connects] = lines
    counter = connects
    recurse(array, sequence)
    maxconnects = max(result)
    leastline = result[maxconnects]
    print(f"#{tc} {leastline}")
