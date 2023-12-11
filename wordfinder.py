"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ..."""Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse file -> list of words."""

        return [w.strip() for w in file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

wf = WordFinder('words.txt')

print(wf.random())