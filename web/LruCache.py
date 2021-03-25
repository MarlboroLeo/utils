from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity=128):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key):
        # 每次访问更新最新使用key
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        # 更新kv
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)
