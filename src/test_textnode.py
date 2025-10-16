import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("Picture of a grape", TextType.IMAGE, "images/graph.jpg")
        node2 = TextNode("Picture of a grape", TextType.IMAGE, "images/graph.jpg")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("to the repository", TextType.LINK, "myrespository/path.git")
        node2 = TextNode("It's a jungle out there!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("This is text")
        node2 = TextNode("This is text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is text", TextType.LINK)
        node2 = TextNode("This is text", TextType.LINK, "url/path.html")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
