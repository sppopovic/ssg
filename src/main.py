from textnode import TextNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    print(node2)
    are_equal = (node == node2)
    print(are_equal)

main()
