"""Python Homework #6 - Advanced Loops"""
import os

ts = os.get_terminal_size()
nWidth = ts.columns#rows
nHeight = ts.lines#columns

#print(nWidth)
#print(nHeight)

def drawBoard(row, column):
  if(column>nHeight or row>nWidth):
    return False
  else:
    for r in range (row):
      for c in range(column+1):
        print("| ", end="")
      print()  
      print("-"*column*2)
    return True

drawBoard(63, 33)
