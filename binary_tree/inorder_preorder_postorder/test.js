function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
};

function inorderPrint(root) {
  if(root) {
    inorderPrint(root.left);
    console.log(root.data);
    inorderPrint(root.right);
  };
};

function preorderPrint(root) {
  if(root) {
    console.log(root.data);
    preorderPrint(root.left);
    preorderPrint(root.right);
  };
};

function postorderPrint(root) {
  if(root) {
    postorderPrint(root.left);
    postorderPrint(root.right);
    console.log(root.data);
  };
};


// test code
var root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);

console.log('Inorder traversal of BT is:')
inorderPrint(root)

console.log('Preorder traversal of BT is:')
preorderPrint(root)

console.log('Postorder traversal of BT is:')
postorderPrint(root)
