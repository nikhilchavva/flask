import LRUcache
class TestLRU:
    def __init__(self):
        obj=LRUcache()
    def testGet(self):
        assert(self.obj.put(1,1))
    def testPut(self):
        self.obj.put(2,2)
        self.obj.put(3,3)
    def testGetCache():
        
if __name__ == '__main__':
test=TestLRU()

