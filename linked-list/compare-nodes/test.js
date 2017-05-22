function Node(char) {
  this.char = char;
  this.next = null;
};

function compare(list1, list2) {

  // Traverse both lists. Stop when either end of linked 
  // list is reached or current char don't watch
  while(list1 && list2 && list1.char == list2.char) {
    list1 = list1.next;
    list2 = list2.next;
  }

  // If both lists are not empty, compare mismatching
  // char
  if(list1 && list2) {
    return (list1.char > list2.char) ? 1 : -1
  }

  // if list1 is not empty but list2 is
  if(list1 && !list2) {
    return 1;
  };

  if(list2 && !list1) {
    return -1;
  }

  // both list have exact char
  return 0;
};

var list1 = new Node('g');
list1.next = new Node('e');
list1.next.next = new Node('e');
list1.next.next.next = new Node('k');
list1.next.next.next.next = new Node('s');
list1.next.next.next.next.next = new Node('a');

var list2 = new Node('g');
list2.next = new Node('e');
list2.next.next = new Node('e');
list2.next.next.next = new Node('k');
list2.next.next.next.next = new Node('s');
list2.next.next.next.next.next = new Node('b');

compare(list1,list2);

var list3 = new Node('g');
list3.next = new Node('e');
list3.next.next = new Node('e');
list3.next.next.next = new Node('k');
list3.next.next.next.next = new Node('s');

compare(list1, list3);
compare(list3, list3);