from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#create a instance of the class Chatbot which will refer to the objct in the memory and will 
#intialize your bot 
#name keyword parameter for you bot name ,storage_adapters means you can pick where to store 
#the bank of queries which we will use to train our bot .our bot will work based on the 
#logic which we give as a keyword args i used Bestmatch logic which means our bot will
#work based on the best match for the queries from the user and it will check for a best
#match in its bank for the response to reply

def chatbot(user_input="hi"):

    DummyBot = ChatBot(name='Dummy',
                    storage_adpaters="chatterbot.storage.SQLStorageAdapter",
                    logic_adapters = ["chatterbot.logic.BestMatch"],  
                    )

    #training our bot .we can use any method for training ,we can pick any language for traning
    #we can give our own query and answer to train the bot .we will use Chatterbot trainers to 
    # train our bot 

    trainer = ChatterBotCorpusTrainer('Dummy')
    trainer.train("chatterbot.corpus.english")

    while True : 
        if user_input.lower() == 'quit' : 
            break 
        else : 
            response = DummyBot.get_response(user_input)
            print(response)

if __name__ == '__main__' : 
    chatbot()



