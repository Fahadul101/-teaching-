def where_is_splitpoint(arr , n):
         
        lsum = 0
        
        for i in range(0 , n):
                lsum += arr[i]
                
                rsum = 0
                
                for j in range(i + 1 , n):
                        
                        rsum += arr[j]
                        
                if (lsum == rsum):
                        
                        return i+1
                        
        return -1
        
def Twoparts(arr , n):
        
        splittingpoints = where_is_splitpoint(arr , n)
        
        if (splittingpoints == -1 or splittingpoints == n):
                
                print("false")
                return
                
        else:
                print("true")


arr = list(map(int , input().split()))
n = len(arr)                
Twoparts(arr , n)