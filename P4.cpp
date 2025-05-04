#include <iostream>
#include <stack>

using namespace std;

struct Exnode {
    char data{};
    Exnode *left = nullptr;
    Exnode *right = nullptr;
};

class Extree {
public:
    char *add(Exnode **temp, char *arr) {
        if (*arr == '\0')
            return nullptr;

        while (true) {
            char *q;
            if (*temp == nullptr) {
                Exnode *n = (Exnode *) malloc(sizeof(Exnode));
                n->data = *arr;
                n->left = nullptr;
                n->right = nullptr;
                *temp = n;
            } else {
                if ((*arr >= 'a' && *arr <= 'z') || (*arr >= 'A' && *arr <= 'Z')) {
                    return arr;
                }
                q = add(&(*temp)->left, arr + 1);
                q = add(&(*temp)->right, q + 1);
                return q;
            }
        }
    }

    void postorder(Exnode *temp) {
        if (temp != nullptr) {
            stack<Exnode *> s;
            s.push(temp);
            stack<char> out;
            while (!s.empty()) {
                Exnode *curr = s.top();
                s.pop();
                out.push(curr->data);
                if (curr->left) {
                    s.push(curr->left);
                }
                if (curr->right) {
                    s.push(curr->right);
                }
            }
            while (!out.empty()) {
                cout << out.top() << " ";
                out.pop();
            }
        } else {
            cout << "Tree is empty!" << endl;
        }
    }

    void deleteTree(Exnode*& root) {
        if (root == nullptr)
            return;
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
        root = nullptr;
    }
};

int main() {
    int ch;
    char a[20];
    Extree obj;
    Exnode *trees[2] = {nullptr, nullptr};  
    cout << "1. Insert\n2. Display\n3. Delete tree\n4. Exit" << endl;

    do {
        cout << "\nChoice: ";
        cin >> ch;
        switch (ch) {
            case 1:
                for (int i = 0; i < 2; i++) {  
                    cout << "Enter Prefix Expression " << i + 1 << ": ";
                    cin >> a;
                    obj.add(&trees[i], a);
                }
                break;
            case 2:
                for (int i = 0; i < 2; i++) {  
                    cout << "Postorder traversal of tree " << i + 1 << ": ";
                    obj.postorder(trees[i]);
                    cout << endl;
                }
                break;
            case 3:
                for (int i = 0; i < 2; i++) {  
                    obj.deleteTree(trees[i]);
                }
                cout << "Both Trees Successfully Deleted" << endl;
                break;
            case 4:
                cout << "\nExiting..." << endl;
                exit(0);
            default:
                cout << "Incorrect Choice!!";
        }
    } while (ch != 4);

    return 0;
}

