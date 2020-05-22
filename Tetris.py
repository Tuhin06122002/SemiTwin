class Tetromino:
    def __init__(self, shapeNo, grid):
        self.SN = shapeNo
        if shapeNo == 0:
            self.cell1 = [0,4]
            self.cell1 = [0,5]
            self.cell1 = [0,6]
            self.cell1 = [0,7]
        
        elif shapeNo == 1:
            pass

        elif shapeNo == 2:
            pass

        elif shapeNo == 3:
            pass
        
        elif shapeNo == 4:
            pass

        elif shapeNo == 5:
            pass

        elif shapeNo == 6:
            pass
    
    def moveRight(self,grid):
        # Checking if possible
        for x in [self.cell1, self.cell2, self.cell3, self.cell4]:
            #Border
            if x[1] > 10:
                # Alert
                return 0
            # If cell to the right is filled
            if grid[x[0]][x[1]+1]:
                return 0
        
        for x in [self.cell1, self.cell2, self.cell3, self.cell4]:
            grid[x[0]][x[1]] = 0
            x[1] += 1
            grid[x[0]][x[1]] = 1
        
        return 1
    
    def moveLeft(self,grid):
        pass

    def moveDown(self,grid):
        pass