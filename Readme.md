#  This is a Chatbot project using Django and Rasa
**First to train please remove the chat/rasa-bot/models folder**

# Requirements:
**Django** 
```
pip3 install django
```

**python-decouple**

```
pip3 install python-decouple
```

#  If you have installed Rasa NLU and Rasa Core skip these steps: 

**rasa_nlu**
```
pip3 install rasa_nlu
```

**rasa_core**

```
pip3 install rasa_core
```

# cd into rasa-bot folder you can replace nlu.md with your json data and also edit the domain.yml && stories.md due to your intents

**Train NLU first, in rasa-bot open terminal**

```
python3 -m rasa_nlu.train --config nlu_config.yml --data nlu.md
// if you replace with json file
python3 -m rasa_nlu.train --config nlu_config.yml --data yourData.json
```

**In rasa-bot/bot.py**
Replace 
```
agent = Agent.load('models/dialogue', interpreter='models/nlu/default/model_20190312-152716/')
```
by 
```
agent = Agent.load('models/dialogue', interpreter='Your_Path')
```

Your_Path  = models/nlu/default/model_2019......../

**Train Rasa Core, still inside rasa-bot**

```
python3 -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

# Run server and application

**cd in root folder**

```
python3 manage.py runserver
```

**cd into rasa-bot in another terminal**

```
python3 bot.py
```

**App run at http://127.0.0.1:8000/ **




