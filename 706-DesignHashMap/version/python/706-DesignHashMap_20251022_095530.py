# Last updated: 10/22/2025, 9:55:30 AM
class MyHashMap(object):

    def __init__(self):
       self.hashMap = [] 

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for pair in self.hashMap:
            if pair[0] == key:
                pair[1] = value
                return
        self.hashMap.append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for pair in self.hashMap:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for pair in self.hashMap:
            if pair[0] == key:
                self.hashMap.remove(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)