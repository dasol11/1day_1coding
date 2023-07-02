#     * 41
#    *** 33
#   *****25 
#  *******17
# *********09
#  ******* 5 6    7
#   *****  5 7    5
#    ***   5 8
#     *
n = int(input())
for i in range(1, 2*n):
    if i <= n :
        print(" "*(n-i),end="")
        print("*"*(2*i-1))
    else:
        print(" "*(i-n),end="")
        print("*"*(4*n-2*i-1))