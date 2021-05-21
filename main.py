import requests
import json



r=requests


# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
  
# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)
  
# printing result
print ("The combined sorted list is : " + str(res))
