# An animal shelter, which holds only dogs and cats, operated on a strictly "first in, first out" basis. 
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter or they can select
# whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create a data structure to maintain this system with operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.

class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.next = None

class AnimalQueue:
    def __init__(self):
        self.oldest = None
        self.newest = None

    def enqueue(self, type, name):
        animal = Animal(type, name)
        if not self.oldest:
            self.oldest = animal
        if self.newest:
            self.newest.next = animal
        self.newest = animal

    def dequeueAny(self):
        if self.oldest:
            name = self.oldest.name
            self.oldest = self.oldest.next
            return name
        return None
    
    def dequeueType(self, type):
        if self.oldest:

            # oldest is the right type
            if self.oldest.type == type:
                return self.dequeueAny()

            # find the oldest of the right type
            prev = self.oldest
            curr = self.oldest.next
            while curr:
                if curr.type == type:
                    name = curr.name
                    prev.next = curr.next
                    return name
                prev = prev.next
                curr = curr.next

        return None

    def dequeueDog(self):
        return self.dequeueType("dog")

    def dequeueCat(self):
        return self.dequeueType("cat")

# Alternative: two seperate queues, each animal stores the order (timestamp) when it was enqueued
# faster dequeue, requires more space
class Animal1:
    def __init__(self, type, name, order):
        self.type = type
        self.order = order
        self.name = name
        self.next = None

class AnimalQueue1:
    def __init__(self):
        self.oldest_dog = None
        self.newest_dog = None
        self.oldest_cat = None
        self.newest_cat = None
        self.order = 0

    def enqueue(self, type, name):
        if type == "dog":
            dog = Animal1("dog", name, self.order)
            self.order += 1

            if not self.oldest_dog:
                self.oldest_dog = dog
            if self.newest_dog:
                self.newest_dog.next = dog
            self.newest_dog = dog

        if type == "cat":
            cat = Animal1("cat", name, self.order)
            self.order += 1

            if not self.oldest_cat:
                self.oldest_cat = cat
            if self.newest_cat:
                self.newest_cat.next = cat
            self.newest_cat = cat

    def dequeueDog(self):
        if self.oldest_dog:
            name = self.oldest_dog.name
            self.oldest_dog = self.oldest_dog.next
            return name
        return None
        
    def dequeueCat(self):
        if self.oldest_cat:
            name = self.oldest_cat.name
            self.oldest_cat = self.oldest_cat.next
            return name
        return None

    def dequeueAny(self):
        if self.oldest_dog and self.oldest_cat:
            return self.dequeueDog() if self.oldest_dog.order < self.oldest_cat.order else self.dequeueCat()
        if self.oldest_dog:
            return self.dequeueDog()
        if self.oldest_cat:
            return self.dequeueCat()
        return None



shelter = AnimalQueue1()
shelter.enqueue("dog", "dog1")
shelter.enqueue("cat", "cat1")
shelter.enqueue("dog", "dog2")
shelter.enqueue("cat", "cat2")
shelter.enqueue("dog", "dog3")
shelter.enqueue("cat", "cat3")
shelter.enqueue("cat", "cat4")

print(shelter.dequeueAny())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
