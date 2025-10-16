from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("jumpin' jehosephet!", TextType.BOLD)
    print(node)

    html = HTMLNode("peanut", "butter")
    html2 = HTMLNode("jelly", "sandwich", [html], {"prop1": "val1", "prop2": "val2"})
    print(html2)

    pnode = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(pnode)
    print(pnode.to_html())


if __name__ == "__main__":
    main()
