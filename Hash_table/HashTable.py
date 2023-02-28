class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

class HashTable:

    def __init__(self,size):
        self.capacity = size
        self.size = 0
        self.buckets = [None] * self.capacity


    def size(self):
        return self.size

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return
    
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result



#1 write a function to determine whether a string contains repeated characters using hash table

def repeated_char(string):
    hash_table = HashTable(128)
    for char in string:
        if hash_table.find(char) is not None:
            return True
        else:
            hash_table.insert(char, True)
    return False

#print(repeated_char("hello"))

#2 Given a string of any length, find the most-used character in the string using hash table

def most_used_char(string):
    hash_table = HashTable(128)
    max_char = None
    max_count = 0
    for char in string:
        if hash_table.find(char) is None:
            hash_table.insert(char, 1)
        else:
            count = hash_table.find(char)
            count += 1
            hash_table.insert(char, count)
        if hash_table.find(char) > max_count:
            max_count = hash_table.find(char)
            max_char = char
    return max_char

#print(most_used_char("hello"))

#3 Write a function to determine whether two strings are anagrams using hash table

def anagram(string1, string2):
    hash_table1 = HashTable(128)
    hash_table2 = HashTable(128)
    for char in string1:
        if hash_table1.find(char) is None:
            hash_table1.insert(char, 1)
        else:
            count = hash_table1.find(char)
            count += 1
            hash_table1.insert(char, count)
    for char in string2:
        if hash_table2.find(char) is None:
            hash_table2.insert(char, 1)
        else:
            count = hash_table2.find(char)
            count += 1
            hash_table2.insert(char, count)
    for char in string1:
        if hash_table1.find(char) != hash_table2.find(char):
            return False
    return True

print(anagram("hello", "ollhe"))