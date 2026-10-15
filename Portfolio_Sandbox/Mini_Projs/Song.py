# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:00:16 2026

@author: aiaqu
"""

last_song = True

    
    
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs_played = []
        current_song = self
        
        while current_song is not None:
            # 1. Check if we've already visited this song
            if current_song in songs_played:
                return True
            
            # 2. Track that we've seen this song
            songs_played.append(current_song)
            
            # 3. Move to the next song in the chain
            current_song = current_song.next

        # If current_song becomes None, we hit the end of the playlist
        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_in_repeating_playlist())