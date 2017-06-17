class Node
  attr_accessor :char, :next

  def initialize(char)
    @char = char
    @next = nil
  end
end


def compare(list1, list2)

  while(list1 && list2 && list1.char == list2.char)
    list1 = list1.next
    list2 = list2.next
  end

  if(list1 && list2)
    return (list1.char > list2.char) ? 1 : -1
  end

  if(list1 && !list2)
    return 1
  end

  if(list2 && !list1)
    return -1
  end

  return 0
end


list1 = Node.new('g')
list1.next = Node.new('e')
list1.next.next = Node.new('e')
list1.next.next.next = Node.new('k')
list1.next.next.next.next = Node.new('s')
list1.next.next.next.next.next = Node.new('a')

list2 = Node.new('g')
list2.next = Node.new('e')
list2.next.next = Node.new('e')
list2.next.next.next = Node.new('k')
list2.next.next.next.next = Node.new('s')
list2.next.next.next.next.next = Node.new('b')

puts compare(list1,list2)

list3 = Node.new('g')
list3.next = Node.new('e')
list3.next.next = Node.new('e')
list3.next.next.next = Node.new('k')
list3.next.next.next.next = Node.new('s')

puts compare(list1, list3)
puts compare(list3, list3)