import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()