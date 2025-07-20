import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_text(self):
        node1 = TextNode("Text one", TextType.TEXT)
        node2 = TextNode("Text two", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Link", TextType.LINK, url="http://example.com")
        node2 = TextNode("Link", TextType.LINK, url="http://example.com")
        self.assertEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("Link", TextType.LINK, url="http://example.com")
        node2 = TextNode("Link", TextType.LINK, url="http://different.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()

