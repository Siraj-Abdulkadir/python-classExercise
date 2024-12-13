
playlist = []
song=input("Please enter a song: " )
addAnother = input(f"Do you want to add another song ? (Enter no if not): ")


def add_song( song ):
 playlist.append(song)
 if(addAnother == "no"):
  return print(f"Here is your playlist: {playlist}")
 else:
  playlist.append(addAnother)
  return print(f"Here is your playlist: {playlist}")

add_song(song)