# NLP_Portfolio

One of the fastest growing fields in Computer Science and Artificial Intelligence is NLP. Almost every top company in the world uses NLP to some extent whether it's something as simple as classifying spam in company emails all the way to building fully function chatbots that can converse with humans in a fully organic way. The main goal of this portfolio was to not only allow for me to learn and better understand the field of NLP, but to hone my skills as an engineer. This portfolio showcases skills such as utilizing regex, lemmatizing words with NLTK, using Wordnet and similarity metrics, how to work with N-grams, web crawling and tokeninizing the data, classifying text using different models, and even building out a full functioning chatbot. Due to the nature of how fast this field is growing it is almost imperative that I continue to learn and develop my NLP skills that can help me land a profession in which I can work with cutting edge and state of the art NLP technology. The way to accomplish this goal is to not only further build and work with new NLP tools, but to also stay up to date with resources such as the ACL to see if there are any new developments in the field. The hope is that this portfolio continues to grow either in the ways of new projects being added or existing projects being refined and further developed as I continue along with my career. I hope that you enjoy the projects in this portfolio as much as I enjoyed creating them.

## Portfolio 0

This is an introduction into NLP and how my interests align with the field. You can see the [Overview of NLP here](Overview_of_NLP.pdf).

## Homework 1

This program takes in data and processes the text to make it readable and presentable using regex. After the data is processed it is then presented to the user. You can see the [file here](Homework1).

## Homework 2

This program takes in a file and collects the 50 most common words out of the text and then allows the user to play a guess game where they try to guess the word. The program utilizes nltk to lemmatize each word and allow for each word to be unique. It also allows us to calculate what words are nouns and use those words as the main portion of the guessing game. You can see the [file here](Homework2).

## Homework 3

This file looks into the use of WordNet and some of the other tools associated with it such as Lesk algorithm, Wu Palmer, SentiWordNet, Collocations and many other tools. This file was originally a google colab notebook, but was converted into a pdf and uploaded here. You can see the [file here](Homework3_Dxt180017ipynb.pdf).

## Homework 4

This program looks into the use of N-Grams as well as using other tools and metrics to calculate accuracies. The program takes in different languages and 
runs them as different N-Gram models as both bigrams and unigrams. From there the program runs a laplace formula to figure out what language the test sentence is going to be based off of the bank of bigrams and unigrams. You can see the [file here](Homework4).

## Homework 5

This program uses a web crawler to scrape different websites information on Lionel Messi. The web crawler looks through a starter site then looks at different links and routing pages from there until it comes up with 15 relevant URL sites. Once the websites have been found, the information on the website is scraped and stored in different text files. From there, the websites sentences are tokenized and later the top 25 terms are found. From there we manually selected the top values and created a knowledge base using this data. The knowledge base is later used for a chatbot. You can see the [file here](Homework5).

## Parsing Sentences

This paper takes a look at different parsing techniques on a sentence created by me. The different parsing techniques that were used were PSG parsing tree, Dependency Parsing and Semantic Role Labeling. Along with this I give my thoughts on pros and cons of the different techniques. You can see the [file here](Parsing-Sentences.pdf).

## Text Classification 1

This program takes a look into using different Sklearn libraries to classify different forms of text. The data that was used for this program was a dataset about rotten tomatoes reviews from Kaggle. Each review was given a rating of a 1 or a 0 with 1 indicating that it was a positive review and 0 indicating that it was a negative review. Different classification tools were used for instance such as neural networks, logistic regression and different types of Naive Bayes. You can see the [file here for text classification 1](TextClassification1).

## ACL Paper Summary

This paper takes a look into a long paper that was submitted to the Association for Computing Linguistics(ACL) conference. The long paper that was chosen was one called SalesBot: Transitioning from Chit-Chat to Task-Oriented Dialogues. The long paper focuses on a chatbot that primarily works on starting with open domain free dialougue and then transition to a task oriented dialogue depending on how the original conversation goes. Within the paper summary, I talk about many details regarding the chatbot as well as my thoughts on how it may impact the future of computing as well as its own field. You can see the [file here](ACL_Paper).

## Chatbot

This program creates a chatbot that can interact with a user about any of the Champions Leagues Finals. The program is able to tell users details about specific interests regarding the Champions League such as "how many goals does Lionel Messi have?", "Who won the 1990-1991 Champions League final?", and many other questions regarding the Champions League. The chatbot relies on a knowledge base that was taken from a dataset on kaggle that contains a lot of the information and data that was needed regarding the Champions League finals, player data, and team data. This data was then put into a SQL database that we were able to call upon. Along with this the program uses a MultiNomial Naive Bayes machine learning model to detect what subject the question is regarding whether it is a question about a specific final, player, or team. From there the chatbot uses similarity metrics and NER to successfully answer the question. You can see the [chatbot here](ChatBot).

## Text Classification 2

This program takes a look into using different keras and tenserflow tools to classify text. It is fairly similar to Text Classification 1, but many of the models and tools that were used are different. The data that was used for this program was a dataset from kaggle regarding jokes. A piece of text is given the value of 1 if it is indeed a joke and a 0 if it is otherwise. In this program different types of models were used such as RNN, CNN, LSTM, and Embedding. You can see the [file here for text classification 2](TextClassification2).

## Skills Learned

Throughout this entire process I was able to gain many skills with some being technical skills as well as soft skills. To see the list of skills click on this [link here](Skills.md).
