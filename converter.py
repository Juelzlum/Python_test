def lbsToKg(weight) : 
    return weight * 0.45

def kgToLbs(weight) : 
    return weight /0.45

def findMax (arr) : 
  max = arr[0]
  for x in arr: 
    if x > max: 
      max = x 
  return max 