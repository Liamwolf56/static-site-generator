import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_string_returns_empty_list(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_blocks_with_extra_newlines(self):
        md = "\n\n# Heading\n\n\nParagraph text\n\n\n- List item\n\n"
        self.assertEqual(
            markdown_to_blocks(md),
            ["# Heading", "Paragraph text", "- List item"]
        )

if __name__ == "__main__":
    unittest.main()
