Incremental Reading Slides
==========================

To run this program, I typically do
```
python inc-read_slides.py <path-to-pdf> <num> | xclip -sel clipboard
```

The program converts the pdf pages into pngs via some program, moves them into the media.collection folder for Anki, and then prints out the text to put into an Anki note.

I've used this for some time now and it works fine.
You just sometimes have to play with the `<num>` parameter in order to get the pngs to look okay.
