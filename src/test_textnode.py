import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equality_different_text(self):
        node1 = TextNode("Hello", TextType.ITALIC, "http://example.com")
        node2 = TextNode("Hi", TextType.ITALIC, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_equality_different_type(self):
        node1 = TextNode("Hello", TextType.ITALIC, "http://example.com")
        node2 = TextNode("Hello", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_repr_with_none_url(self):
        node = TextNode("Hello", TextType.CODE)
        expected = "TextNode(Hello, code, None)"
        self.assertEqual(repr(node), expected)



if __name__ == "__main__":
    unittest.main()