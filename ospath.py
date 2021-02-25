from sys import platform

class ospath:

    def __init__(self):
        self.envirpath = ''
        if platform=="windows":
            self.envirpath = 'C:/temp/'
        if platform=="linux":
            self.envirpath = '/home/jonas/temp/'

    def getPath(self):
        self.envirpath = ''
        if platform=="windows":
            self.envirpath = 'C:/temp/'
        if platform=="linux":
            self.envirpath = '/home/jonas/temp/'
        return self.envirpath

    def getDefaultPath(self):
        self.envirpath = ''
        if platform=="windows":
            self.envirpath = 'C:/monitororder/'
        if platform=="linux":
            self.envirpath = '/home/jonas/monitororder/'
        return self.envirpath