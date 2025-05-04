#include <iostream>
using namespace std;

struct node {
    node *LC;
    int data;
    node *RC;
};

class BST {
    node *root;
    int count;

public:
    BST() {
        root = NULL;
        count = 0;
    }

    node* getroot() {
        return root;
    }

    void addNode(int v) {
        node *p = new node;
        p->data = v;
        p->LC = p->RC = NULL;

        if (root == NULL) {
            root = p;
            return;
        }

        node *cur = root, *q = NULL;
        while (cur) {
            q = cur;
            if (v == cur->data) {
                cout << "\nDuplicate Node!";
                return;
            }
            cur = (v < cur->data) ? cur->LC : cur->RC;
        }

        if (v < q->data) q->LC = p;
        else q->RC = p;
    }

    void displayIN(node *T) {
        if (T) {
            displayIN(T->LC);
            cout << " " << T->data;
            displayIN(T->RC);
        }
    }

    int height(node *T) {
        if (!T) return 0;
        int lh = height(T->LC);
        int rh = height(T->RC);
        return max(lh, rh) + 1;
    }

    void minimumDataValue(node *T) {
        if (!T) {
            cout << "\nTree Empty";
            return;
        }
        while (T->LC) T = T->LC;
        cout << "Minimum data value is: " << T->data;
    }

    void Mirror(node *T) {
        if (T) {
            swap(T->LC, T->RC);
            Mirror(T->LC);
            Mirror(T->RC);
        }
    }

    void searchNode(int v) {
        node *cur = root;
        count = 0;
        while (cur) {
            count++;
            if (v == cur->data) {
                cout << "\nNode Found after " << count << " comparisons";
                return;
            }
            cur = (v < cur->data) ? cur->LC : cur->RC;
        }
        cout << "\nNode with " << v << " not found after " << count << " comparisons";
    }
};

int main() {
    BST B;
    int val, cho = 0;
    while (cho != 7) {
        cout << "\n1. Add Node\n2. Display Inorder\n3. Height\n4. Min Value\n5. Mirror\n6. Search\n7. Exit\nEnter choice: ";
        cin >> cho;
        switch (cho) {
            case 1:
                cout << "Enter value: ";
                cin >> val;
                B.addNode(val);
                break;
            case 2:
                B.displayIN(B.getroot());
                break;
            case 3:
                cout << "Height (Longest path nodes): " << B.height(B.getroot());
                break;
            case 4:
                B.minimumDataValue(B.getroot());
                break;
            case 5:
                B.Mirror(B.getroot());
                cout << "Tree mirrored.";
                break;
            case 6:
                cout << "Enter value to search: ";
                cin >> val;
                B.searchNode(val);
                break;
            case 7:
                cout << "Program Exits!";
                break;
            default:
                cout << "Invalid choice!";
        }
    }
    return 0;
}
