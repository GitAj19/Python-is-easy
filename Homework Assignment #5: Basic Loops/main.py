"""Python Homework #5 - Basic Loops"""

for num in range(1, 101):
  sDivider = "NULL"
  nDivider = 1
  nOccurence = 0
  #multiples of 3
  if num%3 == 0:
    sDivider = "3"
  #multiples of 5
  if num%5 == 0:
    sDivider = "5"
  #multiples of 3 and 5
  if num%3 == 0 and num%5 ==0:
    sDivider = "3 and 5"
  #Prime finder
  while(nDivider <= num):
    if num%nDivider == 0:
      nOccurence = nOccurence + 1
    
    nDivider = nDivider + 1
  
  print("-------------")
  
  if (sDivider == "3"):
    print("Fizz")
  if (sDivider == "5"):
    print("Buzz")
  if (sDivider == "3 and 5"):
    print("FizzBuzz")

  if(nOccurence == 2):
    print("Prime")
  if (nOccurence != 2 and sDivider == "NULL"):
    print(num)
