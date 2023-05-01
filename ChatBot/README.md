## How To Run The Program

Here are the instructions to run the bot

 1. all of the files should be loaded and ready to go so all you need to do is download and import any dependencies you may not have and then run the command python3 bot.py.
 2. The bot will ask you for your name in which you can go ahead and give it, if you wish to logout you may type in the command logout, and it will save your data for next time when you reenter your name
 3. If you at any time say you like or dislike anything the bot will remember what it is.
4. If for some reason the bot is not running then, run the commands **python3 champions_league_kb.py** then **python3 training_model.py** and then finally **python3 bot.py**
5. If for some reason you are getting an error message regarding en_core_web_sm then go ahead and run the commands
 * pip install -U pip setuptools wheel 
* pip install -U spacy
* python3 -m spacy download en_core_web_sm and then replace line 13 in the boy.py file with nlp = en_core_web_sm.load()

From there you can run python3 bot.py

## Lessons Learned

This project was by far the most fun project to create. There were a lot of lessons learned but I think the most interesting thing was to see how so many different NLP components came together and 
created a fully functioning project. Oftentimes assignments may be contained in their own element of trying to experiment with taht specific tool, but being able to apply everything that we had learned
was a very fun learning process overall. Applying the model and then using NER to then figure out what type of question the user was asking was perhaps the coolest thing I was able to build on the project.
