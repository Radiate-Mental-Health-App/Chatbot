## Chatbot Development 🤖
This repository contains a chatbot implementation using Python 3.10.10 along with several required dependencies. The chatbot utilizes the Rasa library, fuzzywuzzy, pandas, pymongo, and google-api-python-client to deliver a versatile and dynamic conversational experience.

## Installation 🛠️
1. Install Python 3.10.10 : https://www.python.org/downloads/release/python-31010/
2. Open your command prompt or terminal and execute the following commands :
   ```
   pip install rasa
   pip install fuzzywuzzy
   pip install pandas
   pip install pymongo
   pip install google-api-python-client
## Running the Chatbot ▶️
1. Run actions
   To execute run actions, open a separate command prompt or terminal window. Use the following       command:
   cmd 1
   ```
   rasa run actions
    ```
3. Train model
   Before running the chatbot, it's essential to train the model. This step needs to be performed     only once. If you've already trined the model, you can skip this step. In a new command prompt     or terminal window, use the following command :
   cmd 2
   ```
   rasa train
4. Run chatbot
   Finally, to run the chatbot, use the following command in the same command prompt or terminal window as the training step :
   cmd 2
   ```
   rasa run --enable-api --cors "*"
   ```
   This command starts the chatbot, enabling it's API and allowing communication. Feel free to connect and interact with the chatbot through the provided API.


#### Note 📝
Ensure that all dependencies are correctly installed, and the Python environment is set up before running the chatbot.
