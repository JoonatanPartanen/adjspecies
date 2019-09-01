import os
from pathlib import Path
from random import choice
import yaml


class AnimalTokens:
    def __init__(self,
                 word_list_files=('adjectives.yaml',
                                  'animals_short.yaml',
                                  'verbs.yaml')):
        this_folder = Path(os.path.dirname(os.path.abspath(__file__)))
        self.word_lists = []
        for file_path in word_list_files:
            processed_path = Path(file_path)
            if not processed_path.is_absolute():
                processed_path = this_folder / processed_path
            with open(processed_path, 'r') as f:
                self.word_lists.append(yaml.safe_load(f))
        self.reroll_limit = 5

    def random_token(self, sep=''):
        token = sep.join(choice(lst) for lst in self.word_lists)
        return token
