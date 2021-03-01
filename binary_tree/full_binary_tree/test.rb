class Node
  attr_accessor :data, :left, :right
  def initialize(data)
    @data = data
  end
end

def isFullTree(root)
  if !root
    return true
  end

  if !root.left && !root.right
    return true
  end

  if root.left && root.right
    return isFullTree(root.left) & isFullTree(root.right)
  end

  return false
end

root = Node.new(10)
root.left = Node.new(20)
root.right = Node.new(30)

root.left.right = Node.new(40)
root.left.left = Node.new(50)
root.right.left = Node.new(60)
root.right.right = Node.new(70)

root.left.left.left = Node.new(80)
root.left.left.right = Node.new(90)
root.left.right.left = Node.new(80)
root.left.right.right = Node.new(90)
root.right.left.left = Node.new(80)
root.right.left.right = Node.new(90)
root.right.right.left = Node.new(80)
root.right.right.right = Node.new(90)

puts "The tree is a full binary tree?: ", isFullTree(root)