from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    # node = TextNode("jumpin' jehosephet!", TextType.BOLD)
    # print(node)

    # html = HTMLNode("peanut", "butter")
    # html2 = HTMLNode("jelly", "sandwich", [html], {"prop1": "val1", "prop2": "val2"})
    # print(html2)

    # pnode = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #     ],
    # )

    # print(pnode)
    # print(pnode.to_html())

    new_nodes = text_to_textnodes(
        "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    )
    # print(new_nodes)


if __name__ == "__main__":
    main()
