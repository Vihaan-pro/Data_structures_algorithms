class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Preorder Traversal: Root, Left, Right
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# Inorder Traversal: Left, Root, Right
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

# Postorder Traversal: Left, Right, Root
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")

# 1. File Organizer Tree
def create_file_organizer():
    root = Tree_node("Root Folder")
    root.left = Tree_node("Documents")
    root.right = Tree_node("Pictures")

    root.left.left = Tree_node("Work")
    root.left.right = Tree_node("Personal")

    root.left.left.left = Tree_node("report.docx")
    root.left.left.right = Tree_node("presentation.pptx")

    root.left.right.left = Tree_node("diary.txt")
    root.left.right.right = Tree_node("photos")

    root.right.left = Tree_node("Vacation")
    root.right.right = Tree_node("Family")

    root.right.left.left = Tree_node("beach.jpg")
    root.right.left.right = Tree_node("mountain.png")

    root.right.right.left = Tree_node("birthday.jpg")
    root.right.right.right = Tree_node("wedding.png")

    return root

# 2. Address Hierarchy Tree
def create_address_hierarchy():
    root = Tree_node("Asia")
    root.left = Tree_node("India")
    root.left.left = Tree_node("Maharashtra")
    root.left.left.left = Tree_node("Mumbai")
    root.left.left.left.left = Tree_node("Mumbai Suburban District")
    root.left.left.left.left.left = Tree_node("Andheri")
    root.left.left.left.left.left.left = Tree_node("MG Road, Apartment 101")

    return root

# 3. Social Network Tree (Simplified as User Hierarchy)
def create_social_network():
    root = Tree_node("User1 (Root)")
    root.left = Tree_node("Friends")
    root.right = Tree_node("Posts")

    root.left.left = Tree_node("User2")
    root.left.right = Tree_node("User3")

    root.left.left.left = Tree_node("User4")
    root.left.left.right = Tree_node("User5")

    root.right.left = Tree_node("Post1")
    root.right.right = Tree_node("Post2")

    root.right.left.left = Tree_node("Like1")
    root.right.left.right = Tree_node("Comment1")

    return root

# Main execution
if __name__ == "__main__":
    print("1. File Organizer Tree:")
    file_tree = create_file_organizer()
    print("Preorder:", end=" ")
    preorder_traversal(file_tree)
    print("\nInorder:", end=" ")
    inorder_traversal(file_tree)
    print("\nPostorder:", end=" ")
    postorder_traversal(file_tree)
    print("\n")

    print("2. Address Hierarchy Tree:")
    address_tree = create_address_hierarchy()
    print("Preorder:", end=" ")
    preorder_traversal(address_tree)
    print("\nInorder:", end=" ")
    inorder_traversal(address_tree)
    print("\nPostorder:", end=" ")
    postorder_traversal(address_tree)
    print("\n")

    print("3. Social Network Tree:")
    social_tree = create_social_network()
    print("Preorder:", end=" ")
    preorder_traversal(social_tree)
    print("\nInorder:", end=" ")
    inorder_traversal(social_tree)
    print("\nPostorder:", end=" ")
    postorder_traversal(social_tree)
    print("\n")
