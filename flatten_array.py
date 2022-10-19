'''Write an algorithm to flatten a multi-dimensional array:

```
vec = [[1,2,3], [4,5,6], [7,8,9]]
=> [1,2,3,4,5,6,7,8,9]
```
'''
def flatten_array(arr, res=[]):
    for i in range(0, len(arr)):
        if isinstance(arr[i], list):
            flatten_array(arr[i], res)
        else:
            res.append(arr[i])
    return res
vec = [[1,2,3], [4,5,6], [7,8,9]]
arr = [1, 2, [3, 4], [5, 6], 7]
arr2 = [1, [2, [3, [4, [5]]], 6, [7]]]
# print(flatten_array(vec))
print(flatten_array(arr2))