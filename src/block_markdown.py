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


def markdown_to_blocks(markdown):
    def md_strip(text):
        return "\n".join(map(lambda x: x.strip(), text.strip().split("\n")))

    return list(
        filter(lambda x: x.strip() != "", map(md_strip, markdown.split("\n\n")))
    )
