from ising_class import *
acell=cell(3,3,10) #dArgs: i,j,n
print(acell.cellspin())
acell.spin.flip()#reaching through the cell to the inner spin object
print(acell.left)#directly accessing the neighbor indices
print(acell.right)
print(acell.up)
print(acell.down)
