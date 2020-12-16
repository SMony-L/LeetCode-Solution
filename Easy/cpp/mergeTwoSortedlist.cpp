/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <cstddef> 
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    // Recursive
    // ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    //     if (l1 == NULL && l2 == NULL) {
    //         return NULL;
    //     }
    //     if (l1 == NULL) {
    //         return l2;
    
    //     }
    //     if (l2 == NULL) {
    //         return l1;
    //     }

    //     if (l1->val < l2->val) {
    //         l1->next = mergeTwoLists(l1->next,l2);
    //         return l1;
    //     }
    //     else {
    //         l2->next = mergeTwoLists(l1, l2->next);
    //         return l2;
    //     }
    // }
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        if (l1 == NULL && l2 == NULL) {
            return NULL;
        }
        if (l1 == NULL) {
            return l2;
    
        }
        if (l2 == NULL) {
            return l1;
        }
        
        while(l1 != NULL & l2 != NULL){

            if (l1->val < l2->val) {
                curr->next = l1;
                l1 = l1->next;
  
            } else {
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;

        }
        
        if(l1 == NULL) {
            curr->next = l2;
        }
        else {
            curr->next = l1;
        }
        return head->next;
        
    }
    void printList(ListNode* n) {
        while (n != NULL) {
            cout << n->val << " ";
            n = n->next;
        }
    }
};

int main() {
    ListNode* head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(4);

    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(3);
    head2->next->next = new ListNode(4);

    ListNode* mergedList = Solution().mergeTwoLists(head1,head2);

    Solution().printList(mergedList);
}