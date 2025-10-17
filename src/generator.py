import re
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) == 1:
            # delimiter not found, just add node as is
            new_nodes.append(node)
            continue
        elif len(parts) % 2 == 0:
            # an opening delimiter lacks a matching close
            raise Exception(
                f"Invalid markdown syntax. No matching delimiter {delimiter}: {node.text}"
            )

        for i in range(len(parts)):
            new_nodes.append(TextNode(parts[i], text_type if i % 2 else TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    # matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)  # provided by boot.dev
    return matches


def extract_markdown_links(text):
    # matches = re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)
    matches = re.findall(
        r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text
    )  # provided by boot.dev
    return matches
