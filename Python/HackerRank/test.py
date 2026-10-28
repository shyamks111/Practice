
## 


class Test:
    def func1(self, grid):
        done = False
        row_len = len(grid)
        col_len = len(grid[0])
        direction = "right"
        pickups = []
        total = 0
        visited = list()
        i, j = 0, 0
        change_direction = False
        while not done:
            change_direction = False
            if direction == "right":    
                if j >= col_len or grid[i][j] == -1 or [i,j] in visited:
                    direction = "down"
                    i += 1
                    j -= 1
                else:
                    change_direction = True
                    pickups.append([i,j])
                    visited.append([i,j])
                    total += grid[i][j]
                    j += 1

            if direction == "down":
                if i>row_len or grid[i][j] == -1 or [i,j] in visited:
                    direction = "left"
                    j -= 1
                    i -= 1
                    change_direction = True
                else:
                    pickups.append([i,j])
                    visited.append([i,j])
                    total += grid[i][j]
                    i += 1

            if direction == "left":
                if j<0 or grid[i][j] == -1 or [i,j] in visited:
                    direction = "up"
                    i -= 1
                    j += 1
                    change_direction = True
                else:
                    pickups.append([i,j])
                    visited.append([i,j])
                    total += grid[i][j]
                    j -= 1

            if direction == "up":
                if i<0 or grid[i][j] == -1 or [i,j] in visited:
                    print([i,j])
                    direction = "right"
                    j += 1
                    i += 1
                    change_direction = True
                else:
                    pickups.append([i,j])
                    visited.append([i,j])
                    total += grid[i][j]
                    i -= 1

            if i >= 0 and j >= 0 and i<row_len and j < col_len and change_direction == True:
                if [i,j] in visited or grid[i][j] == -1:
                     print([i,j])
                     done = True
        
        print(pickups)
        print(total)

            

if __name__ == '__main__':
    test = Test()
    grid = [[1,2,3,4],
            [4,5,7,2],
            [8,3,-1,3],
            [2,5,9,6],
            [1,4,2,-1]]
    test.func1(grid)
