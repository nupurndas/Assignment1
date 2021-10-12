def TowerOfHanoi(n , a, b, c):
    if n==1:
        print ("Move disk 1 from Tower : ", a ,"to Tower : ",b)
        return
    TowerOfHanoi(n-1, a, c, b)
    print ("Move disk",n,"from Tower : ", a ,"to Tower : ",b)
    TowerOfHanoi(n-1, c, b, a)
          
# Driver code
n =  int(input( "Enter number of disc : "))
TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods