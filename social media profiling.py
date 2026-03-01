class User():
    def __init__ (self, lastName, firstName, likesCount, friendsName):
        self.lastName = lastName
        self.firstName = firstName
        self.likesCount = likesCount
        self.friendsNames = friendsNames
        
    def introduceSelf(self):
        print("-----INTRODUCTION-----")
        print("Hi, I am", self.lastName + " " + self.firstName)
        
    def fullProfile(self):
        print("-----fullProfile Information-----")
        print("Name   : ", self.lastName + "," + " " + self.firstName)
        print("Likes  : ", str(self.likesCount))
        for i in self.friendsNames:
            print("Friends: " + "-", i)

friendsNames = []    
lastName = input("Enter lastname: ")
firstName = input("Enter firstname: ")
likesCount = input("Enter how many likes you have: ")
while True:
    friendsName = input("Enter your friends name (press Enter if done): ")
    if friendsName == "":
        break
    friendsNames.append(friendsName)
    
user1 = User(lastName, firstName, likesCount, friendsName)
user1.introduceSelf()
user1.fullProfile()
