from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    temp_list = []
    temp_list
    for node in old_nodes:
        i = 0
        if node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                raise Exception(f"Invalid Markdown syntax")
            temp = node.text.split(delimiter)
            if temp[-1] == "":
                temp.pop()
            for x in temp:
                if i % 2 == 0:
                    temp_list.append(TextNode(x, TextType.TEXT))
                else:
                    temp_list.append(TextNode(x, text_type))
                i += 1
                if temp_list[-1].text == "":
                    temp_list.pop()
        else:
            temp_list.append(node)
    result.extend(temp_list)
    return result


