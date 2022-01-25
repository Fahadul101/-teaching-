def repeat(list1): 
     d=dict()    
     l=[]        
     for i in list1:
          if i in d: 
               d[i]+=1 
          else:       
               d[i]=1 
     for i in d:  
          if d[i]>1:  
               l.append(d[i])
     for i in range(len(l)): 
          for j in range(len(l)):
               if i!=j and l[i]==l[j]: 
                    return True   
     else:                   
          return False
     
               
print(repeat([4,5,6,6,4,3,6,4]))
print(repeat([3,4,6,3,4,7,4,6,8,6,6]))