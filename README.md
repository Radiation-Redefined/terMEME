# terMEME
## A meme scrapper which displays memes inside your linux terminal.

terMEME is a terminal based meme viewer written in Python 3 which allows Linux users to view memes from meme subreddits inside the comfort of their terminals.

**NOTE:**  It can actually fetch you random images from any valid subreddit of your choice. But I just stuck with memes. 

## Dependencies 

- `w3m-img`
    - For image rendering inside the terminal.
- `imagemagick`
    - If your terminal has trouble rendering the images, it will have the option to display the image externally.

## Python Dependencies 

All the dependencies for the project are listed in the requirements.txt.

## Installation 
```
git clone https://github.com/OBITORASU/terMEME.git
cd terMEME
pip3 install -r requirements.txt

sudo apt-get install w3m-img
sudo apt-get install imagemagick
```
With the above done, you are ready to go. Fire up the script by running
```
python3 view.py
```
## Navigation
Use your q key to quit the w3m preview inside your terminal. On the prompt pressing e will terminate the program and any other key will bombard you with more memes. If your terminal is incapable of displaying the images in it, it will switch you to an external view on imagemagick. In the second case pressing q twice will get you back to the prompt.
