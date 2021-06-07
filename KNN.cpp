// K-Nearest Neighbors Algorithm
// Created By: Michael Eiger

// Import the necessary libraries
#include <iostream>
#include <cmath>

// Create a function that will calculate Euclidean Distance between any two pairs of (x,y) points
double euclidean(double x1, double y1, double x2, double y2){
    double distance;
    distance = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
    return floor(distance);
}

int main(){
  
    // Create variables to store the user's input
      // n = Number of pre-classified points
      // k = Number of nearest neighbors we will be using for our algorithm
      // redcount = Number of (x,y) points that have the label "Red" 
      // bluecount = Number of (x,y) points that have the label "Blue"
      // The other variables will be used to iterate through arrays storing the (x,y) coordinates or labels
    int n, k, ncheck = 0, redcount = 0, bluecount = 0, count = 0, labcount = 0, temp = 0,;
    
    // Obtain the number of pre-classified points (n) and number of nearest neighbors (k)
    std::cin >> n >> k;
 
    // Create arrays that will store the (x,y) coordinates or labels, respectively
    double points[n*2] = {0};
    char labels[n] = {'\0'};
  
    // Create variables that will store the x-and-y coordinate of the point we are trying to classify
    double unknownx, unknowny;
    
    // Store the points and their respective labels
    while (std::cin >> points[count]){
        count++;
        if ((count >= 2) && ((count % 2) == 0)){
            std::cin >> labels[labcount];
            labcount++;
            ncheck++;
        }
        
        // Once we have run out of points to store, break the loop
        if (ncheck == n){
            break;
        }
    }

    // Store the point we're trying to classify
    std::cin >> unknownx >> unknowny;

    // Iteratively calculating euclidean distance between the unknown point and each of the known points to 
    // determine the nearest neighbor
    for (int i = 1; i <= k; i++){
        double euc = 1000;
        for (int j = 0; j < n*2; j+=2){
            if (euclidean(unknownx, unknowny, points[j], points[j+1]) <= euc){
                euc = euclidean(unknownx, unknowny, points[j], points[j+1]);
                temp = j/2;
            }
        }
      
        // Ensure that we do not count any given neighbor multiple times 
        points[temp*2] = 1000;
        points[(temp*2)+1] = 1000;
      
        // If the closest neighbor is labeled "Red" or "Blue", add it to the red or blue tally, respectively
        if (labels[temp] == 'R'){
            redcount++;
        } else if (labels[temp] == 'B'){
            bluecount++;
        }
    }

    // If a majority of the k-nearest neighbors have a "Red" label, classify the unknown point as "Red." Else, 
    // if a majority of the k-nearest neighbors have a "Blue" label, classify the unknown point as "Blue"
    if (redcount > bluecount){
        std::cout << 'R' << std::endl;
    } else {
        std::cout << 'B' << std::endl;
    }

    return 0;
}
