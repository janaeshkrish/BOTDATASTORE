# RASA_BOT_STORE_DATA
  Switch to master branch to view code

## Overview 
  Using RASA opensource i have build a chatbot which is used to collect specific data from the user and stores the data in an excel sheet.And if a person want to retrive data based on some conditon it will fetch the data from the excel sheet and displays it in the chat window.
 ## Dependencies
 - Rasa 2.3
 - Python3.8.8
 - Rasa X (pip install rasa-x -i https://pypi.rasa.com/simple)
 - pip version 20.2
 - Docker 
 - image rasa/duckling
 - Code editor
 - pandas
 - openpyxl
 
 ## Usage
  In command prompt type
  > rasa init (to initialize)
  
  > rasa run actions
  
  > docker run -p 8000:8000 rasa/duckling
  
  > rasa x (For chat UI) or rasa shell (opens in command prompt)
