#Python program to print the most frequent words in a text file.
frequent_word = ""
frequency = 0 
words = []
chkd=[]
file = open("sample.txt","r")
for line in file:
    line_word = line.lower().replace(',','').replace('.','').split(" ")
    for w in line_word: 
        words.append(w)
for i in range( len(words)):
  if words[i] in chkd :
    continue
  chkd.append(words[i])
  count=words.count(words[i])
  if(count > frequency):
   frequency = count
   frequent_word = words[i]
print("Most repeated word is " + frequent_word + " ","\nFrequency : ",frequency)
file.close()
