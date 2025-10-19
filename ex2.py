import numpy as np  
arr1 = np.array([1, 2, 3])
print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1[2])
arr1[2] = 5
print(arr1)
arr2 = np.array([[1,2,3],[3,4,5]])
print(arr2)
print(arr2.shape)
print(arr2[1][2])
print(arr2[1,2])
print(arr2[1][-2])
arrs = np.array(['China','USA','Sri Lanka'])
print(arrs)
arrR = np.arange(0,20,2)
print(arrR)
arrL = np.linspace(0,10,20)
print(arrL)
arr = np.random.rand(10)
print(arr)
arr = np.random.randn(3,4)
print(arr)
print(np.zeros(10))
print('/n')
print(np.zeros((2,3)))
print(np.ones((10,10)))
arr= ([1,2,3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))
identify_matrix = np.eye(3)
print(identify_matrix)
arr = np.diag([1,2,3,4,5])
print(arr)
arr = np.random.rand(5,5)
print(arr)
print(np.diag(arr))
print(arr.ndim)
print(arr.shape)
print(np.random.randint(-10,10,4))
print(arr+10)
print(arr-10)
print(arr/2)
print('/n')
print(np.exp(arr))
print('/n')
print(arr)
print('/n')
print(np.log(arr))
print('/n')
print(np.log2(arr))
print('/n')
print(np.sin(arr))
print('/n')
print(np.sum(arr))
print('/n')
print(np.sum(arr ,axis=0))  # sum along columns
print(np.sum(arr ,axis=1))  # sum along rows
print('/n')
print(np.min(arr))
print(np.min(arr, axis=0))  # min along columns
print(np.min(arr, axis=1))  # min along rows
print('/n')
print(np.max(arr))
print(np.max(arr, axis=0))  # max along columns
print(np.max(arr, axis=1))  # max along rows
print('/n')
print(np.mean(arr))
print(np.mean(arr, axis=0))  # mean along columns
print(np.mean(arr, axis=1))  # mean along rows
print('/n')
print(np.median(arr))   # median of the entire array        
print(np.median(arr, axis=0))  # median along columns
print(np.median(arr, axis=1))  # median along rows
print('/n')
print(np.std(arr))  # standard deviation of the entire array
print(np.std(arr, axis=0))  # std along columns
print(np.std(arr, axis=1))  # std along rows    
print('/n')
print(np.var(arr))  # variance of the entire array
print(np.var(arr, axis=0))  # variance along columns
print(np.var(arr, axis=1))  # variance along rows
print('/n')
print(arr[1:,2:3])  # slicing the array
print(arr[1:,2:-1])  # slicing the array
print('/n')
print(np.sort(arr) )# sorting the entire array
print('/n')
print(np.sort(arr, axis=0))  # sorting along columns
print('/n')
print(np.sort(arr, axis=1))  # sorting along rows
print('/n')
print(arr)
print('/n')
print(arr.T)  # transpose of the array
print('/n')
print(arr[:3,:])
print('/n')
print(arr[:3,:].T)
print('/n')
print(arr[:3,:].flatten())  # flattening the array
arr = np.array([4,5,6,7,8])
print(arr)
arr1 = np.append(arr, 8) # appending an element
print(arr1)
arr2 = np.insert(arr, 0, [1,2,3])
print(arr2)  # inserting elements at the beginning
arr3 = np.delete(arr2,0)
print(arr3)  # deleting the first element
arr3 = np.delete(arr2,[1,3])
print(arr3)  # deleting the second and fourth elements
arrC = arr3.copy()  # copying the array
print(arrC)  # printing the copied array
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr2 = np.array([[5,6,7,8],[5,6,7,8]])
arr_cat = np.concatenate((arr1, arr2), axis=0)  # concatenating along rows
print(arr_cat)  # printing the concatenated array
print('/n')
arr_cat = np.concatenate((arr1, arr2), axis=1)  # concatenating along columns
print(arr_cat)  # printing the concatenated array
print('/n')
catV = np.vstack((arr1, arr2))  # vertical stacking
print('/n')
print(catV)  # printing the vertically stacked array
catH = np.hstack((arr1, arr2))  # horizontal stacking
print('/n') 
print(catH)  # printing the horizontally stacked array
print('/n')
arr = np.array([1,2,3,4,5,6,3,6,1,2,4])
print(np.unique(arr) ) # finding unique elements in the array
uniqes, counts = np.unique(arr, return_counts=True)  # finding unique elements and their counts
print(uniqes)  # printing unique elements       
print(counts)  # printing counts of unique elements
print('/n')
# intersection, differentiation, neither
arr1 = np.array([1,2,3,4,5])
arr2= np.array([3,4,5,6,7])
print(np.intersect1d(arr1, arr2) ) # intersection of two arrays
print(np.union1d(arr1, arr2) ) # union of two arrays
print(np.setdiff1d(arr1,arr2)) # elements in arr1 not in arr2
print(np.setxor1d(arr1, arr2)) # elements in either arr1 or arr2 but not both