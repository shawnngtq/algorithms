//// JS function method
function Node(data) {
  this.data = data;
  this.next = null;
};

function LinkedList() {

  this.head = null;

  this.deleteNode = function(node1, node2) {
    
    // When given params are not object
    if(typeof node1 !== 'object' || typeof node2 !== 'object') {
      console.error('The parameters/pointers must be Node');
    }
    // When head node is to be deleted
    else if(node1 == node2) {
      if(!node1.next) {
        console.error('The linked list can\'t be empty');
      };

      // copy the data of next data to head
      node1.data = node1.next.data;

      // store address of next node
      node2 = node1.next;

      // remove link of next node
      node1.next = node1.next.next;
      return;
    };

    var prev = node1;
    // go to next node until it is 1 node before the node to delete
    while(prev.next && prev.next !== node2) {
      prev = prev.next;
    };

    // if the node is the last & it is not the node to delete
    // it means that the node to delete doesn't exist
    if(prev.next == null) {
      console.error('The node to delete doesn\'t exist');
    };

    prev.next = prev.next.next;
  };
};

llist = new LinkedList();
llist.head = new Node(12);
llist.head.next = new Node(15);
llist.head.next.next = new Node(10);
llist.head.next.next.next = new Node(11);
llist.head.next.next.next.next = new Node(5);
llist.head.next.next.next.next.next = new Node(6);
llist.head.next.next.next.next.next.next = new Node(2);
llist.head.next.next.next.next.next.next.next = new Node(3);

llist.deleteNode(llist.head, llist.head);
llist.deleteNode(llist.head, llist.head.next.next);