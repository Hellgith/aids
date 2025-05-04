class Node:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return 0 if node is None else node.height

    def balanceFactor(self, node):
        return 0 if node is None else self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, node, keyword, meaning):
        if node is None:
            return Node(keyword, meaning)
        if keyword < node.keyword:
            node.left = self.insert(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self.insert(node.right, keyword, meaning)
        else:
            node.meaning = meaning
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balanceFactor(node)

        if balance > 1 and keyword < node.left.keyword:
            return self.rightRotate(node)
        if balance < -1 and keyword > node.right.keyword:
            return self.leftRotate(node)
        if balance > 1 and keyword > node.left.keyword:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and keyword < node.right.keyword:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def deleteNode(self, root, keyword):
        if root is None:
            return root
        if keyword < root.keyword:
            root.left = self.deleteNode(root.left, keyword)
        elif keyword > root.keyword:
            root.right = self.deleteNode(root.right, keyword)
        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right
                if temp is None:
                    temp = root
                    root = None
                else:
                    root = temp
                temp = None
            else:
                temp = self.minValueNode(root.right)
                root.keyword = temp.keyword
                root.meaning = temp.meaning
                root.right = self.deleteNode(root.right, temp.keyword)

        if root is None:
            return root
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        balance = self.balanceFactor(root)

        if balance > 1 and self.balanceFactor(root.left) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.balanceFactor(root.right) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.balanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and self.balanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def minValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.minValueNode(node.left)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append((root.keyword, root.meaning))
            self.inorder(root.right, result)

    def findKeyword(self, root, keyword, comparisons):
        if root is None:
            return False, comparisons
        comparisons += 1
        if keyword < root.keyword:
            return self.findKeyword(root.left, keyword, comparisons)
        elif keyword > root.keyword:
            return self.findKeyword(root.right, keyword, comparisons)
        else:
            return True, comparisons

    def addKeyword(self, keyword, meaning):
        self.root = self.insert(self.root, keyword, meaning)

    def deleteKeyword(self, keyword):
        self.root = self.deleteNode(self.root, keyword)

    def updateKeyword(self, keyword, newMeaning):
        self.deleteKeyword(keyword)
        self.addKeyword(keyword, newMeaning)

    def display(self, ascending=True):
        result = []
        self.inorder(self.root, result)
        if not ascending:
            result.reverse()
        for keyword, meaning in result:
            print(f"{keyword}: {meaning}")

    def findKeywordWithComparisons(self, keyword):
        comparisons = 0
        found, comparisons = self.findKeyword(self.root, keyword, comparisons)
        if found:
            print(f"Keyword found with {comparisons} comparisons.")
        else:
            print(f"Keyword not found.")

def main():
    dictionary = AVLTree()

    while True:
        print("\n1. Add Keyword\n2. Delete Keyword\n3. Update Keyword\n4. Display Dictionary (Ascending)\n5. Display Dictionary (Descending)\n6. Find Keyword\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            keyword = input("Enter the keyword: ")
            meaning = input("Enter the meaning: ")
            dictionary.addKeyword(keyword, meaning)
        elif choice == 2:
            keyword = input("Enter the keyword to delete: ")
            dictionary.deleteKeyword(keyword)
        elif choice == 3:
            keyword = input("Enter the keyword to update: ")
            newMeaning = input("Enter the new meaning: ")
            dictionary.updateKeyword(keyword, newMeaning)
        elif choice == 4:
            print("\nDisplaying Dictionary in Ascending Order:")
            dictionary.display(ascending=True)
        elif choice == 5:
            print("\nDisplaying Dictionary in Descending Order:")
            dictionary.display(ascending=False)
        elif choice == 6:
            keyword = input("Enter the keyword to find: ")
            dictionary.findKeywordWithComparisons(keyword)
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
