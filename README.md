# ImageFolderToPDF
ImageFolderToPDF is a python script used to convert a folder of images into a pdf format. The script is non-recursive and only converts image files that are direct children of the targeted folder. Each image is added as a single page to the pdf file.

## Dependencies
- [img2pdf](https://github.com/josch/img2pdf)

## Usage
The absolute path to the folder is required as input.
```py imgfoldertopdf <absolute path>```

The script only converts 1000 images per pdf file and automatically names it as
```<directory name><file number>.pdf```.

The first 1000 images will be added to ```directory1.pdf```. The second 1000 images will be added to ```directory2.pdf``` and so on.

The threshold of 1000 can be modified through the ```threshold``` variable in the script.

By default, only ```[".jpg" , ".jpeg" , ".jpe" , ".jif" , ".jfif", ".png"]``` images with these extensions are converted. Extensions can be added/removed by modifying the ```include_ext``` list in the script.