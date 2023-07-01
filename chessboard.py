import numpy as np
chessboard=[]
for h in range(8):
    tmp=[]
    for w in range(8):
        if (h+w)%2==0:
            tmp.append(0)
        else:
            tmp.append(1)
    chessboard.append(tmp)
chessboard=(np.array(chessboard, ndmin=2))
counter=0
for h in range(8):
    for w in range(8):
        if chessboard[h,w]==1 and w<6:
            counter+=1
print(counter)