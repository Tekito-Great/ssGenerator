from markdown_block import BlockType, block_to_block_type
from markdown import text_to_textnode
from textnode import TextNode, TextType
import re
from htmlnode import LeafNode, ParentNode
from main import text_node_to_html_node

#input : string[], output : HTMLnode[]
def block_to_html(blocks):
    htmlnodes =[]
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                text_nodes =text_to_textnode(block)
                child_nodes = []
                for text in text_nodes:
                    child_nodes.append(text_node_to_html_node(text)) 
                ParentNode = ParentNode(tag="p", value="",dhildren=child_nodes)
                htmlnodes.append(ParentNode)
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass
            case _:
                raise ValueError("This Block Type is not supported")

    print("htmlnodes", htmlnodes)
    print("html", htmlnodes[0].to_html())
    print("html", htmlnodes[1].to_html())
    return htmlnodes



