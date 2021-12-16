#Code for generating Mosaic Collage

#PIL contains image processing features
from PIL import Image
import glob
from math import *
import string

#function for adding two colors together
def addTwoColors(c1,c2):
    new_col = [c1[0] + c2[0],c1[1] + c2[1],c1[2] + c2[2]]
    return new_col    

#function for finding average color of each tile
def avgTileColor(img,width,height):
    total = [0,0,0]
    rgbimage = img.convert('RGB')
    for x in range(width):
        for y in range(height):
            rgb = rgbimage.getpixel((x,y))
            total = addTwoColors(total,rgb)
    total[0] = total[0]/(width*height)
    total[1] = total[1]/(width*height)
    total[2] = total[2]/(width*height)
    return total

#function for finding average color of each tile in master image
def avgMasterColor(img,w,h,width,height):
    total = [0,0,0]
    rgbimage = img.convert('RGB')
    for x in range(width):
        for y in range(height):
            rgb = rgbimage.getpixel((w+x,h+y))
            total = addTwoColors(total,rgb)
    total[0] = total[0]/(width*height)
    total[1] = total[1]/(width*height)
    total[2] = total[2]/(width*height)
    return total

#function to calculate sum of absolute difference between the red, green and blue numbers and return true if color1 closer match and false otherwise
#the smaller difference is the color that is closer to master color
def color_compare(master_color,color1,color2):
    master_r,master_g,master_b = master_color
    color1_r,color1_g,color1_b = color1
    color2_r,color2_g,color2_b = color2
    color1_diff = sqrt(abs(master_r - color1_r)**2 + abs(master_g - color1_g)**2 + abs(master_b - color1_b)**2)
    color2_diff = sqrt(abs(master_r - color2_r)**2 + abs(master_g - color2_g)**2 + abs(master_b - color2_b)**2)

    if color1_diff < color2_diff:
        return True
    else:
        return False

#function to select the tile that best fits with the region of the master image
def tile_selection(master_tile_color,tile_list,color_list):
    if len(tile_list) == 1:
        return [tile_list[0],color_list[0]]
    else:
        [temp_tile, temp_tile_color] = [tile_list[0],color_list[0]]
        [remain_tile,remain_tile_color] = tile_selection(master_tile_color,tile_list[1:],color_list[1:])
        if color_compare(master_tile_color,temp_tile_color,remain_tile_color):
            return [temp_tile, temp_tile_color]
        else:
            return [remain_tile,remain_tile_color]
        
#function to resize images in a directory to same size
def resize_images(tile_location):
    tile_path = tile_location
    tile_name = glob.glob(tile_path + "/*.jpeg") + glob.glob(tile_path + "/*.jpg") + glob.glob(tile_path + "/*.png")
    count = 0

    for tiles in tile_name:
        count = count + 1
        img = Image.open(tiles)
        resized_image = img.resize([5,5])
        resized_image.save(tile_location + "/gifs/resized"+ str(count)+".gif")

#function that creates the photo mosaic        
def create_mosaic(master_image,tile_location,output_file_name):
    #load master image & store size
    img = Image.open(master_image)
    #img.show()
    img_width = img.width
    img_height = img.height
    print "Loaded master image width: " + str(img_width) + " pixels"
    print "Loaded master image height: " + str(img_height) + " pixels"

    #load tiles & store size
    tile_path = tile_location
    tile_name = glob.glob(tile_path + "/*.gif")
    tile_list = []

    for one_tile in tile_name:
        img2 = Image.open(one_tile)
        tile_list.append(img2)

    tile_width = tile_list[0].width
    tile_height = tile_list[0].height
    print "Number of tiles loaded: " + str(len(tile_list)) + " tiles"
    print "Tile image width: " + str(tile_width) + " pixels"
    print "Tile image height: " + str(tile_height) + " pixels"

    color_list =[]            
    for tile in tile_list:
        color_list.append(avgTileColor(tile,tile_width,tile_height))

    #Iterating through the tiles of master image
    horizontal_tiles = img_width/tile_width
    vertical_tiles = img_height/tile_height
    print "Number of tiles master image split horizontally: " + str(horizontal_tiles)
    print "Number of tiles master image split vertically: " + str(vertical_tiles)

    master_colors = []

    #Create output image
    output = Image.new('RGB',img.size)

    for i in range(horizontal_tiles):
        for j in range(vertical_tiles):
            master_tile_color = avgMasterColor(img,tile_width*i,tile_height*j,tile_width,tile_height)
            master_colors.append(master_tile_color)
            [best_fit_tile,best_fit_color] = tile_selection(master_tile_color,tile_list,color_list)
            output.paste(best_fit_tile,(i*tile_width,j*tile_height))
        
    output.save(output_file_name + ".gif")
    output_image = Image.open(output_file_name + ".gif")
    output_image.show()
    
        
#Parameters: master image name, path for tiles, desired output file name
img = Image.open("skyline.gif")
img.show()

#Run for three different scenarios
create_mosaic("skyline.gif","MosaicTiles/gifs50tiles2821","skyline_mosaic_50_[28,21]_tiles")
create_mosaic("skyline.gif","MosaicTiles/gifs300tiles2821","skyline_mosaic_300_[28,21]_tiles")
create_mosaic("skyline.gif","MosaicTiles/gifs300tiles55","skyline_mosaic_300_[5,5]_tiles")

