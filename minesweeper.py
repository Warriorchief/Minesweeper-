def minesweeper(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    out=[]
    for r in range(rows):
        #print("working with r being",r)
        rowminecounts=[]
        for c in range(cols):
            #print("working with c being",c)
            tot=0
            
            if r-1>=0: #if there is a row above it
                if c-1>=0: #if there is a column to the left
                    if matrix[r-1][c-1]==True:
                        tot+=1
                if matrix[r-1][c]==True:
                    tot+=1
                if c+1<cols: #if there is a column to the right of it
                    if matrix[r-1][c+1]==True:
                        tot+=1
            
            if c-1>=0:
                if matrix[r][c-1]==True:
                    tot+=1
            #note that the box itself having a mine does NOT count toward tot
            if c+1<cols:
                if matrix[r][c+1]==True:
                    tot+=1
            
            if r+1<rows:
                if c-1>=0:
                    if matrix[r+1][c-1]==True:
                        tot+=1
                if matrix[r+1][c]==True:
                    tot+=1
                if c+1<cols:
                    if matrix[r+1][c+1]==True:
                        tot+=1
            rowminecounts.append(tot)
        out.append(rowminecounts)
    print(out)
    return out

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

#minesweeper(matrix) = [[1, 2, 1],
                       #[2, 1, 1],
                       #[1, 1, 1]]
