""" 
DESCRIPTION:
A matrix is "fat" when the sum of the roots of its "Widths" is greater than the sum of the roots of its "Heights". 
Otherwise, we call it as a "thin" matrix.

But what is the meaning of that?

A Width of a matrix is the sum of all the elements in a row.
Similarly, a Height of a matrix is the sum of all the elements in a column.

Difficult to assimilate? Let's look at an example.

1. The matrix [ [1, 3] , 
                [5, 7] ] :
  - Sum of rooted Widths:  √(1+3) + √(5+7) = √4 + √12
  - Sum of rooted Heights: √(1+5) + √(3+7) = √6 + √10
  
Since "width" is smaller than "height", we determine this matrix is "thin".

2. The matrix [ [1, 4, 7], 
                [2, 5, 8], 
                [3, 6, 9] ] :
  - Sum of rooted Widths:  √(1+4+7) + √(2+5+8) + √(3+6+9) = √12 + √15 + √18  = 11.57972565...
  - Sum of rooted Heights: √(1+2+3) + √(4+5+6) + √(7+8+9) = √6  + √15 + √24  = 11.22145257...
  
Since "height" is smaller than "width", we determine this matrix is "fat".

TASK: Your task is to return "thin", "fat" or "perfect" depending on the results obtained.

NOTES:
  - All matrices will be squared
  - In case that both sums are equal, the matrix will be considered as "perfect".
  - DON'T round the roots... every digit matters ;)
  - Since the results of the roots may have a slight variation, to determine that a matrix is "perfect", I suggest you use an approximate error of 1E- 10.
  - If a Width or a Height is negative, return None
"""

import math

def thin_or_fat(matrix: list[list[int]]) -> str | None:
    widths = [sum(row) for row in matrix]
    heights = [sum(matrix[row][col] 
                  for row in range(len(matrix))) 
                  for col in range(len(matrix))]

    if any(total < 0 for total in widths + heights):
        return None

    rooted_widths = sum(math.sqrt(width) for width in widths)
    rooted_heights = sum(math.sqrt(height) for height in heights)

    if math.isclose(rooted_widths, rooted_heights, abs_tol=1e-10):
        return "perfect"
    return "fat" if rooted_widths > rooted_heights else "thin"


print(thin_or_fat([[1, 3], [5, 7]]))
print(thin_or_fat([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))