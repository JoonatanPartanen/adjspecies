import os
from pathlib import Path
from random import choice
import yaml


class AnimalTokens:
    def __init__(self,
                 word_list_files=('adjectives.yaml',
                                  'animals_short.yaml',
                                  'verbs.yaml'),
                 with_replacement=False,
                 previously_generated=[]):
        this_folder = Path(os.path.dirname(os.path.abspath(__file__)))
        self.word_lists = []
        for file_path in word_list_files:
            processed_path = Path(file_path)
            if not processed_path.is_absolute():
                processed_path = this_folder / processed_path
            with open(processed_path, 'r') as f:
                self.word_lists.append(yaml.safe_load(f))
        self.previously_generated = set(previously_generated)
        self.with_replacement = with_replacement

    def random_token(self, sep='', maxlen=21):
        while True:
            token = sep.join(choice(lst) for lst in self.word_lists)
            if maxlen and len(token) > maxlen:
                continue
            if not self.with_replacement and token in self.previously_generated:
                continue
            break
        self.previously_generated.add(token)
        return token
