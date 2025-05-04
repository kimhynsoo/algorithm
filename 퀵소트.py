#전통적인 in-place 방식 O(NlogN)
# def quick_sort(arr,start,end):
#     if(start>=end):
#         return
#
#     pivot = start
#     left=start+1
#     right=end
#
#     while left<=right:
#         while left<=end and arr[left] <= arr[pivot]:
#             left+=1
#         while right>start and arr[right]>=arr[pivot]:
#             right-=1
#
#         if left>right:
#             arr[pivot],arr[right]=arr[right],arr[pivot]
#         else:
#             arr[left],arr[right]=arr[right],arr[left]
#
#     quick_sort(arr,start,right-1)
#     quick_sort(arr,right+1,end)

#시간 복잡도는 느리지만 (리스트를 계속 만들기에) 파이썬의 특징을 잘 활용한 퀵정렬
def quick_sort2(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    tail= arr[1:]
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)




array=[8,4,3,2,1,5,7,8,9]
#quick_sort(array,0,len(array)-1)
array=quick_sort2(array)

print(array)