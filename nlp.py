import re

#f = open("pg244.txt", "r", encoding="utf-8-sig")
f = open("pg1155.txt", "r", encoding="utf-8-sig")
#f = open("pg2097.txt", "r", encoding="utf-8-sig")

punc = '''()-[]{};:'"\,<>/@#$%^&*_~'''
new_sent_punc = ".!?"
line_number = 0
sent_number = 0
chapter = ""
sent = ""
#CapitalWords = []

class character:
  first_page = 0
  last_page = 0




for line in f:
    line_number+=1
    line = line.strip()#removes extra whitespace
    line = re.sub(r"[^\x00-\x7F]+", "", line)#removes non UTC characters
    
    try:
        

        #print(re.sub ('^[Cc][Hh][Aa][Pp][Tt][Ee][Rr]',"", line))
        
        searchResults = re.search('^[Cc][Hh][Aa][Pp][Tt][Ee][Rr]', line)
        print(searchResults.string)
        chapter = searchResults.string



        #print(line)
        #re.match('(?<=test :).*',text)
        #print(re.match('(?<=CHAPTER :).*',line))
        #chapter = line.split("CHAPTER",1)[1]
        #chapter = chapter.strip()
        #chapter = chapter.split(" ")[0]
    except:
        pass
    

    #looks for end of sentence punc
    for ele in line:
        if (ele not in new_sent_punc):
            sent = sent + ele
        else:
            #print (chapter + " : " + str(sent_number) + " : " + sent)
            sent_number = sent_number + 1
            sent = ""
    
    print ("Chapter: " + chapter + " line number: " + str(line_number) + " sent number: " + str(sent_number))
    print(sent)
    #print (words)
    #for ele in line:
    #    if ele in new_sent_punc:
    #        sent_number = sent_number + 1
    #        line = line.replace(ele, "")#removes punctuation



    #for ele in line:
    #    if ele in punc:
            #print(line)
    #        line = line.replace(ele, "")#removes punctuation   
            #print (ele)

    #words = line.split()
    #for word in words:
    #    properName = re.search("^[A-Z][a-z]", word)
    #    if (properName):
    #        properName = properName.string.lower()
    #        CapitalWords.append(properName)
        
        #print (line)

    #line = line.lower()#makes lowercase
    #for ele in line:
    #    if ele in punc:
    #        line = line.replace(ele, "")#removes punctuation
                     
            
    
        
        



#frequent_words_that_were_capitalized = {i:CapitalWords.count(i) for i in CapitalWords}

#frequent_words_that_were_capitalized = dict(sorted(frequent_words_that_were_capitalized.items(), key=lambda item: item[1]))



#pronoun_list = ["i", "you", "he", "she", "it", "we", "you", "they", "me", "you", "him", "her", "it", "us", "you", "them", "mine", "yours", "his", "hers", "its", "ours", "yours", "theirs", "this", "these", "that", 
#            "those", "who", "whom", "which", "what", "that", "whoever", "whichever", "whomever", "all", "another", "any", "anybody", "anyone", "anything", "each", "everybody", 
#            "everyone", "everything", "few", "many", "nobody", "none", "one", "several", "some", "somebody", "someone", "myself", "yourself", "himself", "herself", "ourselves", "yourselves", 
#            "themselves", "myself", "yourself", "himself", "herself", "ourselves", "yourselves", "themselves", "there"]

 
 
# Remove pronouns from frequent_words_that_were_capitalized
#for key in pronoun_list:
#    try:
#        del frequent_words_that_were_capitalized[key]
#    except:
#        pass#word not found, ignore

#article_list = ["a", "an", "the"]

#remove articles from frequent_words_that_were_capitalized
#for key in article_list:
#    try:
#        del frequent_words_that_were_capitalized[key]
#    except:
#        pass#word not found, ignore


#conjunction_list = ["and", "or", "but", "because", "for", "if", "and", "when"]
#remove conjunctions from frequent_words_that_were_capitalized
#for key in conjunction_list:
#    try:
#        del frequent_words_that_were_capitalized[key]
#    except:
#        pass#word not found, ignore

#https://www.espressoenglish.net/the-100-most-common-words-in-english/
#most_common_words = ["time","year","people","way","day","man","thing","woman","life","child","world","school","state","family","student","group","country","problem","hand","part","place","case","week","company","system",
#"program","question","work","government","number","night","point","home","water","room","mother","area","money","story","fact","month","lot","right","study","book","eye","job","word","business","issue","side","kind","head",
#"house","service","friend","father","power","hour","game","line","end","member","law","car","city","community","name","president","team","minute","idea","kid","body","information","back","parent","face","others","level","office",
#"door","health","person","art","war","history","party","result","change","morning","reason","research","girl","guy","moment","air","teacher","force","education"]

#for key in most_common_words:
#    try:
#        del frequent_words_that_were_capitalized[key]
#    except:
#        pass#word not found, ignore

#additional_words = ["audley","marguerite","would","janes","take","cross","holyhead","license","will","two","again","are","every","yard","south","mansions","supposing","bournemouth","had","have","quite","remember","adventurers","once",
#"moat","never","whittingtons","still","british","see","lets","paris","look","anyway","labour","scotland","soho","literary","archive","were","young","french","get","from","united","little","shall","england","let","hes","dr","hall","lusitania",
#"your","go","thank","was","danvers","say","cowley","did","weve","jamess","good","nothing","states","where","whats","juliuss","foundation","very","kramenin","perhaps","suddenly","come","rita","peel","edgerton","by","just","after","shes","is",
#"of","ritz","on","to","ah","youre","sure","russian","with","my","london","do","theres","why","tuppences","dont","not","german","boris","american","beresford","so","as","how","now","ill","at","id","miss","finn","oh",
#"thats","gutenberg","project","ive","carter","in","yes","well","then","no","","im","mrs","sir","mr"]

#for key in most_common_words:
#    try:
#        del frequent_words_that_were_capitalized[key]
#    except:
#        pass#word not found, ignore

#print (frequent_words_that_were_capitalized)