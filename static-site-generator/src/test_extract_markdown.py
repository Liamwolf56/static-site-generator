import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(matches, expected)

    def test_extract_markdown_images_multiple(self):
        text = "![one](url1) and ![two](url2)"
        matches = extract_markdown_images(text)
        expected = [("one", "url1"), ("two", "url2")]
        self.assertListEqual(matches, expected)

    def test_extract_markdown_links_single(self):
        text = "Here is a [link](https://example.com)"
        matches = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertListEqual(matches, expected)

    def test_extract_markdown_links_multiple(self):
        text = "Here is [one](url1) and [two](url2)"
        matches = extract_markdown_links(text)
        expected = [("one", "url1"), ("two", "url2")]
        self.assertListEqual(matches, expected)

    def test_extract_markdown_links_ignores_images(self):
        text = "![image](image.png) and [link](https://site.com)"
        matches = extract_markdown_links(text)
        expected = [("link", "https://site.com")]
        self.assertListEqual(matches, expected)

if __name__ == "__main__":
    unittest.main()
