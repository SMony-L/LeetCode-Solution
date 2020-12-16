#include <string>
#include <iostream>
#include <stack>
#include <cstdlib>
#include <map>
using namespace std;

class Solution {
public:
    // Using stack
    // bool isValid(string s) {
    //     stack<char> myStack;
    //     for(int i = 0; i < s.length(); i++) {
    //         switch (s[i]) {
    //             case '(':
    //             case '[':
    //             case '{': myStack.push(s[i]); break;
    //             case ')': if (myStack.empty() || myStack.top() != '(') return false; else myStack.pop(); break;
    //             case ']': if (myStack.empty() || myStack.top() != '[') return false; else myStack.pop(); break;
    //             case '}': if (myStack.empty() || myStack.top() != '{') return false; else myStack.pop(); break;
    //             default: ;
    //         }
    //     }
    //     if (myStack.size() == 0) return true;
    //     return false;
    // }


    bool isValid(string s) {
        map<char, char> myMap={{'(', ')'}, {'[', ']'}, {'{', '}'}};
        stack<char> myStack;

        for (const char& c: s) {
            if (myMap.find(c) != myMap.end()) {
                myStack.push(c);
            } else {
                if (myStack.empty() || myMap[myStack.top()] != c) {
                    return false;
                }
                myStack.pop();
            }
        }
        return myStack.empty();
    }
};

int main() {
    string s = "[{()}]";
    Solution result;
    if (result.isValid(s) == 1) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }

    return 0;
}