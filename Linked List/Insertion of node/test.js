//// JS function version
function Node(data) {
  this.data = data;
  this.next = null;
};

function LinkedList() {

  this.head = null;

  this.sortedInsert = function(new_node) {

    // To ensure that node/object is inserted
    if(typeof new_node !== "object") {
      console.error("Please insert a Node");
    }
    else if(this.head == null) {
      this.head = new_node
    }
    else if(this.head.data >= new_node.data) {
      new_node.next = this.head;
      this.head = new_node;
    }
    else {
      current = this.head
      while(current.next && current.next.data < new_node.data) {
        current = current.next;
      };

      new_node.next = current.next;
      current.next = new_node;
    };
  };

  this.nodePush = function(new_data) {
    new_node = new Node(new_data);
    new_node.next = this.head;
    this.head = new_node;
  };

  //// 1st method to print
  // this.printList = function() {
  //   temp = this.head;
  //   while(temp) {
  //     console.log(temp.data);
  //     temp = temp.next;
  //   };
  // };

  // 2nd method to print
  this.printList = function() {
    let temp = this.head;
    let tempArray = [];
    while(temp) {
      tempArray.push(temp.data)
      temp = temp.next;
    };
    console.log('Array: ', tempArray);
  };
};


//// ES6 class version
// class Node {
//   constructor(data) {
//     this.data = data;
//     this.next = null;
//   };
// };

// class LinkedList {
//   constructor() {
//     this.head = null;
//   };

//   sortedInsert(new_node) {

//     if(typeof new_node !== 'object') {
//       console.error('Please insert a Node');
//     }
//     else if(!this.head) {
//       this.head = new_node;
//     }
//     else if(this.head.data >= new_node.data) {
//       new_node.next = this.head;
//       this.head = new_node;
//     }
//     else {
//       var current = this.head
//       while(current.next && current.next.data < new_node.data) {
//         current = current.next;
//       };

//       new_node.next = current.next;
//       current.next = new_node;
//     };
//   };

//   nodePush(new_data) {
//     new_node = new Node(new_data);
//     new_node.next = this.head;
//     this.head = new_node;
//   };

//   printList() {
//     let temp = this.head;
//     let tempArray = [];
//     while(temp) {
//       tempArray.push(temp.data)
//       temp = temp.next;
//     };
//     console.log('Array: ', tempArray);
//   };
// };

// 1st method to create list
llist = new LinkedList();
new_node = new Node(5);
llist.sortedInsert(new_node);
new_node = new Node(10);
llist.sortedInsert(new_node);
new_node = new Node(7);
llist.sortedInsert(new_node);
new_node = new Node(3);
llist.sortedInsert(new_node);
new_node = new Node(1);
llist.sortedInsert(new_node);
new_node = new Node(9);
llist.sortedInsert(new_node);
llist.printList();

// 2nd method to create list
// The list will not be sorted
llist = new LinkedList();
llist.nodePush(5);
llist.nodePush(10);
llist.nodePush(7);
llist.nodePush(3);
llist.nodePush(1);
llist.nodePush(9);
llist.printList();