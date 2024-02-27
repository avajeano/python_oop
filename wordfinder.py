"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Returns random words from a dictionary"""

    def __init__(self,path):
        """Put in path to a dictionary"""
        self.path = path
    
    def word_count(path):
        with open(path,'r') as dictionary:
            total_words = 0
            for line in dictionary:
                words = line.split()
                total_words += len(words)
        print(f"{total_words} words read")
    
    def random(path):
        with open(path,'r') as dictionary:
            line_count = sum(1 for line in dictionary)
        random_line_num = random.randint(0, line_count - 1)
        with open(path, 'r') as file:
            for i, line in enumerate(file):
             if i == random_line_num:
                return line.strip()

class SpecialWordFinder(WordFinder):
   """Excludes blanks and comments"""

   def parse(self, path):
      with open(path,'r') as dictionary:
         #Filter out blank lines and comments
         lines = [line.strip() for line in dictionary if line.strip() and not line.strip.startswith('#')]
         line_count = len(lines)
      random_line_num = random.randit(0, line_count -1)
      return lines[random_line_num]
