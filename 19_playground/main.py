# https://platzi.com/clases/7967-python-21-dias/63842-playground-implementacion-de-un-stack/

from node import Node

class Playlist:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def addSong(self, song):
        """Este método permite agregar una canción a la pila. 
        La canción se agrega en el tope de la pila."""
        new_song = Node(song)
        if self.length == 0:
            self.top = new_song
            self.bottom = new_song
        else:
            new_song.next = self.top
            self.top = new_song
        self.length += 1


    def playSong(self):
        """Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla. Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista"."""
        if self.length == 0:
            raise Exception("No hay canciones en la lista")
        else:
            popped_song = self.top
            if popped_song == self.bottom:
                self.bottom = None
            self.top = self.top.next
        self.length -= 1
        return popped_song.value

    def getPlaylist(self):
        """Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de reproducción, desde la última agregada hasta la primera."""
        lista_songs = []
        current = self.top
        while current:
            lista_songs.append(current.value)
            current = current.next
        return lista_songs


if __name__ == '__main__':
    playlist = Playlist()

    playlist.addSong("Bohemian Rhapsody")
    playlist.addSong("Stairway to Heaven")
    playlist.addSong("Hotel California")
    print(playlist.playSong())
    print(playlist.playSong())
    print(playlist.playSong())
    print(playlist.playSong())


    # print(playlist.getPlaylist()) 