from inline_markdown import text_to_textnodes
from block_markdown import markdown_to_blocks
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

    # new_nodes = text_to_textnodes(
    #     "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # )
    # print(new_nodes)

    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    print(list(markdown_to_blocks(md)))


if __name__ == "__main__":
    main()
