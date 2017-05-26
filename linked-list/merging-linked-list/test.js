function Node(data) {
  this.data = data;
  this.next = null;
};

function LinkedList() {
  this.head = null;
  this.count = 0;
  var current;

  this.nodePush = function(data) {
    var new_node = new Node(data);
    this.count += 1;

    if(!this.head) {
      this.head = new_node;
    }
    else {
      current = this.head;
      while(current.next) {
        current = current.next;
      }
      current.next = new_node;
    };
  };

  this.printList = function() {
    var temp = [];
    var current = this.head;
    while(current) {
      temp.push(current.data);
      current = current.next;
    };
    console.log(temp);
  };
};

function mergeLinkedList(list1, list2) {

  // C1: 1 of the list is empty
  // no change to the linked list
  if(list1.count == 0 || list2.count == 0) {
    console.log('1 of the list is empty');
  }

  var head1 = list1.head;
  var head2 = list2.head;

  // C2: both lists are of the same length
  while(head1 && head2) {
    var next1;
    var next2;

    next1 = head1.next;
    next2 = head2.next;

    head2.next = next1;
    head1.next = head2;

    head1 = next1;
    head2 = next2;
  };

  list2.head = head2;

  // Counting of the number of nodes is not dynamic
  if(list1.count >= list2.count) {
    list1.count += list2.count;
    list2.count = 0;
  }
  else if(list1.count < list2.count) {
    list2.count = list2.count - list1.count;
    list1.count *= 2;
  };
};

var list1 = new LinkedList();
list1.nodePush(5);
list1.nodePush(7);
list1.nodePush(17);
list1.nodePush(13);
list1.nodePush(11);
list1.printList();

var list2 = new LinkedList();
list2.nodePush(12);
list2.nodePush(10);
list2.nodePush(2);
list2.nodePush(4);
list2.nodePush(6);
list2.printList();

var list3 = new LinkedList();

var list4 = new LinkedList();
list4.nodePush(1);
list4.nodePush(2);
list4.nodePush(3);

var list5 = new LinkedList();
list5.nodePush(4);
list5.nodePush(5);
list5.nodePush(6);
list5.nodePush(7);
list5.nodePush(8);

// when 2 linked lists are of equal length
mergeLinkedList(list1, list2);
// when 1 of the linked list is empty
mergeLinkedList(list1, list3);
// when 1st linked list is shorter than 2nd list
mergeLinkedList(list4, list5);