"""
def boom(a,x,y,n):
    length=a[x-1][y-1]-1
    #print(x,y,length)
    top=max(x-length-1,0)
    bottom=min(x+length,n)
    left=max(y-length-1,0)
    right=min(y+length,n)
    #print("범위",top,bottom,left,right)
    for i in range(top,bottom):
        a[i][y-1]=0
    #a[x][bottom:top-1]=0
    for j in range(left,right):
        a[x-1][j]=0
    #a[left:right][y]=0
    return a
def drop(a, n):
    # Iterate from bottom to top and right to left to handle dropping elements
    for j in range(n):
        for i in range(n-1, 0, -1):
            if a[i][j] == 0:
                print(i,j,"현재위치 0")
                # Move elements down
                k = i
                while k > 0 and a[k][j] == 0:
                    #print(k,j)
                    a[k][j] = a[k-1][j]
                    a[k-1][j] = 0
                    k -= 1
                print()
    
    return a
n=int(input())
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
x,y=map(int,input().split())
a=boom(a,x,y,n)
a=drop(a,n)

for i in range(n):
    if(a[x+1][y]==0):
        a[]

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print('')

"""
def boom(a, x, y, n):
    """
    Simulates an explosion in a 2D grid and updates the grid accordingly.

    Args:
        a (list of lists): The 2D grid represented as a list of lists.
        x (int): The x-coordinate of the explosion center.
        y (int): The y-coordinate of the explosion center.
        n (int): The size of the grid (n x n).

    Returns:
        list of lists: The modified grid after the explosion.
    """

    length = a[x - 1][y - 1] - 1  # Calculate explosion length based on cell value
    top = max(x - length - 1, 0)  # Define top boundary
    bottom = min(x + length, n)  # Define bottom boundary
    left = max(y - length - 1, 0)  # Define left boundary
    right = min(y + length, n)  # Define right boundary

    # Apply explosion effect (set elements within range to 0)
    for i in range(top, bottom):
        a[i][y - 1] = 0
    for j in range(left, right):
        a[x - 1][j] = 0

    return a


def drop(a, n):
    """
    Simulates gravity by dropping elements in the grid.

    Args:
        a (list of lists): The 2D grid represented as a list of lists.
        n (int): The size of the grid (n x n).

    Returns:
        list of lists: The modified grid after applying gravity.
    """

    for j in range(n):  # Iterate from bottom to top
        for i in range(n - 1, 0, -1):  # Iterate from right to left
            if a[i][j] == 0:  # Check if current cell is empty
                k = i  # Initialize index to find non-zero element above
                while k > 0 and a[k][j] == 0:  # Search for non-zero element above
                    k -= 1  # Move index up

                if k >= 0:  # If non-zero element found
                    a[i][j] = a[k][j]  # Shift element down
                    a[k][j] = 0  # Set original position to empty

    return a


def main():
    n = int(input())  # Get grid size
    a = []  # Initialize empty grid

    for i in range(n):  # Read grid input
        row = list(map(int, input().split()))
        a.append(row)

    x, y = map(int, input().split())  # Get explosion center coordinates

    # Apply explosion and gravity
    a = boom(a, x, y, n)
    a = drop(a, n)

    # Print the modified grid
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()