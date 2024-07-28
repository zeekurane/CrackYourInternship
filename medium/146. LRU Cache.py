class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.lru_cache_dict={}
        self.lru_key=None

        
    def get(self, key: int) -> int:
        
        if key in self.lru_cache_dict:
            value=self.lru_cache_dict[key]
            del self.lru_cache_dict[key]
            self.lru_cache_dict[key]=value
            if key==self.lru_key:
                for x in self.lru_cache_dict:
                    self.lru_key=x
                    break
            return self.lru_cache_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lru_cache_dict)<=self.capacity:
            try:
                del self.lru_cache_dict[key]
            except KeyError:
                pass
            self.lru_cache_dict[key]=value
            
        if len(self.lru_cache_dict)>self.capacity:
            del self.lru_cache_dict[self.lru_key]
            for x in self.lru_cache_dict.keys():
                self.lru_key=x
                break
        
        if len(self.lru_cache_dict)==1 or key==self.lru_key:
            for x in self.lru_cache_dict.keys():
                self.lru_key=x
                break