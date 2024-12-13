
playlist = []
song=input("Please enter a song: " )
addAnother = input("Do you want to add another song?: ")

def add_song( song ):
 
 playlist.append(song)
 if(addAnother):
  playlist.append(addAnother)
  output = f" Here is your playlist {playlist}"
  return print(output)
 
 else:
    return print (playlist)




add_song(song)