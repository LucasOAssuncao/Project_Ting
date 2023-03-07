from ting_file_management.abstract_queue import AbstractQueue
from queue import deque


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError("Invalid index")
        return self.queue[index]
