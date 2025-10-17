import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # def test_block_to_block_type(self):
    #     blocks = [
    #         "This is a paragraph, buddy.",
    #         "# Heading 1",
    #         "```\nthis is some code in codeland\n```",
    #         "-This will be a nice unordered list\n-with multiple\n-items",
    #         "1. An ordered list here\n2. which more than one\n3. precious item",
    #         "> this is an important quote\n> from a very famous individual",
    #     ]
    #     results = []
    #     for block in blocks:
    #         results.append(block_to_block_type(block))
    #     print(results)
    #     self.assertListEqual(
    #         results,
    #         [
    #             BlockType.PARAGRAPH,
    #             BlockType.HEADING,
    #             BlockType.CODE,
    #             BlockType.UNORDERED_LIST,
    #             BlockType.ORDERED_LIST,
    #             BlockType.QUOTE,
    #         ],
    #     )

    def test_block_to_type_quote(self):
        block = "> this is an important quote\n> from a very famous individual"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, result)

    def test_block_to_type_ordered_list(self):
        block = "- This will be a nice unordered list\n- with multiple\n-items"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, result)

    def test_block_to_type_unordered_list(self):
        block = "1. An ordered list here\n2. which more than one\n3. precious item"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, result)

    def test_block_to_type_code(self):
        block = "```\nthis is some code in code \n and it has multiple lines```"
        result = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, result)

    def test_block_to_type_paragraph(self):
        block = "This is a paragraph\nwith multiple lines, my man."
        result = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_block_to_type_heading(self):
        h1 = block_to_block_type("# Heading")
        h2 = block_to_block_type("## Heading")
        h3 = block_to_block_type("### Heading")
        h4 = block_to_block_type("#### Heading")
        h5 = block_to_block_type("##### Heading")
        h6 = block_to_block_type("###### Heading")
        self.assertEqual(BlockType.HEADING, h1)
        self.assertEqual(BlockType.HEADING, h2)
        self.assertEqual(BlockType.HEADING, h3)
        self.assertEqual(BlockType.HEADING, h4)
        self.assertEqual(BlockType.HEADING, h5)
        self.assertEqual(BlockType.HEADING, h6)
