playlist=[]

print("Welcome to Super Playlist!")
print("You can:")
print("\t'Add' a song")
print("\t'Delete' a song")
print("\t'Edit' a song")
print("\t'Show' all songs")

while True:
    command=input("Enter a command: ")

    if command=="Show":
        print(playlist)
        
    if command=="Add":
        song=input("Enter a song name: ")
        if song not in playlist:
            playlist.append(song)
        else:
            print("Error!")

    if command=="Delete":
        song=input("Enter a song name: ")
        if song in playlist:
            playlist.remove(song)
        else:
            print("Error!")

    if command=="Edit":
        song=input("Enter a song name: ")
        if song in playlist:
            new = input("Enter a new name for song: ")
            ind = playlist.index(song)
            playlist[ind]=new
        else:
            print("Error!")

    if command=="Exit":
        print("Bye!")
        break




    
