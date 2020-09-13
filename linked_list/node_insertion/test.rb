# class Node
#   attr_accessor :data, :next

#   def initialize(data)
#     self.data = data
#     self.next = nil
#   end
# end

# class LinkedList
#   attr_accessor :head

#   def initialize
#     self.head = nil
#   end

#   def sortedInsert(new_node)
#     if(!self.head)
#       self.head = new_node

#     elsif(self.head.data >= new_node.data)
#       new_node.next = self.head
#       self.head = new_node

#     else
#       current = self.head
#       while(current.next && current.next.data < new_node.data)
#         current = current.next
#       end

#       new_node.next = current.next
#       current.next = new_node
#     end
#   end

#   def push(new_data)
#     new_node = Node.new(new_data)
#     new_node.next = self.head
#     self.head = new_node
#   end

#   def printList
#     temp = self.head
#     while(temp)
#       puts temp.data
#       temp = temp.next
#     end
#   end
# end


class Node
  attr_accessor :data, :next

  def initialize(data)
    @data = data
    @next = nil
  end
end

class LinkedList
  attr_accessor :head

  def initialize
    @head = nil
  end

  def sortedInsert(new_node)
    if(!@head)
      @head = new_node

    elsif(@head.data >= new_node.data)
      new_node.next = @head
      @head = new_node

    else
      current = @head
      while(current.next && current.next.data < new_node.data)
        current = current.next
      end

      new_node.next = current.next
      current.next = new_node
    end
  end

  def push(new_data)
    new_node = Node.new(new_data)
    new_node.next = @head
    @head = new_node
  end

  def printList
    temp = @head
    while(temp)
      puts temp.data
      temp = temp.next
    end
  end
end


llist = LinkedList.new()
new_node = Node.new(5)
llist.sortedInsert(new_node)
new_node = Node.new(10)
llist.sortedInsert(new_node)
new_node = Node.new(7)
llist.sortedInsert(new_node)
new_node = Node.new(3)
llist.sortedInsert(new_node)
new_node = Node.new(1)
llist.sortedInsert(new_node)
new_node = Node.new(9)
llist.sortedInsert(new_node)
llist.printList()