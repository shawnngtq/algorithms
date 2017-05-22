function Node(data) {
  this.data = data;
  this.next = null;
};

function sumLinkedListNodes(list1, list2) {
  var value1 = '';
  var value2 = '';
  var head1 = list1;
  var head2 = list2;

  // two instead of one while loop
  // becaue 1st & 2nd linked list might not be same length
  while(head1) {
    value1 += head1.data;
    head1 = head1.next;
  };

  while(head2) {
    value2 += head2.data;
    head2 = head2.next;
  };

  // finding the sum
  var sum = (+value1) + (+value2);
  sum += '';

  // resultant list's nodes' data
  var list3Data = sum.split('');

  // resultant list
  var list3 = {head: new Node(+list3Data[0])};

  var current = list3.head;
  var i = 1, len = list3Data.length;
  for(i; i < len; i++) {
    current.next = new Node(+list3Data[i]);
    current = current.next;
  };

  return list3;
};


var list1 = new Node(5);
list1.next = new Node(6);
list1.next.next = new Node(3);

var list2 = new Node(8);
list2.next = new Node(4);
list2.next.next = new Node(2);

sumLinkedListNodes(list1, list2);