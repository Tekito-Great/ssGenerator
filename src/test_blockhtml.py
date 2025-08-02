import unittest


from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from blockhtml import block_to_html

class TestBlockTHML(unittest.TestCase):

    def block_to_html_test(self):
        blocks = [
            "This is a paragraph\n Second line of the first paragraph\n Third line of the first paragraph",
            "This is another paragraph"
        ]
        print("blocks", blocks)
        html_nodes = block_to_html(blocks)
        self.assertEqual(len(html_nodes), 2)
        self.assertEqual(html_nodes[0], ParentNode(tag="p", value="", children=[
            LeafNode(tag=None, value="This is a paragraph\n Second line of the first paragraph\n Third line of the first paragraph")
        ]))
        self.assertEqual(html_nodes[1], ParentNode(tag="p", value="", children=[
            LeafNode(tag=None, value="This is another paragraph")
        ]))


if __name__ == "__main__":
    unittest.main()