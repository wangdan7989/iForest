import kmeans
pixels = [[(12,20,25),1],[(17,31,92),5],[(17,45,2),3],[(13,40,24),2]]
means = kmeans.kmeans(pixels,4)
print (means)

