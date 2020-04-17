#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because we go through all the inputs once in a loop.


b) O(n^n) because you have two loops in the code.


c) O(n) because it's a recursion and is going down towards its base case.

## Exercise II

def broken_eggs(floor_number):
# establish base case
  if floor_number >= f:
    return 0
# going towards base case
  return 1 + broken_eggs(floor_number - 1)

  This is a recursive function and will return big O notation of O(n)


