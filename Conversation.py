from Engine import ConversationalEngine
from ArticulationMapper import ArticulationMapper
from collections import namedtuple
class Conversation():
    def __init__(self, app, engine: ConversationalEngine, articulationdata: str):
        '''
        arguments: 
        app -- any object type, for reference by the conversation
        engine -- ConversationalEngine | an instantiated conversational engine
        articulationdata -- str | filepath to the articulation .csv file
        '''
        super().__init__()
        self.app=app
        self.engine = engine
        self.utterances = []
        self.responses = []
        self.interactions = []
        self.articMapper = ArticulationMapper(articulationdata)
    
    def interact(self, utterance: str, returnPayload = False):
        '''
        arguments:
        utterance -- str | the input utterance from the user 
        returnPayload -- bool | True if desired return value is conversation payload, False if desired return value is just articulation string. Default is False.

        returns: 
            str articulation value if returnPayload arg is False, otherwise: 
            dictionary with key-value pairs of: 
            articulation -- str  | the articulation for the matched intent
            intent -- str | the matched intent
            probability -- float | the probability associated with the matched intent
            probability_matrix -- list | a 2-dimensional list with elements of [intent name, probability] for all intents in the training set, sorted by highest to lowest probability
        '''
        self.utterances.append(utterance)
        response = self.engine.getIntent(utterance)
        self.responses.append(response.get('intent'))
        if response.get('probability') > 0.3:
            articulation = self.articMapper.get(response.get('intent'))
            if articulation == None:
                articulation = self.articMapper.get('no_articulation')
        else:
            articulation = self.articMapper.get('default')
        Interaction = namedtuple('Interaction', ['utterance', 'response'])
        self.interactions.append(Interaction(utterance, articulation))
        if returnPayload == False:
            return articulation
        else:
            return {
                'articulation' : articulation,
                'intent' : response.get('intent'),
                'probability' : response.get('probability'),
                'probability_matrix' : response.get('probability_matrix')
            }

    def get(self):
        '''returns all the interactions for the conversation as a list'''
        return self.interactions
    
    def getConversationLength(self):
        '''returns the conversation length'''
        return len(self.interactions)

