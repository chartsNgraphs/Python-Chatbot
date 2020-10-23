from Engine import ConversationalEngine
from ArticulationMapper import ArticulationMapper
from collections import namedtuple
class Conversation():
    def __init__(self, app, engine: ConversationalEngine):
        super().__init__()
        self.app=app
        self.engine = engine
        self.utterances = []
        self.responses = []
        self.interactions = []
        self.articMapper = ArticulationMapper()
    
    def interact(self, utterance: str):
        self.utterances.append(utterance)
        response = self.engine.getIntent(utterance)
        self.responses.append(response[0])
        articulation = self.articMapper.get(response[0])
        Interaction = namedtuple('Interaction', ['utterance', 'response'])
        self.interactions.append(Interaction(utterance, articulation))
        return articulation

    def get(self):
        '''returns all the interactions for the conversation as a list'''
        return self.interactions
    
    def getConvoLength(self):
        '''returns the conversation length'''
        return len(self.interactions)
    
def main():
    engine = ConversationalEngine(app=None)
    convo = Conversation(app=None, engine=engine)
    while 1: 
        entry=input()
        print(convo.interact(entry))

if __name__=="__main__":
    main()