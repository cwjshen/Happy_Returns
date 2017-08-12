# In this implementation, the image is represented by a 
# 2d array, where each pixel an index in the array.

# Each pixel is defined by an "x and y" or "row and column"
# The input of start_loc will be a tuple of x and y
from collections import deque

def flood_fill(img_matrix, start_loc, color):
	num_rows = len(img_matrix)
	num_cols = len(img_matrix[0])
	original_color = img_matrix[start_loc[0]][start_loc[1]]
	queue = deque([start_loc])


	while queue:
		print 'Queue: ', queue
		curr_pixel = queue.popleft()
		
		x = curr_pixel[0]
		y = curr_pixel[1]

		# Change current pixel to desired color
		img_matrix[x][y] = color

		# Add adjacent pixels to the queue only if:
		# 1) The adjacent pixel is within bounds of the matrix
		# 2) If the color of the adjacent pixel matches the original color

		# Top
		if y - 1 >= 0:
			if img_matrix[x][y-1] == original_color:
				queue.append((x, y-1))

		# Right
		if x + 1 <= num_cols:
			if img_matrix[x+1][y] == original_color:
				queue.append((x+1, y))

		# Bottom
		if y + 1 <= num_rows:
			if img_matrix[x][y+1] == original_color:
				queue.append((x, y+1))

		# Left
		if x - 1 >= 0:
			if img_matrix[x-1][y] == original_color:
				queue.append((x-1, y))

	return img_matrix

def main():
	img_matrix = [ ["G", "W", "G", "G"],
				   ["W", "W", "W", "G"],
				   ["G", "W", "W", "G"],
				   ["G", "G", "G", "W"] ]
	start_loc = (1,1)
	color = "R"

	print 'Before Fill:', img_matrix

	flood_fill(img_matrix, start_loc, color)

	print 'After Fill:', img_matrix

main()
