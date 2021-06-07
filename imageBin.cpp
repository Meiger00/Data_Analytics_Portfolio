// Image Binarization Tool
// Created By: Michael Eiger

// TO TEST THIS PROGRAM LOCALLY AFTER COMPILATION, RUN THE FOLLOWING COMMAND:
// ./imageBin (name of the .bmp image to binarize) (name to be given to the output .bmp image)

// NOTE: This program has a notable dependency: the "bitmap_image" library, created by Arash Partow.
// The bitmap_image library is downloadable from the following link: https://www.partow.net/programming/bitmap/index.html

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include "bitmap_image.hpp"

int main(int argc, char *argv[]) {
    
	// Get a string containing the .bmp image name to be binarized
    std::string file_name(argv[1]);
	
	// Get a string containing the name to be given to the .bmp file containing the binarized image
    std::string out_file(argv[2]);

    // Declaring the image as an object of class "bitmap_image"
    bitmap_image image(file_name);

    // Converting the image to grayscale
    image.convert_to_grayscale();

    // Determine number of pixels in image's height and width, respectively (plus other variable declarations)
    int height = image.height(), width = image.width(), glob_mean = 0;
    rgb_t temp;

    // Determining global threshold
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            temp = image.get_pixel(j, i);
            glob_mean += (temp.red + temp.green + temp.blue);
        }
    }
    glob_mean = glob_mean/((height*width)*3);

    // Perform binarization by comparing a pixel's mean density to the global threshold
	// If a pixel's mean density is GREATER THAN the global threshold, set the pixel to White
	// If a pixel's mean density is LESS THAN the global threshold, set the pixel to Black
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            int local_mean = 0;
            temp = image.get_pixel(j, i);
            local_mean += (temp.red + temp.green + temp.blue);
            if ((local_mean/3) < glob_mean){
                image.set_pixel(j, i, 0, 0, 0);
            } else {
                image.set_pixel(j, i, 255, 255, 255);
            }
        }
    }

    // Outputting the binarized image as a .bmp file
    image.save_image(out_file);

    return 0;
}
