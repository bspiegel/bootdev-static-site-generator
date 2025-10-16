from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("jumpin' jehosephet!", TextType.BOLD)
    print(node)
    html = HTMLNode("peanut", "butter")
    html2 = HTMLNode("jelly", "sandwich", [html], {"prop1": "val1", "prop2": "val2"})
    print(html2)


if __name__ == "__main__":
    main()
