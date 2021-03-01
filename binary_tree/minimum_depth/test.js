function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
};

function minDepth(root) {
  if (!root) {
    return 0;
  };

  if (!root.left && !root.right) {
    return 1;
  };

  if (!root.left) {
    return minDepth(root.right) + 1;
  };

  if (!root.right) {
    return minDepth(root.left) + 1;
  };

  return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
};

var root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);
console.log(minDepth(root));

var root2 = new Node(1);
root2.left = new Node(2);
root2.left.left = new Node(4);
root2.left.right = new Node(5);
console.log(minDepth(root2));





function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
};

function minDepth(root) {
  if (!root) {
    return 0;
  };

  var q = [];

  q.push({'node': root, 'depth': 1});

  while(q.length > 0) {
    var queueItem = q.shift();
    var node = queueItem['node'];
    var depth = queueItem['depth'];

    if (!node.left && !node.right) {
      return depth;
    };

    if (node.left) {
      q.push({'node': node.left, 'depth': depth+1});
    };

    if (node.right) {
      q.push({'node': node.right, 'depth': depth+1});
    };
  };
};


var root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);
console.log(minDepth(root));

var root2 = new Node(1);
root2.left = new Node(2);
root2.left.left = new Node(4);
root2.left.right = new Node(5);
console.log(minDepth(root2));