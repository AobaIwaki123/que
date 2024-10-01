class Que:
    "要素が整数のキューオブジェクト"

    def __init__(self, queue: list[int]) -> None:
        """
        コンストラクタ
        >>> q = Que([1, 2, 3])
        >>> q.get()
        [1, 2, 3]
        """
        self._queue: list = queue

    def __eq__(self, other) -> bool:
        """
        入力されたキューとの等価性を評価する
        >>> q1 = Que([1, 2, 3])
        >>> q2 = Que([1, 2, 3])
        >>> q1 == q2
        True
        >>> q3 = Que([4, 5, 6])
        >>> q1 == q3
        False
        """
        if isinstance(other, Que):  # otherがQueである
            return self.get() == other.get()  # self, otherのlistが等しい
        return False

    def get(self) -> list[int]:
        """
        リストを返す
        >>> q = Que([1, 2, 3])
        >>> q.get()
        [1, 2, 3]
        """
        return self._queue

    def head(self) -> int:
        """
        先頭を返す
        >>> q = Que([1, 2, 3])
        >>> q.head()
        1
        """
        return self._queue[0]

    def add(self, x: int):
        """
        要素を追加する
        >>> q = Que([1, 2, 3])
        >>> q2 = q.add(4)
        >>> q2.get()
        [1, 2, 3, 4]
        """
        que_list: list[int] = self.get()
        que_list.append(x)
        return Que(que_list)

    def pop(self):
        """
        先頭要素を削除する
        >>> q = Que([1, 2, 3])
        >>> q2 = q.pop()
        >>> q2.get()
        [2, 3]
        """
        que_list: list[int] = self.get()
        new_que_list = que_list[1:]
        return Que(new_que_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
