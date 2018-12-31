Incremental Reading Slides
==========================

To run this program, I typically do
```
python inc-read_slides.py <path-to-pdf> <num> | xclip -sel clipboard
```

The program converts the pdf pages into pngs via some program, moves them into the media.collection folder for Anki, and then prints out the text to put into an Anki note.

I've used this for some time now and it works fine.
You just sometimes have to play with the `<num>` parameter in order to get the pngs to look okay.

### Not Authorized Error

This error stems from ImageMagick's security policy, which is controlled in its `policy.xml` file.
On Linux, this can be found under `/etc/ImageMagick-6/policy.xml` or similar area.
To enable converting from PDFs, change the rights for PDF to "read".
For example, in the file near the bottom,
```xml
<policy domain="coder" rights="read" pattern="PDF" />
```

### Nix Support

If you know what Nix is and how to use it, first run `nix-shell`.
Then, run the above command.

This approach has the benefit of not needing to manually download ImageMagick or find the right version of Python.
Also, you don't have to change the policy file (as far as I know).
