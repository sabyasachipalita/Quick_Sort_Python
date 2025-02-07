# def partition(a,low,high):
#             pivot=a[low]
#             i=low+1
#             j=high
#             while True:
#                     while i<=j and a[i]<=pivot:
#                             i+=1
#                     while(i<=j) and a[j]>pivot:  
#                             j=j-1
#                     if(i<=j):
#                             a[i],a[j]=a[j],a[i]
#                     else:
#                             break
#             a[low],a[j]=a[j],a[low]
#             return j

# def quick_sort(a,low,high):
#         if(low<=high):
#                 piv=partition(a,low,high)
#                 quick_sort(a,low,piv-1)
                
#                 quick_sort(a,piv+1,high)

# a=[2,1,4,3,6,5,8,7] 
# print("original array:",a)
# quick_sort(a,0,len(a)-1)
# print("sorted array",a)



#factorial of a number
# def fact(n):
#         if(n==0) or (n==1):
#                 return 1
#         else:
#                 return fact (n)*(n-1)
# print(fact(4))
# 
# 
# 
#fibonnaci series
# n=int(input("enter number:"))
# a=0
# b=1
# c=0

# def selection_sort(a):
#         n=len(a)
#         for i in range(n-1):
#                 mini=i
#                 for j in range(i+1,n):
#                         if a[j]<=a[mini]:
#                                 mini=j
#                                 a[i],a[mini]=a[mini],a[i]
#         return a        
# a=[2,1,4,3,6,5]
# print(selection_sort(a)) 
# import keyword
# print(keyword.kwlist)
# 
# n=int(input("enter number:"))
# def reverse(n):
#             s=str(n)
#             d=s[::-1]
#             return int(d)


# x=n**2
# y=reverse(n)**2
# if x==reverse(y):
#         print("adam number")
# else:
#         print("not")
# 
# 
# def bubble_sort(a):
#             n=len(a)
#             for i in range(n):
#                     swaped=True
#                     for j in range(0,n-i-1):
#                             if a[j]>=a[j+1]:
#                                     a[j],a[j+1]=a[j+1],a[j]
#                                     swaped=True
                                    
#                     if not swaped:
#                             break
# a=[2,1,4,3]
# bubble_sort(a)   
# print("sorted",a)
# def merge_sort(arr):
#             if len(arr)<=1:
#                     return arr
#             mid=len(arr)//2
#             left_arr=arr[:mid]
#             right_arr=arr[mid:]
#             left_arr=merge_sort(left_arr)
#             right_arr=merge_sort(right_arr)
#             return merge(left_arr,right_arr)

# def merge(left_arr,right_arr):
#         i=0
#         j=0
#         result=[]
#         while i<len(left_arr) and j<len(right_arr):
#                 if (left_arr[i]<=right_arr[j]):
#                         result.append(left_arr[i])
#                         i+=1
#                 else:
#                         result.append(right_arr[j])
#                         j+=1
#         result+=left_arr[i:]
#         result+=right_arr[j:]
#         return result

# a=[2,1,4,3,9,8,7,6,5]
# sorted=merge_sort(a)
# print(sorted) 
# 
# 
# list=[1,2,3,4,5]
# max_value=list[0]
# for num in list:
#             if num>max_value:
#                     max_value=num
# print("max",max_value) 
# sabyasachi palita
# selection_sort in python

# def selection_sort(a):
#             n=len(a)
#             for i in range(n-1):
#                     mini=i
#                     for j in range(i+1,n):
#                             if a[j]<=a[mini]:
#                                     mini=j
#                                     a[i],a[mini]=a[mini],a[i]
#             return a
# a=[2,1,4,3,7,5,6]
# selection_sort(a)
# print(selection_sort(a))
# 
# 
# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# if a == b:
#             print("t")
# else:
#         print("f") 
# 
                                    


                                          


            
            
                     
                                                


        
