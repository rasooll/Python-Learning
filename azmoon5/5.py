def multiplication_table(n):
	out_list=[]
	start_zarb = 1
	while start_zarb <= n:
		row_list=[start_zarb]
		row_zarb = 1
		while row_zarb < n:
			row_list.append(int(row_list[-1])+start_zarb)
			row_zarb = row_zarb + 1
		out_list.append(row_list)
		start_zarb = start_zarb + 1
	return out_list
print(multiplication_table(6))