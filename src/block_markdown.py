# Blocks look like this:
#
# # This is a heading
#
# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
#
# - This is the first list item in a list block
# - This is a list item
# - This is another list item
#

import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    def md_strip(text):
        return "\n".join(map(lambda x: x.strip(), text.strip().split("\n")))

    return list(
        filter(lambda x: x.strip() != "", map(md_strip, markdown.split("\n\n")))
    )


def all_lines_begin_with(block, marker):
    for line in block.split("\n"):
        if not line.startswith(marker):
            return False
    return True


# regular expressions for block matching
re_code = re.compile(r"^```[\s\S]*```$")
re_heading = re.compile(r"^(#{1,6})\s")
re_quote = re.compile(r"^(>.*\n?)+$", re.MULTILINE)
re_unordered = re.compile(r"^(-\s+.*\n?)+$", re.MULTILINE)
re_ordered = re.compile(r"^(\d+\.\s+.*\n?)+$", re.MULTILINE)


def block_to_block_type(block):
    if re_code.match(block):
        return BlockType.CODE

    if re_heading.match(block):
        return BlockType.HEADING

    if re_quote.match(block):
        return BlockType.QUOTE

    if re_unordered.match(block):
        return BlockType.UNORDERED_LIST

    if re_ordered.match(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


# block_to_block_type(): Alternative implementation without regexes:
#
# def block_to_block_type(block):
#     lines = block.split("\n")

#     if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
#         return BlockType.HEADING
#     if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
#         return BlockType.CODE
#     if block.startswith(">"):
#         for line in lines:
#             if not line.startswith(">"):
#                 return BlockType.PARAGRAPH
#         return BlockType.QUOTE
#     if block.startswith("- "):
#         for line in lines:
#             if not line.startswith("- "):
#                 return BlockType.PARAGRAPH
#         return BlockType.UNORDERED_LIST
#     if block.startswith("1. "):
#         i = 1
#         for line in lines:
#             if not line.startswith(f"{i}. "):
#                 return BlockType.PARAGRAPH
#             i += 1
#         return BlockType.ORDERED_LIST
#     return BlockType.PARAGRAPH
