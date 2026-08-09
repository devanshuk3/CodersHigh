i=0
j=0
count = 1

#right = (i+count, j)
#up = (i, j+count)
#count+=1
#left = (i-count, j)
#down = (i, j-count)

def right(i, j, count):
    print("R")
    return (i+count, j) 

def up(i,j,count):
    print("U")
    return(i, j+count)

def down(i, j ,count):
    print("D")
    return (i, j-count)

def left(i,j,count):
    print(f"FD {count}")
    return (i-count, j)

for count in range(10):
    #lt 90
    for i in range(count):
      right(i,j,count)
    #lt 90
    for i in range(count):
          up(i,j,count)
    count+=1
    #lt 90
    for i in range(count):
          left(i,j,count)
    #lt 90
    for i in range(count):
          down(i,j,count)