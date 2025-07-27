from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode   


def main():
    test = TextNode("test", TextType.LINK,"http://test.test")   
    print (test)


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("text_node must be an instance of TextNode")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:               
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("TextNode with LINK type must have a URL")
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("TextNode with IMAGE type must have a URL")
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Unsupported TextType: {text_node.text_type}")



main()