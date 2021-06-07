// Conway's Game of Life
// Created by: Michael Eiger

#include <iostream>

int main(){
    int rows, cols, gens, count = 0;
    int living = 0, not_living = 0;

    // Rows >= 3
    // Cols <= 20
    // 0 <= Gens <= 50
    std::cin >> rows >> cols >> gens;

    char alive = '*', dead = '.', board[rows][cols] = {0}, temp, initial[500] = {0};
    int board_state[rows*cols*2] = {0};

    // Initialize the boards
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            board[i][j] = '0';
        }
    }

    // Obtain and store the initial board state
    while (std::cin >> temp){
        initial[count] = temp;
        count++;

        if (count == (rows*cols)){
            break;
        }
    }

    // Initialize the boards again
    count = 0;
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            board[i][j] = initial[count];
            count++;
        }
    }

    // If generations = 0
    if (gens == 0){
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if (j != (cols - 1)){
                    std::cout << board[i][j] << ' ';
                } else {
                    std::cout << board[i][j];
                }
            }
            std::cout << std::endl;
        }
        return 0;
    }

    while (gens > 0){

        // Count living/dead cells BEFORE UPDATING THE BOARD
        count = 0;
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                living = 0;
                not_living = 0;
                if (((i - 1) >= 0) && ((j - 1) >= 0)){ // Upper left of a given cell
                    if (board[i-1][j-1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if ((i - 1) >= 0){ // Directly above a given cell
                    if (board[i-1][j] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if (((i - 1) >= 0) && ((j + 1) < cols)){ // Upper right of a given cell
                    if (board[i-1][j+1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if ((j + 1) < cols){ // Directly right of a given cell
                    if (board[i][j+1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if ((j - 1) >= 0){ // Directly left of a given cell
                    if (board[i][j-1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if (((i + 1) < rows) && ((j - 1) >= 0)){ // Lower left of a given cell
                    if (board[i+1][j-1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if ((i + 1) < rows){ // Directly below a given cell
                    if (board[i+1][j] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }
                if (((i + 1) < rows) && ((j + 1) < cols)){ // Lower right of a given cell
                    if (board[i+1][j+1] == alive){
                        living++;
                    } else {
                        not_living++;
                    }
                }

            board_state[count] = living;
            count++;
            board_state[count] = not_living;
            count++;
            }
        }

        // Update the board
        count = 0;
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if ((board[i][j] == alive) && ((board_state[count] < 2) || (board_state[count] > 3))){
                    board[i][j] = dead;
                } else if ((board[i][j] == dead) && ((board_state[count] == 3))){
                    board[i][j] = alive;
                } else {
                    board[i][j] = board[i][j];
                }
                count+=2;
            }
        }
        gens--;
    }

    // Print the final board!
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            if (j != (cols - 1)){
                std::cout << board[i][j] << ' ';
            } else {
                std::cout << board[i][j];
            }
        }
        std::cout << std::endl;
    }

    return 0;
}
