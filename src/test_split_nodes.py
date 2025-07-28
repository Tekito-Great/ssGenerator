import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_split_nodes_delimiter_valid1(self):
        nodes = [TextNode("*This* is *italic* 'text'. *So great!*", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(len(result), 5)
        self.assertEqual((result[0].text, result[0].text_type, result[0].url), ("This", TextType.ITALIC, None))
        self.assertEqual((result[1].text, result[1].text_type, result[1].url), (" is ", TextType.TEXT, None))
        self.assertEqual((result[2].text, result[2].text_type, result[2].url), ("italic", TextType.ITALIC, None))
        self.assertEqual((result[3].text, result[3].text_type, result[3].url), (" 'text'. ", TextType.TEXT, None))
        self.assertEqual((result[4].text, result[4].text_type, result[4].url), ("So great!", TextType.ITALIC, None))
        
    def test_split_nodes_delimiter_valid2(self):
        nodes = [TextNode("This is 'code' text, including **bold** mark.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "'", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual((result[0].text, result[0].text_type, result[0].url), ("This is ", TextType.TEXT, None))
        self.assertEqual((result[1].text, result[1].text_type, result[1].url), ("code", TextType.CODE, None))
        self.assertEqual((result[2].text, result[2].text_type, result[2].url), (" text, including **bold** mark.", TextType.TEXT, None))

    def test_split_nodes_delimiter_valid3(self):
        nodes = [TextNode("This is a **bold** text **again!**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 4)
        self.assertEqual((result[0].text, result[0].text_type, result[0].url), ("This is a ", TextType.TEXT, None))
        self.assertEqual((result[1].text, result[1].text_type, result[1].url), ("bold", TextType.BOLD, None))
        self.assertEqual((result[2].text, result[2].text_type, result[2].url), (" text ", TextType.TEXT, None))
        self.assertEqual((result[3].text, result[3].text_type, result[3].url), ("again!", TextType.BOLD, None))

    def test_split_nodes_delimiter_invalid_text_type(self):
        nodes = [TextNode("This is *bold* text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "*", TextType.LINK)

    def test_split_nodes_delimiter_text_node(self):
        nodes = [TextNode("This is a text node", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "", TextType.TEXT)
        self.assertEqual(len(result), 1)
        self.assertEqual((result[0].text, result[0].text_type, result[0].url), ("This is a text node", TextType.TEXT, None))

    def test_split_nodes_delimiter_no_delimiter(self):
        nodes = [TextNode("This is a text without delimiter", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "*", TextType.BOLD)


class TestExtractMarkdownImages(unittest.TestCase):
    
    def test_extract_markdown_images_valid(self):
        text = "This is an image ![alt text](http://example.com/image.png) and one more image ![another alt](http://example.com/another_image.png)"
        result = extract_markdown_images(text)
        self.assertListEqual([("alt text", "http://example.com/image.png"), ("another alt", "http://example.com/another_image.png")], result)

    def test_extract_markdown_images_no_images(self):
        text = "This is a text without images"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_images_invalid_text(self):
        with self.assertRaises(ValueError):
            extract_markdown_images(12345)

class TestExtractMarkdownLinks(unittest.TestCase):
    
    def test_extract_markdown_links_valid(self):
        text = "This is a link [example](http://example.com) and another [test](http://test.com)"
        result = extract_markdown_links(text)
        self.assertListEqual([("example", "http://example.com"), ("test", "http://test.com")], result)

    def test_extract_markdown_links_no_links(self):
        text = "This is a text without links"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_invalid_text(self):
        with self.assertRaises(ValueError):
            extract_markdown_links(12345)