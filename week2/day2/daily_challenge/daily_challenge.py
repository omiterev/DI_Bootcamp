import math
class Pagination:
    def __init__(self,items=None,page_size=10):
        self.items=items
        self.page_size=page_size
        if items==None:
            self.items=[]
        self.current_idx=0
        self.total_pages=math.ceil((len(self.items)+1)/page_size)
        pass
    def get_visible_items(self):
        start=self.current_idx*self.page_size
        end=start+self.page_size
        return self.items[start:end]
    def go_to_page(self,page_num):
        if page_num<1:
            raise ValueError("page_num out of range")
        if page_num > self.total_pages:
            self.current_idx=self.total_pages-1
        else:
            self.current_idx=page_num-1
        return self
    def first_page(self):
        self.current_idx=0
        return self
    def last_page(self):
        self.current_idx=self.total_pages-1
        return self
    def next_page(self):
        page_num=self.current_idx+1
        if page_num==self.total_pages:
            print('Last page.')
            return self
        else:
            self.current_idx+=1
            return self
    def previous_page(self):
        page_num=self.current_idx-1
        if page_num<0:
            print('Fitst page.')
            return self
        else:
            self.current_idx-=1
            return self
    def __str__(self):
        return "\n".join(str(x) for x in self.get_visible_items())
        pass


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError