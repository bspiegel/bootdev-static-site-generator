import unittest

from textnode import TextType, TextNode
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot.dev](https://www.boot.dev) and another [to perplexity.ai](https://www.perplexity.ai)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "to perplexity.ai", TextType.LINK, "https://www.perplexity.ai"
                ),
            ],
            new_nodes,
        )

    def test_split_trailing_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and some trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and some trailing text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_leading_whitespace(self):
        node = TextNode(
            "          [to boot.dev](https://www.boot.dev) and another [to perplexity.ai](https://www.perplexity.ai)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "to perplexity.ai", TextType.LINK, "https://www.perplexity.ai"
                ),
            ],
            new_nodes,
        )

    def test_split_trailing_whitespace(self):
        node = TextNode(
            "This is a link [to boot.dev](https://www.boot.dev) and another [to perplexity.ai](https://www.perplexity.ai)                    ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "to perplexity.ai", TextType.LINK, "https://www.perplexity.ai"
                ),
            ],
            new_nodes,
        )

    def test_split_only_image(self):
        node = TextNode(
            "![peanut butter](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "peanut butter", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
            ],
            new_nodes,
        )

    def test_split_only_link(self):
        node = TextNode(
            "[to boot.dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot.dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )
