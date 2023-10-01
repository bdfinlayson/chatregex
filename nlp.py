import re

#f = open("pg244.txt", "r", encoding="utf-8-sig")
f = open("pg1155.txt", "r", encoding="utf-8-sig")
#f = open("pg2097.txt", "r", encoding="utf-8-sig")

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
line_number = 0

chapter = ""
CapitalWords = []

for line in f:
    line_number+=1
    line = line.strip()#removes extra whitespace
    line = re.sub(r"[^\x00-\x7F]+", "", line)#removes non UTC characters
    
    #print (words)
    for ele in line:
        if ele in punc:
            print(line)
            line = line.replace(ele, "")#removes punctuation   
            print (ele)

    words = line.split()
    for word in words:
        properName = re.search("^[A-Z][a-z]", word)
        if (properName):
            properName = properName.string.lower()
            CapitalWords.append(properName)
        
        #print (line)

    line = line.lower()#makes lowercase
    for ele in line:
        if ele in punc:
            line = line.replace(ele, "")#removes punctuation         
            
    try:
        
        chapter = line.split("chapter",1)[1]
        chapter = chapter.strip()
        chapter = chapter.split(" ")[0]
        
        
    except:
        pass
    print (chapter + " : " + str(line_number) + " : " + line)


frequent_words_that_were_capitalized = {i:CapitalWords.count(i) for i in CapitalWords}

frequent_words_that_were_capitalized = dict(sorted(frequent_words_that_were_capitalized.items(), key=lambda item: item[1]))


pronoun_list = ["i", "you", "he", "she", "it", "we", "you", "they", "me", "you", "him", "her", "it", "us", "you", "them", "mine", "yours", "his", "hers", "its", "ours", "yours", "theirs", "this", "these", "that", 
            "those", "who", "whom", "which", "what", "that", "whoever", "whichever", "whomever", "all", "another", "any", "anybody", "anyone", "anything", "each", "everybody", 
            "everyone", "everything", "few", "many", "nobody", "none", "one", "several", "some", "somebody", "someone", "myself", "yourself", "himself", "herself", "ourselves", "yourselves", 
            "themselves", "myself", "yourself", "himself", "herself", "ourselves", "yourselves", "themselves", "there"]

 
 
# Remove pronouns from frequent_words_that_were_capitalized
for key in pronoun_list:
    try:
        del frequent_words_that_were_capitalized[key]
    except:
        pass#word not found, ignore

article_list = ["a", "an", "the"]

#remove articles from frequent_words_that_were_capitalized
for key in article_list:
    try:
        del frequent_words_that_were_capitalized[key]
    except:
        pass#word not found, ignore


conjunction_list = ["and", "or", "but", "because", "for", "if", "and", "when"]
#remove conjunctions from frequent_words_that_were_capitalized
for key in conjunction_list:
    try:
        del frequent_words_that_were_capitalized[key]
    except:
        pass#word not found, ignore

print (frequent_words_that_were_capitalized)