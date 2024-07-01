import pygame
import os

# Initialize the Pygame mixer
pygame.mixer.init()

def load_music(file_path):

# Load a music file into Pygame mixer. Args: file_path (str): Path to the music file.

    try:
        pygame.mixer.music.load(file_path)
        print(f"Loaded: {os.path.basename(file_path)}")
    except pygame.error as e:
        print(f"Error loading file: {e}")

def play_music():

# Start playing loaded music.

    try:
        pygame.mixer.music.play()
        print("Playing music...")
    except pygame.error as e:
        print(f"Error playing file: {e}")

def pause_music():

#Pause currently playing music.

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Music paused...")
    else:
        print("No music is currently playing")

def unpause_music():

#Resume paused music.

    if pygame.mixer.music.get_busy():
        print("Music is already playing.")
    else:
        pygame.mixer.music.unpause()
        print("Music resumed...")

def stop_music():

#Stop currently playing music.

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Music stopped")
    else:
        print("No music is currently playing")

def main():

#Main function to run the CLI music player.

    print("Simple CLI Music Player")
    print("Commands: load <file_path>, play, pause, unpause, stop, quit")

    while True:
        command = input("Enter command: ").strip().split()

        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "load":
            if len(command) < 2:
                print("Please provide the path to the music file.")
            else:
                file_path = command[1]
                load_music(file_path)
        elif cmd == "play":
            play_music()
        elif cmd == "pause":
            pause_music()
        elif cmd == "unpause":
            unpause_music()
        elif cmd == "stop":
            stop_music()
        elif cmd == "quit":
            print("Exiting music player.")
            break
        else:
            print("Unknown command. Please use load, play, pause, unpause, stop, or quit.")

if __name__ == "__main__":
    main()
