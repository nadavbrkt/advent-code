
mov = [(x, y) for x in range(-1,2) for y in range(-1,2) if not x == y == 0]

def create_new_ring(arr):
	width = len(arr)
	new_arr = [[None] + x + [None] for x in arr]
	new_arr = [([None] * (width + 2))] + new_arr + [([None] * (width + 2))]
	return new_arr
	
def get_node_val(x, y, arr):
	val = 0
	for m in mov:
		if ( (x + m[0] < len(arr[0])) and (x + m[0] >= 0) ) and \
		   ( (y + m[1] < len(arr)) and (y + m[1] >= 0) ):
			if arr[x + m[0]][y + m[1]] is not None:
				val += 	arr[x + m[0]][y + m[1]]
	return val

	