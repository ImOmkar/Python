input1=input("Enter Sentence: \n")
ExcludedWords=['and','the','is','are','to','have','do','for','here','more','of']
a=input1.split()
count=0
for each in a:
    if each in ExcludedWords:
        count+=1
print("There are",count," excluded words in the sentence")
