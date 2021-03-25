from mpi4py import MPI
import os
import math
from datetime import datetime

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def function(path_=os.getcwd()+"/transfer.txt",dest_=os.getcwd()+"/transfer.txt"):
    if rank == 0:
        with open(path_,'r') as f:
            data = f.read()
            send = comm.send(data,dest=1)
            f.close()
    elif rank == 1:
        data = comm.recv(source=0)
        with open(dest_,'w') as f:
            f.write(data)
            f.close()

if __name__=='__main__':
    if(not os.path.exists(os.getcwd()+"/transfer.txt")):
        temp=""
        for i in range(0,100000):
            temp+="Copy 1,2 copy 1,2 \n"
        with open(os.getcwd()+"/transfer.txt",'w') as f:
            f.write(temp)
    function()