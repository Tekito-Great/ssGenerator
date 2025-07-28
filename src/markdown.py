from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType
import re

dict = {
    TextType.TEXT: "",
    TextType.BOLD: "**",
    TextType.ITALIC: "*",
    TextType.CODE: "'",
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type not in [TextType.TEXT, TextType.BOLD, TextType.ITALIC, TextType.CODE]:
        raise ValueError("text_type must be TEXT, BOLD, ITALIC, or CODE")
    
    if not isinstance(old_nodes, list):
        raise ValueError("old_nodes must be a list of TextNode instances") 

    if text_type not in dict or dict[text_type] != delimiter:
        raise ValueError("text_type and delimiter combination is not supported")

    new_nodes = []

    for node in old_nodes:
        if (node.text_type != TextType.TEXT) or (text_type == TextType.TEXT and delimiter == ""): 
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) == 0:
            raise ValueError(f"TextNode with text '{node.text}' does not contain the delimiter '{delimiter}'")
        if node.text.count(delimiter) % 2 != 0:
            raise ValueError(f"TextNode with text '{node.text}' contains an odd number of delimiters '{delimiter}'")
        
        # Split the text into three parts using the delimiter
        parts = node.text.split(delimiter) 
        if len(parts) % 2 != 1:
            raise ValueError(f"TextNode with text '{node.text}' does not split into an odd number of parts with delimiter '{delimiter}'")
        
        # Create a new TextNode for each part
        i = 0
        for i in range(len(parts)):
            if parts[i] != "":
                if i % 2 == 0:
                    # Even index parts are of the specified text_type
                    node_new = TextNode(parts[i], TextType.TEXT, node.url)
                else:
                    # Odd index parts are of TextType.TEXT
                    node_new = TextNode(parts[i], text_type, node.url)                    
                new_nodes.append(node_new) 
            
    return new_nodes

def extract_markdown_images(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    match = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)

    if match == []:
        return []

    return match

def extract_markdown_links(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    if match == []:
        return []

    return match