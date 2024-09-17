import unittest

from que import Que


class TestQue(unittest.TestCase):
    def test_get(self):
        "キューを取得する"
        q = Que([1, 2, 3])
        get_que = q.get()
        self.assertEqual(get_que, [1, 2, 3])

    def test_head(self):
        "キューの先頭を取り出す"
        q = Que([1, 2, 3])
        head: int = q.head()
        self.assertEqual(head, 1)

    def test_add(self):
        "キューに要素を追加する"
        q = Que([1, 2, 3])
        new_q: Que = q.add(4)
        new_list = new_q.get()
        self.assertEqual(new_list, [1, 2, 3, 4])

    def test_pop(self):
        "キューの先頭を削除する"
        q = Que([1, 2, 3])
        new_q: Que = q.pop()
        self.assertEqual(new_q.get(), [2, 3])

    def test_eq(self):
        "等価性の評価をテストする"
        # 等価なケース
        q1 = Que([1, 2, 3])
        q2 = Que([1, 2, 3])
        self.assertTrue(q1 == q2)

        # 等価でないケース
        q1 = Que([1, 2, 3])
        q2 = Que([1, 2, 4])
        self.assertFalse(q1 == q2)
