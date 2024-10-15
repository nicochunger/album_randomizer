# Album Randomizer

This project is an album selection program that randomly selects music albums from a list you define. The idea is that I had periods where I didn't know what to listen to. So I figured I would listen to all my favorite albums but didn't know how to choose which one to listen to.

Thats when I thought about writing this simple script where I divide the process in two steps:

1. List out all the albums you like or want to listen to. It's easier to this when you do it all at once just going artist by artist listing all albums.
2. Run this script which randomly selects one of the albums from the list. Every time you run the script a new album is selected (without repetition).

So it adds an element of surprise by not knowing which album you're going to get :).

## Usage

1. Clone the repository or download the `album_randomizer.py` file to your local machine.
2. Open a terminal and navigate to the directory containing `album_randomizer.py`.
3. Create a `albums.txt` file with all the albums you want, one per line. In this repository, you can find my personal list 😉.
3. Run the script with the desired options:
    - `--last`: Show the last selected album.
    - `--all`: Show all the shown albums so far.
    - `--reset`: Reset the shown albums list.

### Examples

- To run the script normally just run:
    ```sh
    python album_randomizer.py
    ```
- To show the last selected album:
    ```sh
    python album_randomizer.py --last
    ```

- To show all the shown albums so far:
    ```sh
    python album_randomizer.py --all
    ```

- To reset the shown albums list:
    ```sh
    python album_randomizer.py --reset
    ```
