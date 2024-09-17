class Que:
    "要素が整数のキューオブジェクト"
    def __init__(self, queue: list[int]) -> None:
        self._queue: list = queue

    def __eq__(self, other)->bool:
        "入力されたキューとの等価性を評価する"
        if isinstance(other, Que): # otherがQueである
            return self.get() == other.get() # self, otherのlistが等しい
        return False


    def get(self)->list[int]:
        "リストを返す"
        return self._queue
    
    def head(self)->int:
        "先頭を返す"
        return self._queue[0]
    
    def add(self, x:int):
        que_list: list[int] = self.get()
        que_list.append(x)
        return Que(que_list)
    
    def pop(self):
        que_list: list[int] = self.get()
        new_que_list = que_list[1:]
        return Que(new_que_list)
