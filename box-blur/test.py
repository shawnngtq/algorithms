def boxBlur(image):

  r = []
  for i in range(len(image)-2):
    r.append([])
    for j in range(len(image[0])-2):
      r[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
  return r


image = [[1,1,1], [1,7,1], [1,1,1]]
boxBlur(image)
image = [[0,18,9], [27,9,0], [81,63,45]]
boxBlur(image)
image = [[36,0,18,9], [27,54,9,0], [81,63,72,45]]
boxBlur(image)
image = [[7,4,0,1], [5,6,2,2], [6,10,7,8], [1,4,2,0]]
boxBlur(image)
image = [[36,0,18,9,9,45,27], [27,0,54,9,0,63,90], [81,63,72,45,18,27,0], [0,0,9,81,27,18,45], [45,45,27,27,90,81,72], [45,18,9,0,9,18,45], [27,81,36,63,63,72,81]]
boxBlur(image)
