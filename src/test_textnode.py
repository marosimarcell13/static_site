import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_wURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "URL")
        node2 = TextNode("This is a text node", TextType.BOLD, "URL")
        self.assertEqual(node, node2)
    
    def test_dif_text(self):
        node = TextNode("Dog", TextType.BOLD, "URL")
        node2 = TextNode("Cat", TextType.BOLD, "URL")
        self.assertNotEqual(node, node2)
    
    def test_dif_URL(self):
        node = TextNode("Dog", TextType.BOLD, "URL")
        node2 = TextNode("Dog", TextType.BOLD, "RLU")
        self.assertNotEqual(node, node2)

    def test_dif_Type(self):
        node = TextNode("Dog", TextType.BOLD, "URL")
        node2 = TextNode("Dog", TextType.LINK, "URL")
        self.assertNotEqual(node, node2)

    def test_mis_URL(self):
        node = TextNode("Dog", TextType.BOLD, "URL")
        node2 = TextNode("Dog", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()