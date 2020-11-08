from algo import *

dist=[[1,2,3],[4,5,6],[7,8,9]]
co_mat=coordinate_mat(dist)
for i in range(3):
	for j in range(3):
		print(co_mat[i][j])

a, b, c = best_fit_plane(co_mat)
print("a is :",a ,"b is :", b ,"c is :", c )
