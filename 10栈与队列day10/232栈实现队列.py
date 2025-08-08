class MyQueue(object):

    def __init__(self):
        self.A,self.B = [],[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: int
        """
        peek = self.peek()
        self.B.pop()
        return peek

    def peek(self):
        """
        :rtype: int
        """
        if self.B:
            return self.B[-1]
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]
        
            

    def empty(self):
        """
        :rtype: bool
        """
        return not self.A and not self.B