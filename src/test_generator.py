import unittest

from textnode import TextType, TextNode
from generator import split_nodes_delimiter


class TestGenerator(unittest.TestCase):

    def test_inlines_split_code1(self):
        node = TextNode("This is text with a `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertSequenceEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word.", TextType.TEXT),
            ],
        )

    def test_inline_split_italic(self):
        node = TextNode("This is text with _italic words_.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertSequenceEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(".", TextType.TEXT),
            ],
        )

    def test_inline_split_bold(self):
        node = TextNode("This is text with a **bold** word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertSequenceEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word.", TextType.TEXT),
            ],
        )
