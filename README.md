# Final Project EE551_Engineering Programming_Python
- Names: Shehpar Sohail & Michael Hodgetts

## For Pencil-Sketching/Cartoonifying:
1. With Pip set up, use the command line for installing the following packages:
```
- pip install numpy
- pip install matplotlib
- pip install opencv-python
```
2. Run Pencil-Sketching.py:

In command prompt, navigate to the directory where the script �PencilSketching.py� is saved.
To run the application to convert normal photos into pencil sketches, run:
```
- python PencilSketching.py
```

The application is written to run the function that generates the pencil-sketch. Four photos of various styles were examined: landscape, portrait, urban, and close-up landscape. Once the algorithm to produce the pencil-sketch is run, each photo is examined one at a time. The original image is first displayed for five seconds and then the corresponding transformed image is shown for five seconds. Thus, a total of eight pictures are displayed.

3. Run Cartoon.py:

Similar to Pencil-Sketching, in command prompt, navigate to the directory where the script �Cartoon.py� is saved.
To run the application to convert normal photos into cartoon versions, run:
```
- python Cartoon.py
```

The application is written to run the function that generates the cartoon version of an image. Four photos of various styles were examined: landscape, portrait, urban, and close-up landscape. Once the algorithm to produce the cartoon is run, each photo is examined one at a time. The original image is first displayed for five seconds and then the corresponding transformed image is shown for five seconds. Thus, a total of eight pictures are displayed.

## For Generating Photo Mosaics:
1. Like Pencil-Sketching and Cartoonifying images, certain Python packages are required before running the application. For this application to run successfully the required packages are Pillow, glob, math, and string. As glob, math, and string modules come with the installation of Python, use the command line for installing Pillow:
```
- pip install pillow
```

2. Run MosaicCollage.py:

In command prompt, navigate to the directory where the script �MosaicCollage.py� is saved.
To run the application to convert normal photos into photo mosaics, run:
```
- python MosaicCollage.py
```

3. Test Cases:

This application generates three photo mosaics of the same skyline master image located in the same directory as the script �MosaicCollage.py�.

The �skyline_mosaic_ 50_[28,21]_tiles.gif� maps 50 tiles of width 28 pixels, height 21 pixels to the master picture. These 50 tiles are located in the directory �gifs50tiles2821�. Similarly, 
the �skyline_mosaic_300_[28,21]_tiles.gif� maps 300 tiles of width 28 pixels, height 21 pixels to the master picture. These 300 tiles are located in the directory �gifs300tiles2821�. Likewise, the �skyline_mosaic_300_[5,5]_tiles.gif� maps 300 tiles of width 5 pixels, height 5 pixels to the master picture. These 300 tiles are located in the directory �gifs300tiles55�. To size the all tiles to their respective width and heights, the function resize_images(tile_location) was used.

4. Conclusion:

Larger quantity of tiles to select from and smaller tile dimensions resulted in better resolution. Examples of all three photo mosaics generated by the application are also provided in the directory �ExampleMosaicOutputs�.


## Video Link:
```
- https://youtu.be/wYukl8D9SaE
```

