
class DuckStream(object):
    """
    Create a duck type class which is similar to IoStream, and methods in this class
    dont support multithreading.
    Only used for xmodem module.
    
    """

    def __init__(self, data: bytes | bytearray | None = None):
        self.offset = 0
        self.bufByteArray = bytearray()
        if data is not None:
            self.bufByteArray.extend(data)

    def read(self, size=1) -> bytearray | bool:
        if self.index > (self.size-1):
            return False
        if size > (self.size-self.index):
            startPos = self.offset
            self.offset=self.size
            return self.bufByteArray[startPos:]
        else:
            startPos = self.offset
            self.offset+=size
            return self.bufByteArray[startPos:(startPos+size)]
        

    def write(self, data: bytes|bytearray|list):
        self.bufByteArray.extend(data)

    def seek(self, offset: int):
        if offset > (self.size-1): raise ValueError("The offset exceeds the limit.")
        self.offset = offset

    @property
    def size(self) -> int:
        return len(self.bufByteArray)

    @property
    def index(self) -> int:
        return self.offset



data = bytes([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
stream = DuckStream()
stream.write([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

stream.seek(20)
print(stream.read(5), stream.index)