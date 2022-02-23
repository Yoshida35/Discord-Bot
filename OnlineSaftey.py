print("What is your name?")
name = str(input())
print("Hi", name,", I'm Josh, Do you have a best friend? (y / n)")
ynfriend = str(input())

if ynfriend == "y":
        print ("What is their name?")
        friend = str(input())

        if friend == "Connor":
                knowsConner = True

        else:
                knowsConnor = False
                print("You'll find one.")

else:
	print("Please Enter 'y' or 'n'")

print("How old are you?")
age = int(input())
Older = 69 - age
print("I am", Older, "Years older than you")

print("")

print("So what do you like doing?")
likesDoing = input()
print("Same, I also like doing that!")

print("Quick question, What is 9 + 10?")
Ans = int(input())
if Ans == "19":
	print("Ok")
elif Ans == "21":
	print("No, just Stop!")
else:
	print("Are you sure? (y / n)")

Ans2 = input()
if Ans2 == "y":
	print("Ok then...")
elif Ans2 == "n":
	print("Well tough, you had your chance...")
else:
	print("Please Enter 'y' or 'n'")

print("")
print("")
print("So... I don't know, Give me a number!")
num = int(input())
print("")
print("Watch this... I'll multiply that number and my age together and then tell me my name!")
print(num * 69, "Is the number, what is my age?")
guess = int(input())

if guess == 69:
	print("Well done!")
elif guess >= 69:
        print("Well we all know that's not true")
else:
	print("Unlucky, maybe next time.")

print("")

print("What do you like to do the most?")
print("1. Gaming")
print("2. Going Out Places")
print("3. Both")
print("4. Neither")
print("Please Enter either '1', '2', '3', or '4'.")
Likes = int(input())
if Likes == 1:
	LikesGames = name
	print("I like Gaming too!")
elif Likes == 2:
	LikesSocial = name
	print("I like going out places too!")
elif Likes == 3:
	LikesBoth = name
	print("I like Both too!")
elif Likes == 4:
	LikesNeither = name
	print("I don't like them either!")
else:
	print("Please Enter '1', '2', '3', or '4'.")

print("Sorry, I've got to go now, See you next time, Bye!")

print("")
print("")
print("")

print("Here is all I got from the interaction:")
print("name =", name)
print("friend = ", friend)
print("Knows Connor =", knowsConner)
print("age =", age)
print("Likes doing -", likesDoing)
print("Interlectual level")
print("Likes Option", Likes, "out of '1 - Gaming', '2 - Socialising', '3 - Both', and '4 - Neither'")
print("")
print("Don't giveaway your infomation!")
print("")
input()
