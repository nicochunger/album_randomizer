import argparse
import random
# import os

def main(show_last, show_all, reset):
    if reset:
        confirm = input("Are you sure you want to reset the shown albums list? Type 'Y' to confirm: ")
        if confirm == 'Y':
            open('shown_albums.txt', 'w').close()
            print("The shown albums list has been reset.")
        else:
            print("Reset operation cancelled.")
        return

    # Open the files (creates 'shown_albums.txt' if it doesn't exist)
    with open('albums.txt', 'r') as album_file, open('shown_albums.txt', 'a+') as shown_album_file:
        # Read all albums
        albums = [line.strip() for line in album_file]

        # Go to the beginning of the shown_albums file and read shown albums
        shown_album_file.seek(0)
        shown_albums = [line.strip() for line in shown_album_file]

        if show_last:
            if shown_albums:
                last_shown_album = shown_albums[-1]
                artist, album = last_shown_album.split(' - ')
                print(
                    f"The last shown album was Nr. {len(shown_albums)}: '{album}' by {artist}")
            else:
                print("No album has been shown yet.")
            return

        if show_all:
            if shown_albums:
                print("These are all the shown albums so far:")
                for i, item in enumerate(shown_albums):
                    artist, album = item.split(' - ')
                    print(f"Nr. {i+1}: '{album}' by {artist}")
            else:
                print("No album has been shown yet.")
            return

        # Find the albums that haven't been shown yet
        not_shown_albums = list(set(albums) - set(shown_albums))

        if not not_shown_albums:  # if all albums have been shown
            print("All albums have been shown!")
            return

        # Select a random album that hasn't been shown
        new_album = random.choice(not_shown_albums)

        # Write this album to the 'shown_albums.txt' file
        shown_album_file.write(new_album + '\n')

        # Display the selected album
        artist, album = new_album.split(' - ')
        print(
            f"The new randomly selected album is Nr. {len(shown_albums) + 1}: '{album}' by {artist}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Album selection program.')
    parser.add_argument('--last', action='store_true',
                        help='Show the last selected album')
    parser.add_argument('--all', action='store_true',
                        help='Show all the shown albums so far')
    parser.add_argument('--reset', action='store_true',
                        help='Reset the shown albums list')
    parser.add_argument('--sort', action='store_true', help='Sort the albums list')
    args = parser.parse_args()

    if args.sort:
        with open('albums.txt', 'r') as album_file:
            albums = [line.strip() for line in album_file]
            albums.sort()
        with open('albums.txt', 'w') as album_file:
            for album in albums:
                # Write each album to the file
                if album == albums[-1]:
                    # If the album is the last one, don't add a newline
                    album_file.write(album)
                else:
                    album_file.write(album + '\n')
        print("The albums list has been sorted.")
    else:
        main(args.last, args.all, args.reset)
