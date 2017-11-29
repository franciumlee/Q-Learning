import numpy as np

Q_table=np.zeros((6,6))
Q_table=np.array(Q_table)
R_table=np.zeros((6,6))
R_table=np.array(R_table)

R_table=[[-1,-1,-1,-1,0,-1],
         [-1, -1, -1, 0, -1,100],
        [-1, -1, -1, 0, -1, -1],
        [-1, 0, 0, -1, 0, -1],
       [0, -1, -1, 0, -1, 100],
        [-1, -1, -1, -1, 0, 100]]
R_table=np.array(R_table)

for x in range(0,500):
    for s in range (0,6):
        for a in range (0,6):
            if(R_table[s,a]>-1):
                Q_table[s,a]=R_table[s,a]+0.8*Q_table[a,:].max()
    if(x % 50 == 0):
        print("Step:",x)
        print(Q_table)
print("normalize")
print(Q_table/5)