def partition(a,low,high):
            pivot=a[low]
            i=low+1
            j=high
            while True:
                    while i<=j and a[i]<=pivot:
                            i+=1
                    while(i<=j) and a[j]>pivot:  
                            j=j-1
                    if(i<=j):
                            a[i],a[j]=a[j],a[i]
                    else:
                            break
            a[low],a[j]=a[j],a[low]
            return j

def quick_sort(a,low,high):
        if(low<=high):
                piv=partition(a,low,high)
                quick_sort(a,low,piv-1)
                
                quick_sort(a,piv+1,high)

a=[2,1,4,3,6,5,8,7] 
print("original array:",a)
quick_sort(a,0,len(a)-1)
print("sorted array",a)











                                  


                                          


            
            
                     
                                                


        
