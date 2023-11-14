# Chatbot

# installing
- python 3.10.10
- pip install rasa
- pip install fuzzywuzzy
- pip install pandas
- pip install pymongo
- pip install google-api-python-client

# jalankan run actions di cmd(1) - ini cmd tersendiri 
rasa run actions 

#  Train Model di cmd(2) -  train hanya perlu sekali tidak perlu berulang kali jika sudah pernah ditrain bisa lanjut ke "Run chatbot"
rasa train 

# Run chatbot di cmd(2)
rasa run --enable-api --cors "*"
