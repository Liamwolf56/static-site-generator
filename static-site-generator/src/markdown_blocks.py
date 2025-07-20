def markdown_to_blocks(markdown):
    # Split on double newlines to separate blocks
    raw_blocks = markdown.split("\n\n")

    # Strip whitespace from each block and remove empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]

    return blocks
