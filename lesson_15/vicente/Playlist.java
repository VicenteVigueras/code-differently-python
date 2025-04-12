package com.codedifferently.lesson16.vicente;

import java.util.Collections;
import java.util.List;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Playlist {
    
    private List<Song> songs;
    private String playlistName;
    private String creator;
    

    public Playlist(String playlistName, List<Song> songs, String creator) {
        this.playlistName = playlistName;
        this.songs = songs;
        this.creator = creator;       
    }

    public Playlist() {
    }


    public List<Song> shuffle(List<Song> playlist) {
    Collections.shuffle(playlist);
    return playlist;
    }

    public void addSong(List<Song> playlist, Song song) {
        playlist.add(song);
    }

    public void removeSong(List<Song> playlist, Song song) {
        if(!playlist.contains(song)) {
            System.out.println("Song Not Found in the List");
        } else {
            playlist.add(song);
        }
       
    
    }

    public void filterByGenre() {

    }

    public void displayPlaylist(List<Song> playlist) {
      for(Song song: playlist) {
        System.out.println(song);
      }
    }


    public static void main(String[] args) {

    }

}
