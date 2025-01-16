#open file

story = open("beatrix.txt", "r")


#set up the replacements

replacements = [
    (" The ", " Car "),
    (" the ", " car "),
    (" and ", " dinosaur "),
    (" He ", " Camera "),
    (" he ", " camera "),
    (" to ", " flower "),
]

# read the story

new_story = story.read()


#for loop that replaces the first item in tuple with second

for old, new in replacements:
    new_story = new_story.replace(old, new)

print(new_story)
