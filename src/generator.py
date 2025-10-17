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


def split_node(node, matches, text_type):
    match_nodes = []
    remaining_text = node.text
    for match in matches:
        # split once on constructed image markdown
        markdown = f"[{match[0]}]({match[1]})"
        if text_type == TextType.IMAGE:
            markdown = "!" + markdown
        parts = remaining_text.split(markdown, 1)
        # append leading text string as node and create new image node and append
        # check if text is empty or just whitespace first
        if parts[0].strip():  # check for whitespace only
            match_nodes.append(TextNode(parts[0]))
        match_nodes.append(TextNode(match[0], text_type, match[1]))
        remaining_text = parts[1]
    if remaining_text.strip():
        match_nodes.append(TextNode(remaining_text))
    return match_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if not node.text.strip():
            # node text is whitespace only
            continue
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        match_nodes = split_node(node, matches, TextType.IMAGE)
        new_nodes.extend(match_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if not node.text.strip():
            # node text is whitespace only
            continue
        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        match_nodes = split_node(node, matches, TextType.LINK)
        new_nodes.extend(match_nodes)
    return new_nodes
