# Completed implementation of a queue ADT

class Queue:
  def __init__(self):
    self.items = []
  def is_empty(self):
    return self.items == []
  def enqueue(self, item): #Adds an element to the rear of the queue
    self.items.insert(0,item)
  def dequeue(self): #Adds an element to the front of the queue
    return self.items.pop()
  def size(self):
    return len(self.items)
