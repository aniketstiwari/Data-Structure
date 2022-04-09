import pdb

class Queue:

  def __init__(self, capacity):
    self.front = self.size = 0
    self.rear = capacity - 1
    self.queue = [None] * capacity
    self.capacity = capacity


  def is_full(self):
    return self.size == self.capacity

  def is_empty(self):
    return self.size == 0

  def enqueue(self, item):
    if self.is_full():
      print("Queue is full")
      return
    self.rear = (self.rear + 1) % (self.capacity)
    self.queue[self.rear] = item
    self.size += 1
    print("%s enqueue item is" % str(item))

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return

    print("%s dequeue item is " % str(self.queue[self.front]))
    self.front = (self.front + 1) % self.capacity
    self.size -= 1

  def que_front(self):
    if self.is_empty():
      print("queue is empty")
      return
    print("Front item is", self.queue[self.front])

  def que_rear(self):
    if self.is_empty():
      print("queue is empty")
      return
    print("Rear item is", self.queue[self.rear])


if __name__ == '__main__':
  queue = Queue(5)
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  queue.enqueue(4)
  queue.enqueue(5)

  queue.dequeue()
  queue.dequeue()

  queue.que_front()
  queue.que_rear()

  #queue.enqueue(6)
