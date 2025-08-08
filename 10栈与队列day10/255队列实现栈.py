class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        n = len(self.queue)
        self.queue.append(x)
        for i in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue