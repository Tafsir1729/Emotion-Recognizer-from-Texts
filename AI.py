import csv
from collections import Counter

def wordSplitter(sentence):   #takes a list of sentences as input, outputs a list of seperated words
    tempStringOne=""
    tempStringOne = ' '.join(map(str, sentence)) # convert from list to string
    tempStringTwo = tempStringOne.split(".")  # split by dots
    tempStringOne = "".join(tempStringTwo)  # again join to remove dots
    strtt = tempStringOne.lower()  # lower casing the string
    wordList = list(strtt.split(" "))  #convert the string into list
    return wordList

def wordCounter(inputList):
    # Finding count of each element
    list_freq = (Counter(inputList))
    for key, value in list_freq.items():
        #print(key, "  ", value)
        keyArr.append(key)
        valueArr.append(value)

keyArr = []
valueArr = []

test=[]
frequencyCat=[]
frequencySent=[]

sentenceJoy=[]
sentenceFear=[]
sentenceDanger=[]
sentenceSadness=[]
sentenceDisgust=[]
sentenceShame=[]
sentenceGuilt=[]

uniqueWords=[]

count=1;
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        try:
            if line_count == -1:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if len(row[0]) < 11:
                    frequencyCat.append(row[0].strip())  #if row[0].strip() not in frequencyCat: pushes unique val
                    frequencySent.append(row[1].strip())
                #print(f'\t{row[0]} , {row[1]} ')
                line_count += 1
        except:
            print("")

i=0
for x in frequencyCat:
    if "joy" in x:
        sentenceJoy.append(frequencySent[i])  #holds the sentence that is categorized as joy emotion
    elif "fear" in x:
        sentenceFear.append(frequencySent[i])  #holds the sentence that is categorized as fear emotion
    elif "danger" in x:
        sentenceDanger.append(frequencySent[i])  #holds the sentence that is categorized as danger emotion
    elif "sadness" in x:
        sentenceSadness.append(frequencySent[i])  #holds the sentence that is categorized as sad emotion
    elif "disgust" in x:
        sentenceDisgust.append(frequencySent[i])  #holds the sentence that is categorized as disgust emotion
    elif "shame" in x:
        sentenceShame.append(frequencySent[i])  #holds the sentence that is categorized as shame emotion
    elif "guilt" in x:
        sentenceGuilt.append(frequencySent[i])  #holds the sentence that is categorized as guilt emotion
    i=i+1

allSplittedWords=wordSplitter(frequencySent)

allSplittedWordsJoy=wordSplitter(sentenceJoy)
allSplittedWordsFear=wordSplitter(sentenceFear)
allSplittedWordsDanger=wordSplitter(sentenceDanger)
allSplittedWordsSadness=wordSplitter(sentenceSadness)
allSplittedWordsDisgust=wordSplitter(sentenceDisgust)
allSplittedWordsShame=wordSplitter(sentenceShame)
allSplittedWordsGuilt=wordSplitter(sentenceGuilt)

wordCounter(allSplittedWords)  #call it to count elements of the list
mainKeyArr=keyArr  #holds the word
mainValArr=valueArr #holds the correspondent words frequency
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsJoy)  #call it to count elements of the list
joyKeyArr=keyArr
joyValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsFear)  #call it to count elements of the list
fearKeyArr=keyArr
fearValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsDanger)  #call it to count elements of the list
dangerKeyArr=keyArr
dangerValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsSadness)  #call it to count elements of the list
sadnessKeyArr=keyArr
sadnessValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsDisgust)  #call it to count elements of the list
disgustKeyArr=keyArr
disgustValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsShame)  #call it to count elements of the list
shameKeyArr=keyArr
shameValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

wordCounter(allSplittedWordsGuilt)  #call it to count elements of the list
guiltKeyArr=keyArr
guiltValArr=valueArr
keyArr=[]  #always empty this global var after calling "wordCounter"
valueArr=[]  #always empty this global var after calling "wordCounter"

dataDictionary = {}
dataDictionaryArray=[]
count=0

for x in mainKeyArr:
    dataDictionary["word"] = x
    indexVar = mainKeyArr.index(x)
    dataDictionary["frequency"] = mainValArr[indexVar]

    if x in joyKeyArr:   #counting how many times a word appear in joy category
        indexVar = joyKeyArr.index(x)
        dataDictionary["frequencyJoy"] = joyValArr[indexVar]
    else:
        dataDictionary["frequencyJoy"] = 0

    if x in fearKeyArr:  #counting how many times a word appear in fear category
        indexVar = fearKeyArr.index(x)
        dataDictionary["frequencyFear"] = fearValArr[indexVar]
    else:
        dataDictionary["frequencyFear"] = 0

    if x in dangerKeyArr:  #counting how many times a word appear in danger category
        indexVar = dangerKeyArr.index(x)
        dataDictionary["frequencyDanger"] = dangerValArr[indexVar]
    else:
        dataDictionary["frequencyDanger"] = 0

    if x in sadnessKeyArr:  #counting how many times a word appear in sadness category
        indexVar = sadnessKeyArr.index(x)
        dataDictionary["frequencySadness"] = sadnessValArr[indexVar]
    else:
        dataDictionary["frequencySadness"] = 0

    if x in disgustKeyArr:  #counting how many times a word appear in disgust category
        indexVar = disgustKeyArr.index(x)
        dataDictionary["frequencyDisgust"] = disgustValArr[indexVar]
    else:
        dataDictionary["frequencyDisgust"] = 0

    if x in shameKeyArr:  #counting how many times a word appear in shame category
        indexVar = shameKeyArr.index(x)
        dataDictionary["frequencyShame"] = shameValArr[indexVar]
    else:
        dataDictionary["frequencyShame"] = 0

    if x in guiltKeyArr:  #counting how many times a word appear in guilt category
        indexVar = guiltKeyArr.index(x)
        dataDictionary["frequencyGuilt"] = guiltValArr[indexVar]
    else:
        dataDictionary["frequencyGuilt"] = 0

    dataDictionaryArray.append(dataDictionary)   #create an array "list" of the dictionary
    dataDictionary={}   #empty the dictinary

while(1):
    val = input("Enter your sentence: ")
    strtt = val.lower()  # lower casing the string
    wordList = list(strtt.split(" "))  #convert the string into list

    freqJoy = 0
    freqFear = 0
    freqDanger = 0
    freqSadness = 0
    freqDisgust = 0
    freqShame = 0
    freqGuilt = 0

    hashList=[]
    hashTable={}

    for x in wordList:
        for d in dataDictionaryArray:  # "d" is a variable, "nba_players" is the array
            if d["word"] == x:
                hashTable["word"]=x
                #print("The word is: " + d["word"])
                #print("frequency is: " + str(d["frequency"]))
                #print("frequency joy is: " + str(d["frequencyJoy"]))
                #print("frequency fear is: " + str(d["frequencyFear"]))
                #print("frequency danger is: " + str(d["frequencyDanger"]))
                #print("frequency sadness is: " + str(d["frequencySadness"]))
                #print("frequency disgust is: " + str(d["frequencyDisgust"]))
                #print("frequency shame is: " + str(d["frequencyShame"]))
                #print("frequency guilt is: " + str(d["frequencyGuilt"]))
                freqJoy= freqJoy+float(d["frequencyJoy"]/d["frequency"])
                freqFear = freqFear+float(d["frequencyFear"] / d["frequency"])
                freqDanger = freqDanger+float(d["frequencyDanger"] / d["frequency"])
                freqSadness= freqSadness+float(d["frequencySadness"] / d["frequency"])
                freqDisgust = freqDisgust+float(d["frequencyDisgust"] / d["frequency"])
                freqShame = freqShame+float(d["frequencyShame"] / d["frequency"])
                freqGuilt = freqGuilt+float(d["frequencyGuilt"] / d["frequency"])

                hashTable["freqJoy"]=float(d["frequencyJoy"]/d["frequency"])
                hashTable["freqFear"]=float(d["frequencyFear"] / d["frequency"])
                hashTable["freqDanger"]=float(d["frequencyDanger"] / d["frequency"])
                hashTable["freqSadness"]=float(d["frequencySadness"] / d["frequency"])
                hashTable["freqDisgust"]=float(d["frequencyDisgust"] / d["frequency"])
                hashTable["freqShame"]=float(d["frequencyShame"] / d["frequency"])
                hashTable["freqGuilt"]=float(d["frequencyGuilt"] / d["frequency"])

                hashList.append(hashTable)
                hashTable={}

    total=freqJoy+freqFear+freqDanger+freqSadness+freqDisgust+freqShame+freqGuilt

    print("JOY : ",round((freqJoy/total)*100.0,2),"%")
    print("FEAR : ",round((freqFear/total)*100.0,2),"%")
    print("DANGER : ",round((freqDanger/total)*100.0,2),"%")
    print("SADNESS : ",round((freqSadness/total)*100.0,2),"%")
    print("DISGUST : ",round((freqDisgust/total)*100.0,2),"%")
    print("SHAME : ",round((freqShame/total)*100.0,2),"%")
    print("GUILT : ",round((freqGuilt/total)*100.0,2),"%")

    if(val=="exit"):
        break



