def addToList(l, m, p) :
  if(l.count(p) > 0):
    getRejected(m, p)
    return False
  else:
    l.append(p)
    return True

def getRejected(l,p):
  l.append(p)
