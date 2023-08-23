#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self._value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    self._value = new_value

  def is_sentence(self):
    if self.value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    count = 0
    sentences = self.value.replace("?", ".").replace("!", ".").replace("...", ".").replace("..", ".")
    print(sentences)
    for _ in sentences.split("."):
      count += 1
    return count-1
  
simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())
