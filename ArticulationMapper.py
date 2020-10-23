import pandas as pd

class ArticulationMapper():
    def __init__(self, filepath):
        super().__init__()
        self.df = pd.read_csv(filepath)
        self.articulations = {}
        for row in self.df.itertuples():
            self.articulations[row.intent_name] = row.articulation
    
    def get(self, intent: str) -> str: 
        """returns the articulation for a given intent. if the intent has no articulation, then returns None"""
        return self.articulations.get(intent)

