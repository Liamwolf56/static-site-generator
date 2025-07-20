import unittest
from textnode import TextNode, TextType
from split_nodes_links_images import split_nodes_image, split_nodes_link

class TestSplitNodesLinksImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(result, expected)

    def test_split_links(self):
        node = TextNode(
            "This is a link [to google](https://google.com) and [to github](https://github.com)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to github", TextType.LINK, "https://github.com"),
        ]
        self.assertEqual(result, expected)

    def test_no_images(self):
        node = TextNode("Just plain text here.", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_no_links(self):
        node = TextNode("No links here.", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_non_text_node(self):
        node = TextNode("Should stay the same", TextType.CODE)
        self.assertEqual(split_nodes_image([node]), [node])
        self.assertEqual(split_nodes_link([node]), [node])


if __name__ == "__main__":
    unittest.main()
