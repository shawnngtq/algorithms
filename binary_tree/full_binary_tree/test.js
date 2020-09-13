function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
};

function isFullTree(root) {
  if (!root) { return true; };

  if (!root.left && !root.right) { return true; };

  if (root.left && root.right) { return isFullTree(root.left) && isFullTree(root.right); };

  return false;
};


var root = new Node(10);
root.left = new Node(20);
root.right = new Node(30);

root.left.right = new Node(40);
root.left.left = new Node(50);
root.right.left = new Node(60);
root.right.right = new Node(70);

root.left.left.left = new Node(80);
root.left.left.right = new Node(90);
root.left.right.left = new Node(80);
root.left.right.right = new Node(90);
root.right.left.left = new Node(80);
root.right.left.right = new Node(90);
root.right.right.left = new Node(80);
root.right.right.right = new Node(90);

console.log("The tree is a full binary tree?: ", isFullTree(root));