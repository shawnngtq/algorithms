var res;

function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
};

function findMaxPath(root) {
  if(!root) { return 0; };

  var l = findMaxPath(root.left);
  var r = findMaxPath(root.right);

  var max_single = Math.max(root.data, root.data+Math.max(l,r));

  var max_top = Math.max(max_single, l+r+root.data);

  res = Math.max(res, max_top);

  return max_single;
};

function findMaxSum(root) {
  res = -Infinity;

  findMaxPath(root);

  return res;
};


var root = new Node(10);
root.left = new Node(-2);
root.right = new Node(10);
console.log("Max path sum is ", findMaxPath(root));

var root = new Node(10);
root.left = new Node(2);
root.right = new Node(10);
root.left.left = new Node(20);
root.left.right = new Node(1);
root.right.right = new Node(-25);
root.right.right.left = new Node(3);
root.right.right.right = new Node(4);
console.log("Max path sum is ", findMaxSum(root));