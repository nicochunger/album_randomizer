import argparse
import random


def main(show_last, show_all, reset, show_remaining):
    if reset:
        confirm = input(
            "Are you sure you want to reset the shown albums list? Type 'Y' to confirm: "
        )
        if confirm == "Y":
            open("shown_albums.txt", "w").close()
            print("The shown albums list has been reset.")
        else:
            print("Reset operation cancelled.")
        return

    # Open the files (creates 'shown_albums.txt' if it doesn't exist)
    with (
        open("albums.txt", "r") as album_file,
        open("shown_albums.txt", "a+") as shown_album_file,
    ):
        # Read all albums
        albums = [line.strip() for line in album_file]

        # Go to the beginning of the shown_albums file and read shown albums
        shown_album_file.seek(0)
        shown_albums = [line.strip() for line in shown_album_file]

        if show_remaining:
            not_shown_albums = list(set(albums) - set(shown_albums))
            if not_shown_albums:
                print(f"There are {len(not_shown_albums)} albums left to listen to:")
                for i, item in enumerate(sorted(not_shown_albums)):
                    print(f"Nr. {i + 1}: {item}")
            else:
                print("All albums have been listened to!")
            return

        if show_last:
            if shown_albums:
                last_shown_album = shown_albums[-1]
                artist, album = last_shown_album.split(" - ")
                print(
                    f"The last shown album was Nr. {len(shown_albums)}: '{album}' by {artist}"
                )
            else:
                print("No album has been shown yet.")
            return

        if show_all:
            if shown_albums:
                print("These are all the shown albums so far:")
                for i, item in enumerate(shown_albums):
                    artist, album = item.split(" - ")
                    print(f"Nr. {i + 1}: '{album}' by {artist}")
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
        shown_album_file.write(new_album + "\n")

        # Display the selected album
        artist, album = new_album.split(" - ")
        print(
            f"The new randomly selected album is Nr. {len(shown_albums) + 1}: '{album}' by {artist}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Album selection program.")
    parser.add_argument(
        "--last", action="store_true", help="Show the last selected album"
    )
    parser.add_argument(
        "--all", action="store_true", help="Show all the shown albums so far"
    )
    parser.add_argument(
        "--reset", action="store_true", help="Reset the shown albums list"
    )
    parser.add_argument("--sort", action="store_true", help="Sort the albums list")
    parser.add_argument(
        "--remaining",
        action="store_true",
        help="Show albums that haven't been listened to yet",
    )
    args = parser.parse_args()

    if args.sort:
        with open("albums.txt", "r") as album_file:
            albums = [line.strip() for line in album_file]
            # Track duplicates before removing them
            original_albums = albums.copy()
            # Remove duplicates
            albums = list(set(albums))
            # Find duplicates
            duplicates = [
                item for item in original_albums if original_albums.count(item) > 1
            ]
            # Sort the albums
            albums.sort()
        with open("albums.txt", "w") as album_file:
            for album in albums:
                if album == albums[-1]:
                    album_file.write(album)
                else:
                    album_file.write(album + "\n")
        print("The albums list has been sorted.")
        if duplicates:
            print("The following duplicates were removed:")
            for duplicate in sorted(set(duplicates)):
                print(f"- {duplicate}")
    else:
        main(args.last, args.all, args.reset, args.remaining)
