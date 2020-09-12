/*
description: Improving the functions and added my own functions
reference url: http://www.thatjsdude.com/interview/linkedList.html
reference github: https://github.com/khan4019/front-end-Interview-Questions
*/

//// Doubly linked list
function DoublyLinkedList() {
  this.head = null;
};

DoublyLinkedList.prototype.push = function (data) {

  var head = this.head;
  var current = head;
  var previous = head;

  // if there is no head
  if (!head) {
    this.head = { 'data': data, 'previous': null, 'next': null };
  }
  else {
    while (current.next) {
      previous = current;
      current = current.next;
    };

    current.next = { 'data': data, 'previous': current, 'next': null };
  };
};

doubList = new DoublyLinkedList();
doubList.push(1);
doubList.push(2);
doubList.push(3);


//// Reverse doubly linked list
function reverseDoublyLinkedList(dll) {
  var head = dll.head;
  var current = dll.head;
  var temp;

  while (current) {

    // reverse the node sequence
    temp = current.next;
    current.next = current.previous;
    current.previous = temp;

    // when it is the last node
    if (!temp) {
      // set last node as head
      dll.head = current;
    };

    // move pointer to next node
    current = temp;
  };
};

doubList = new DoublyLinkedList();
doubList.push(1);
doubList.push(2);
doubList.push(3);
reverseDoublyLinkedList(doubList);


/*
//// Delete a node from doubly LL
C1: DELETE HEAD, make 2nd node the head, set the previous of new head as null
C2: NODE IN THE MIDDLE, skip break the chain, skip current node. 
    hence next of previous node would be the next of the current node. 
    Besides, previous of the next node would be previous node
C3: DELETE TAIL, make the next of 2nd last node as null
C4: DON'T FIND, don't do anything
*/
function deleteNodeDLL(dll, data) {
  var current = dll.head;
  var previous;

  // C1
  if (current.data == data) {
    dll.head = current.next;
    // if there is only 1 node, the head will be null
    if (dll.head) {
      dll.head.previous = null;
    };
    return dll;
  };

  // C2
  while (current.next) {
    if (current.data == data) {
      previous.next = current.next;
      current.next.previous = previous;
      return dll;
    };

    previous = current;
    current = current.next;
  };

  // C3
  if (current.data == data) {
    previous.next = null;
  };

  return dll;
};

doubList = new DoublyLinkedList();
doubList.push(1);
doubList.push(2);
doubList.push(3);
deleteNodeDLL(doubList, 1);