import unittest

from textnode import TextType, TextNode
from generator import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


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

    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_image_multi(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_link(self):
        text = "This is text with a link [to google](https://www.google.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to google", "https://www.google.com")], matches)

    def test_extract_markdown_link_multi(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_image_and_link(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image and [to youtube](https://www.youtube.com/@bootdotdev) link"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ],
            images,
        )
        self.assertListEqual(
            [
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            links,
        )
