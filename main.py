#!/usr/bin/python3

import re

def re_join(r1,r2):
    return rf"{r1}|{r2}"

def clean(s):

    # Remove project gutenberg extra text
    start_split = re.split(r"\*\*\* START OF THE PROJECT GUTENBERG [ A-Z]+ \*\*\*", s)
    s = start_split[1]
    end_split = re.split(r"\*\*\* END OF THE PROJECT GUTENBERG [ A-Z]+ \*\*\*", s)
    s = end_split[0]

    # Remove and convert various whitespace junk
    s = re.sub(r" {2,}", r"", s)             # 
    s = re.sub(r"([^\.])\n{2,}", r"\1. ", s)
    s = re.sub(r"[\n]+|[\r\n]+", r" ", s)

    clean = s
    return clean

def chapter_split(s):

    # This preserves strings like "H. W. McGee" or "Dr. Watson"
    # In other words, these periods are swapped with '#' so that they aren't
    # interpreted as sentence terminators
    s = re.sub(r"(?:(?<= [A-Z])|(?<=Mrs)|(?<=Mr)|(?<=Dr)|(?<=St))\. ", '# ', s)

    parts = re.split(r"(?i)chapter [ivx ]+", s)
    parts = [p for p in parts if p]
    chapter_chunks = [p for p in parts if len(p) > 200]
    chapters = [re.split(r"\. ", c) for c in chapter_chunks]

    for chapter_idx in range(len(chapters)):
        for sentence_idx in range(len(chapters[chapter_idx])):
            chapters[chapter_idx][sentence_idx] = re.sub(r"#", '.', chapters[chapter_idx][sentence_idx])

    return chapters 

with open("text/the_secret_adversary.txt", 'r') as file:
    content_raw = file.read()
    content = clean(content_raw)
    chapters = chapter_split(content)

    # The sign of the four
    # investigator = "Sherlock|Holmes"
    # assistant = "Watson"
    # perpetrator = "Tonga"
    # suspect = "Jonathan|Small"

    # A study in scarlet
    # investigator = "Sherlock|Holmes"
    # assistant = "Watson"
    # perpetrator = "Jefferson|Hope"
    # suspect = ""

    # The secret adversary
    investigator = "Tommy|Thomas|Beresford"
    assistant = "Tuppence|Prudence|Cowley"
    perpetrator = "Brown"
    # suspect = ""

    investigator_found = False
    assistant_found = False
    perpetrator_found = False
    suspect_found = False

    total_sentence_idx = 0
    for chapter_idx, chapter in enumerate(chapters):
        for sentence_idx, sentence in enumerate(chapter):
            total_sentence_idx += 1

            #print(f"{chapter_idx+1}/{sentence_idx}/{total_sentence_idx}:{sentence}")

            # Check for the investigator
            if investigator_found is False:
                investigator_matches = re.findall(rf"{investigator}", sentence)
                if len(investigator_matches) > 0:
                    investigator_found = True
                    print(f"Investigator {investigator} found "
                        + f"in chapter {chapter_idx+1} sentence {sentence_idx} ({total_sentence_idx})")

            # Check for the assisstant 
            if assistant_found is False:
                assistant_matches = re.findall(rf"{assistant}", sentence)
                if len(assistant_matches) > 0:
                    assistant_found = True
                    print(f"Assisstant {assistant} found "
                        + f"in chapter {chapter_idx+1} sentence {sentence_idx} ({total_sentence_idx})")

            # Check for the perpetrator
            if perpetrator_found is False:
                perpetrator_matches = re.findall(rf"{perpetrator}", sentence)
                if len(perpetrator_matches) > 0:
                    perpetrator_found = True
                    print(f"Perpetrator {perpetrator} found "
                        + f"in chapter {chapter_idx+1} sentence {sentence_idx} ({total_sentence_idx})")
                    
                    '''
            # Check for suspect
            if suspect_found is False:
                suspect_matches = re.findall(rf"{suspect}", sentence)
                if len(suspect_matches) > 0:
                    suspect_found = True
                    print(f"Suspect {suspect} found "
                        + f"in chapter {chapter_idx+1} sentence {sentence_idx} ({total_sentence_idx})")
                        '''


    quit()