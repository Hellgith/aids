class TreeNode:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.left = self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    def add(self, keyword, meaning):
        self.root = self._insert(self.root, keyword, meaning)

    def _insert(self, node, keyword, meaning):
        if not node:
            return TreeNode(keyword, meaning)
        if keyword < node.keyword:
            node.left = self._insert(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self._insert(node.right, keyword, meaning)
        else:
            node.meaning = meaning
        return node

    def delete(self, keyword):
        self.root = self._delete(self.root, keyword)

    def _delete(self, node, keyword):
        if not node:
            return node
        if keyword < node.keyword:
            node.left = self._delete(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._delete(node.right, keyword)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._find_min(node.right)
            node.keyword, node.meaning = temp.keyword, temp.meaning
            node.right = self._delete(node.right, temp.keyword)
        return node

    def _find_min(self, node):
        while node.left: node = node.left
        return node

    def update(self, keyword, new_meaning):
        node = self._search(self.root, keyword)
        if node:
            node.meaning = new_meaning
        else:
            print(f"'{keyword}' not found.")

    def _search(self, node, keyword):
        if not node or node.keyword == keyword:
            return node
        return self._search(node.left, keyword) if keyword < node.keyword else self._search(node.right, keyword)

    def display_sorted(self, ascending=True):
        self._inorder(self.root) if ascending else self._reverse_inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"{node.keyword}: {node.meaning}")
            self._inorder(node.right)

    def _reverse_inorder(self, node):
        if node:
            self._reverse_inorder(node.right)
            print(f"{node.keyword}: {node.meaning}")
            self._reverse_inorder(node.left)

    def max_comparisons(self):
        return self._height(self.root)

    def _height(self, node):
        if not node: return 0
        return max(self._height(node.left), self._height(node.right)) + 1

def main():
    bst = DictionaryBST()
    while True:
        print("\n1. Add ") 
        print("\n2. Delete ") 
        print("\n3. Update" )
        print("\n4. Display ")
        print("\n5. Max Comparisons" ) 
        print("\n6. Exit")
        choice = input("Choice: ")
        if choice == "1":
            k = input("Keyword: "); m = input("Meaning: ")
            bst.add(k, m)
        elif choice == "2":
            bst.delete(input("Keyword to delete: "))
        elif choice == "3":
            k = input("Keyword to update: "); m = input("New meaning: ")
            bst.update(k, m)
        elif choice == "4":
            o = input("Order (asc/desc): ").lower()
            bst.display_sorted(o == "asc")
        elif choice == "5":
            print("Max comparisons:", bst.max_comparisons())
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
