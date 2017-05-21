/*
description: Improving the functions and added my own functions
reference url: http://www.thatjsdude.com/interview/linkedList.html
reference github: https://github.com/khan4019/front-end-Interview-Questions
*/

//// Singly linked list
function SinglyLinkedList() {
  this.head = null;
};


//// Add node to Singly linked list
SinglyLinkedList.prototype.push = function(data) {
  var node = {
    'data': data,
    'next': null
  };

  // if there is no head, make new node the head
  if(!this.head) {
    this.head = node;
  }
  else {

    var current = this.head;

    // find the tail of linked list
    while(current.next) {
      current = current.next;
    };

    // put the new node at the tail
    current.next = node;
  };
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.head;
singList.head.next;
singList.head.next.next;


/*
//// Remove node from Singly linked list
C1: Targeted node is head
C2: Targeted node is tail
C3: Targeted node is neither head nor tail
*/
SinglyLinkedList.prototype.remove = function(data) {
  var current = this.head;

  // C1
  if(current.data == data) {
    this.head = current.next;
  }
  else {
    var previous = current;

    // So long there is a subsequent node
    while(current.next) {

      // C3
      // if current node is the targeted node
      if(current.data == data) {
        // skip the current node
        previous.next = current.next;
        break;
      }

      previous = current;
      current = current.next;
    };

    // C2
    (current.data == data) && (previous.next = null);
    // (current.data == data) ? (previous.next = null) : (console.error("No such node exist"));
  };
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.remove(1);
console.log(singList);
singList.remove(4);


//// Reverse Singly linked list
function reverseSinglyLinkedList(sll) {
  
  if(!sll.head) {
    console.error("This is not a linked list");
  }
  else if(!sll.head.next) {
    console.log("There is only 1 node in the linked list");
  }
  else {
    console.log("This is a linked list with at least 1 node");
  };

  var nodes = [];
  var current = sll.head;

  // store all the nodes (object) in an array
  while(current) {
    nodes.push(current);
    current = current.next;
  };

  var reversedSLL = new SinglyLinkedList();

  reversedSLL.head = nodes.pop();
  current = reversedSLL.head;

  var node = nodes.pop();
  //make sure to make next of the newly inserted node to be null
  //other wise the last node of your SLL will retain its old next.
  while(node) {
    node.next = null;
    current.next = node;

    current = current.next;
    node = nodes.pop();
  };

  return reversedSLL;
}

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
reverseSinglyLinkedList(singList);


//// kth node from end
function kthNodeFromEnd(sll, k) {
  var node = sll.head;
  var i = 1;
  var kthNode;

  // make sure k > 0
  if(k <= 0) {
    console.error("k must be greater than 0");
    return;
  };

  // until there is no more node
  while(node) {
    if(k == i) {
      kthNode = sll.head;
    }
    else if(i - k > 0) {
      kthNode = kthNode.next;
    };

    i++;
    node = node.next;
  };

  return kthNode;
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
kthNodeFromEnd(singList, 0);
kthNodeFromEnd(singList, 1);
kthNodeFromEnd(singList, 3);


//// delete kth node from end
function deletekthNodeFromEnd(sll, k) {
  var node = sll.head;
  var i = 1;
  var kthNode;
  var previous;

  if(k <= 0) {
    console.error("k must be greater than 0");
    return;
  };

  while(node) {
    if(k == i) {
      kthNode = sll.head;
    }
    else if(i - k > 0) {
      previous = kthNode;
      kthNode = kthNode.next;
    };

    i++;
    node = node.next;
  };

  //kth node is the head
  if(!previous)
    sll.head = sll.head.next;
  else{
    previous.next = kthNode.next;
  }
  return sll;
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
deletekthNodeFromEnd(singList, 1);


//// Detect a infinite loop in Singly Linked List
function detectInfLoop(sll) {
  var slowPointer = sll.head;
  var fastPointer = sll.head;

  while(slowPointer && fastPointer && fastPointer.next) {
    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next.next;

    if(slowPointer == fastPointer) {
      return true;
    };
  };
  return false;
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
detectInfLoop(singList);

singList.head.next.next.next.next.next = singList.head.next.next
detectInfLoop(singList);


//// Detect Node where infinite loop started
function findInfLoopStart(sll) {
  var slowPointer = sll.head;
  var fastPointer = sll.head;

  while(slowPointer && fastPointer) {
    // move slowPointer by 1 step
    slowPointer = slowPointer.next;

    // if fast is null, it means there's no infinite loop
    if(!fastPointer.next) {
      return null;
    };

    // move fastPointer by 2 steps
    // fastPointer is 1 step ahead of slowPointer
    fastPointer = fastPointer.next.next;

    // if slowPointer node is same as the following node
    if(slowPointer == fastPointer) {
      slowPointer = sll.head;
      while(slowPointer != fastPointer) {
        slowPointer = slowPointer.next;
        fastPointer = fastPointer.next;
      };
      return slowPointer;
    };
  };
};




////////////////////////////////////////
/*
100% COMPLETELY MY CODE
*/

//// number of node
function countNodeSLL(sll) {
  var node = sll.head;
  var count = 0;

  while(node) {
    node = node.next;
    count += 1;
  };

  return count;
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
countNodeSLL(singList);


//// replicate nodes of singly linked list into a list
function replicateNodesSLL(sll) {
  var node = sll.head
  var nodesList = [];

  // empty linked list?
  if(node == null) {
    console.log("This is an empty linked list");
    return;
  };

  while(node) {
    nodesList.push({data: node.data, next: node.next});
    node = node.next
  };

  return nodesList;
};

var singList = new SinglyLinkedList();
singList.push(1);
singList.push(2);
singList.push(3);
singList.push(4);
singList.push(5);
replicateNodesSLL(singList);


//// find the middle node
function middleNodeSLL(sll) {
};