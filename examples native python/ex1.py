name = input ("What's your name? ")
print ("hello " + name)
p = 12

# revive function
def revivePlayer(p):
    if p>0:
        print ("Player has health, they do not need to be revived")
    else:
        print ("Player has been revived")
        p = 100

revivePlayer(p)
p = 0
revivePlayer(p)
# added stuff
print ('hello!!!!!!!!!')