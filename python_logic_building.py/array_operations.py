arr = [10,23,5,23,1,2]

#print largest no in array
print("maximum no in an array is ",max(arr))

#print second largest no in array
arr.sort()
print("second maximum no in an array is ",arr[-2])

#print smallest no in array
print("smallest no in an array is ",min(arr))

#sum of all elements in array
print("sum of array elements ",sum(arr))

#sort the array
arr.sort()
print("sorted array ",arr)

#reverse the array
arr.reverse()
print("array reverse ",arr)

#count the no of elements in array
print("Length of array elements ",len(arr))

#count the duplicate no in array
dup = []
for i in arr:
    if arr.count(i)>1 and i not in dup:
        dup.append(i)
print("duplicate value",dup)
