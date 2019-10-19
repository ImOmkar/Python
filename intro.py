import sys
sys.path.append('add you folder path here') # this is to check by moving your imported module and to access it
from my_module import *
import sys

courses = ['History','Math','Physics','CompSci']

index = find_index(courses, 'Math')
#print(index)
#print(test)

print(sys.path)