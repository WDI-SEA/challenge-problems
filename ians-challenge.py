# for howver many friends, make a list out of them
# k poping friendsd out of list 
# some of logic loop to first friend

class Friend():
    def __init__(self, name, next):
        self.name = name
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def insert(self, data):
        if self.size == 0:
            self.head = Friend(data, None)
            self.tail = self.head
        else:
            new_friend = Friend(data, self.head)
            self.tail.next = new_friend
            self.tail = new_friend
        self.size += 1

    def pop_after(self, search_friend):
        current_friend = self.head
        while current_friend:
            if current_friend == search_friend:
                current_friend.next = current_friend.next.next
                self.size -= 1
            else:
                current_friend = current_friend.next

def circular_list(friends, count):
    friend_list = LinkedList()
    for num in range(1, friends + 1):
        friend_list.insert(num)
    current_friend = friend_list.head

    while len(friend_list) > 1:
        pass
    
def circular_game(friends, k, index = 0):
    k -= 1
    friend_list = []
    for num in range(0, friends):
        friend_list.append(num)
    print(friend_list)

    while len(friend_list) > 1:
        index += k
        if index >= len(friend_list):
            index %= len(friend_list)
        friend_list.pop(index)
        print(friend_list)
        
    return friend_list[0]

# print(circular_game(5, 2))
# print(circular_game(6, 5))