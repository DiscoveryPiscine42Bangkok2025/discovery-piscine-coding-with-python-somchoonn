def checkmate(board):
# แบ่งเป็นแถว
    rows = board.strip().split("\n")
    new_rows = []
    line = len(rows)

# Check Board
    for i in rows:
        if len(i) != line:
            print("Board is not square")
            return 

# Change not allow to .
    for i in range(line):
        new_row = ""
        for j in range(line):
            if rows[i][j] not in "KPBQR.":
                new_row += "."
            else:
                new_row += rows[i][j]
        new_rows.append(new_row)
    rows = new_rows
                
        
    
# หาตำแหน่งของ K
    king_count = 0
    king_pos = None
    for i in range(line):
        for j in range(line):
            if rows[i][j] == "K":
                king_pos = (i, j)
                king_count += 1
# Check King
    if king_count != 1:
        print("There should be exactly one King")
        return
        
# เช็คการเดินของตัวต่างๆ
    def in_bounds(x, y):
        return 0 <= x < line and 0 <= y < line
    
    def pawn_check(x, y):
        #(y,x) 
        moves = [(-1, -1), (-1, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and (nx, ny) == king_pos:
                return True
        return False
    
    def bishop_check(x, y):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                if not in_bounds(nx, ny):
                    break
                if (nx, ny) == king_pos:
                    return True
                if rows[nx][ny] != ".":
                    break
        return False
    
    def rook_check(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]        
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                if not in_bounds(nx, ny):
                    break
                if (nx, ny) == king_pos:
                    return True
                if rows[nx][ny] != ".": 
                    break
        return False
    def queen_check(x, y):
    # รวมทิศทางของ Rook และ Bishop
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx, ny = nx + dx, ny + dy
                if not in_bounds(nx, ny):
                    break
                if (nx, ny) == king_pos:
                    return True
                if rows[nx][ny] != ".":
                    break
        return False

        
    # Check คำตอบ
    for i in range(line):
        for j in range(line):
            piece = rows[i][j]
            if piece == "P" and pawn_check(i, j):
                print("Success")
                return
            elif piece == "B" and bishop_check(i, j):
                print("Success")
                return
            elif piece == "R" and rook_check(i, j):
                print("Success")
                return
            elif piece == "Q" and queen_check(i, j):
                print("Success")
                return
    print("Fail")