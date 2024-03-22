import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_1(self):
        node = TextNode("Node", "italic", None)
        node2 = TextNode("Node", "italic", None)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("Node", None, None)
        node2 = TextNode("Node", None, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

