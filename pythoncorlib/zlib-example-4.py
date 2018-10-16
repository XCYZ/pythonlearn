import zlib
import string,StringIO

class ZipInputStream:
    def __init__(self,file):
        self.file = file
    