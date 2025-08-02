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
    block_list = markdown.split("\n\n")
    cleaned_list = [s.strip() for s in block_list if s.strip() != ""]
    return cleaned_list

def block_to_block_type(block):
    lines = block.splitlines()

    if lines and re.match(r'^#{1,6}\s', lines[0]):
        return BlockType.HEADING
    
    if len(lines) >= 2 and (lines[0].startswith("```") or lines[0].startswith("~~~")) and lines[-1].startswith(lines[0][:3]):
        return BlockType.CODE
    
    if block.lstrip().startswith(">"):
        return BlockType.QUOTE
    
    if block.lstrip().startswith("- "):
        return BlockType.UNORDERED_LIST
    
    if all(re.match(rf'^{i+1}\. ', line.lstrip()) for i, line in enumerate(block.splitlines()) if line.strip() != ''):
        return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH