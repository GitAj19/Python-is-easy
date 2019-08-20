"""Python Homework #7 - Dictionaries and Sets"""

def guessTheValue(key, value):
  if key in SongDet and str(SongDet[key]) == value:
     return True
  else:
    return False

SongDet = {"Song Name":"Am I Wrong", "Genere":"Pop", "Released Date":"April 12, 2013",
           "Album":"Black Star Elephant", "Artist":"Nico & Vinz", "Producers":"William Wiik Larsen", "Duration":4.07, "Nominations":"\tSpellemann Award for Hit of the Year - 2014\n\t\t\t\tSoul Train Music Award for Best International Performance - 2014\n\t\t\t\tBillboard Music Award for Top Radio Song - 2015",
           "Url":"https://www.youtube.com/watch?v=bg1sT4ILG0w",
           "Song Writers":"William Wiik Larsen, Nico Sereba, Vincent Dery, Abdoulie Jallow"}

for key in SongDet:
  print(key, end=" : ")
  print(SongDet[key])
  print()

while(True):
  iKey = str(input("Input Key: "))
  iValue = str(input("Input Value: "))
  print(guessTheValue(iKey, iValue))
  if(iKey == ""):
    break
