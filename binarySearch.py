#values should be sorted like a dictionary
#lower bound and upper bound or 1st and last
#mid index = lower+upper/2 it is like finding a word in a dictioary


from traceback import print_tb


def search(arr,n):
    l =0
    u=len(arr)-1

    while l<=u:
        mid =(l+u)//2
        
        
        if arr[mid]== n:

            globals()['pos'] = mid

            return True

        else :
            if arr[mid]<n:
                l=mid

            else:
                u=mid
    
arr = [4,6,8,10,13,16,19,22,444,555,666]
n= 444
if search(arr , n):
    print('Found at' , pos)

else :
    print("Not found")


 

