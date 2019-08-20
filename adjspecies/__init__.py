import os
from pathlib import Path
from random import choice
import yaml


class AnimalTokens:
    def __init__(self,
                 adjective_file='adjectives.yaml',
                 animal_file='animals_short.yaml',
                 with_replacement=False):
        this_folder = Path(os.path.dirname(os.path.abspath(__file__)))
        adjective_abs = this_folder / adjective_file
        animals_abs = this_folder / animal_file
        with open(adjective_abs, 'r') as f:
            self.adjectives = yaml.safe_load(f)
        with open(animals_abs, 'r') as f:
            self.animals = yaml.safe_load(f)
        self.generated = set()
        self.with_replacement = with_replacement

    def random_token(self, sep='', maxlen=16):
        while True:
            token = choice(self.adjectives) + sep + choice(self.animals)
            if maxlen and len(token) > maxlen:
                continue
            if not self.with_replacement and token in self.generated:
                continue
            break
        self.generated.add(token)
        return token
