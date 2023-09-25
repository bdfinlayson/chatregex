## 1. Description
This project requires analyzing famous crime novels' plots, settings, and protagonist/antagonist relationships. Specifically, you will implement this analysis in a chatbot manner.

For this project, you will analyze three publicly available crime novels/stories by famous crime novelists that will be assigned to your team shortly after all project groups have been established. You can find novels at the Project Gutenberg site: http://www.gutenberg.org/.Links to an external site.

All project functions must be implemented via regular expressions (Python's re package) and Python only (version 3.10).

## 2. Implementation
Your project will have three main parts. Namely, prompts processing, analysis, and results production. 

### 2.1 Prompts
Everything on this project will be executed and presented through natural language prompts. You have significant freedom in how you will implement promot-based interaction. Here are some rules you will need to follow:

You will use the prompt to ask ChatRegex to produce the analysis outlined in 2.2, questions 1-7. You will ask ChatRegex those questions, and you should produce precise results and in natural, well-structured English. For the prompts, try to allow flexibility in asking questions. For example, do not hardcode exact strings from questions 2.2, 1-7. Allow for prompts asking "Describe when the ..." and direct questions "When the ..." or more personal "Tell me when the ...".

For all of this, you can only use regex from Python and the packages available in Python 3.10. 

### 2.2 Novel Analysis to be Performed
This project aims to analyze the frequency of occurrence of the protagonists and the perpetrator(s) across the novel - per chapter and per sentence in a chapter, the mention of the crime and other circumstances surrounding the antagonists. The ultimate objective is to use basic NLP tools to observe any patterns in plot structures across the works of one or all authors.  

Specifically, for this project, you are to analyze and report on: 

- When does the investigator (or a pair) occur for the first time -  chapter #, the sentence(s) # in a chapter,
- When is the crime first mentioned - the type of the crime and the details -  chapter #, the sentence(s) # in a chapter,
- When is the perpetrator first mentioned - chapter #, the sentence(s) # in a chapter,
- What are the three words that occur around the perpetrator on each mention (i.e., the three words preceding and the three words following the mention of a perpetrator),
- When and how the detective/detectives and the perpetrators co-occur - chapter #, the sentence(s) # in a chapter,
- When are other suspects first introduced - chapter #, the sentence(s) # in a chapter
To effectively conduct this analysis, you should find resources and read the plot summaries of each novel so you can make your search more effective. If plot summaries are unavailable, use regex to search for clues and report how well/fast that approach worked.

Feel free to use any background resource to understand the plot, protagonist and antagonist names, and other details. Look for spoilers, details, etc. Our goal is not to predict the crime blindly, but to computationally analyze the plot structure to see if the outcomes could be predicted computationally.

### 2.3 Results Production
The analysis results in 2.2 should be generated as natural text describing the results, as if you are interacting with a human investigator. 

You will ask ChatRegex the questions from 2.1, which should produce good, natural English results. 

The Deliverable and Implementation Logistics
Use only Python regular expressions and built-in Python libraries to implement the project.

In your report, describe your findings focusing on a) design choices for implementation, b) findings, and c) challenges you encountered, including implementation of prompt processor and regex-based analysis concerning your novels. 

Report everything in a 2-page long report (maximum), excluding references. Use proper, grammatically correct, and clear academic English. 

Submit a zip with a PDF of a report, presentation, and the source code. 

Be ready to present in the class - 10-minute presentation + 2 min Q&A. Video submission is acceptable if you are 100% off campus, asynchronous project. Send the video as a link to an accessible file. 

## Submission
Submit a zip with a pdf of a report, presentation, and the source code are due on Sunday before the class. 

## Grading
50% - technical implementation

50% - presentation of the findings and a write-up.  

## Due Date 
October 15th, 2023 11:59 PM EST for the submission.

October 16th, 2023 6:00 PM EST for the live/video of the presentation. 

## Project Organization
You will work on a team of 3-4-person projects. There should be a single project manager for the project.

## Support and Expectations
Project managers will be responsible for communication with the instructor and the timely delivery of the report, the code, and the presentation.  I will offer help on any topic you need. This is an investigative project. 