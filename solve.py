# Longest path on a directed graph problem
# Problem shared by Matt T. 6/5/2019
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    # puzzle, puzzle_coords = puzzle_generator(6,4)
    # print(puzzle)
    # moves = legal_moves(puzzle, puzzle_coords, [3,3],[3,3])
    # map = binarize_moves(puzzle_coords, moves)
    # print(map)
    # quit()

    # Generate puzzles and try them a bunch of times. Save the longest solutions.
    puzzle_runs = 1
    max_length_solutions_by_puzzle = []
    all_solution_lengths = np.zeros(36)
    f = open("puzzle_log.txt","a")
    for a in range(1000):
        # Make a new puzzle
        puzzle, puzzle_coords = puzzle_generator(6,4)
        longest_puzzle = []
        longest_puzzle_solution = []
        for i in range(1000):
            print("Working on puzzle number " + str(puzzle_runs) + ", iteration " + str(i) + ".\n")
            one_path = traverse_puzzle_randomly(puzzle, puzzle_coords)
            all_solution_lengths[len(one_path)-1] += 1
            if len(one_path) > len(longest_puzzle_solution):
                longest_puzzle_solution = one_path
                longest_puzzle = puzzle
                f.write("New longest puzzle discovered! Length is " + str(len(longest_puzzle_solution)) + ".\n")
                f.write("Puzzle number " + str(puzzle_runs) + ", iteration " + str(i) + ".\n")
                f.write(str(longest_puzzle) + "\n")
                f.write("Solution:\n")
                f.write(str(longest_puzzle_solution) + "\n")
                f.flush()
                print(puzzle_runs)
                print("New longest puzzle discovered! Check puzzle_log.txt to see it!")
            if len(longest_puzzle_solution) == 36:
                break
                #pass
        max_length_solutions_by_puzzle.append(len(longest_puzzle_solution))
        f.write("Puzzle exhausted. Max length solution for each puzzle so far:\n")
        f.write(str(max_length_solutions_by_puzzle) + "\n")
        puzzle_runs += 1

    plt.plot(all_solution_lengths)
    plt.title("Distribution of random puzzle solution lengths")
    plt.show()

    plt.close()
    plt.plot(max_length_solutions_by_puzzle)
    plt.title("Maximum length solution found for each puzzle")
    plt.show()

def legal_moves_2(puzzle, puzzle_coords, position, visited_coords):
    """return all available moves from the given position"""
    # give position in row, column format
    legal_list = []
    # Get the current value you are sitting on
    my_spot = puzzle[position[0]][position[1]]
    for coord in puzzle_coords:
        if abs(coord[0] - position[0]) <= my_spot and abs(coord[1] - position[1]) <= my_spot and coord not in visited_coords:
            legal_list.append(coord)
    return legal_list

def legal_moves(puzzle, puzzle_coords, position, visited_coords):
    """return all available moves from the given position"""
    # give position in row, column format
    legal_list = []
    # Get the current value you are sitting on
    my_spot = puzzle[position[0]][position[1]]
    for coord in puzzle_coords:
        dist = [abs(coord[0] - position[0]),abs(coord[1] - position[1])]
        dist.sort()
        if dist[1] == my_spot and dist[0] <= my_spot and coord not in visited_coords:
            legal_list.append(coord)
    return legal_list

def traverse_puzzle_randomly(puzzle, puzzle_coords):
    visited_coords = []
    # Select a random starting location
    start_coord = [np.random.randint(1,len(puzzle)),np.random.randint(1,len(puzzle))]
    visited_coords.append(start_coord)
    first_legal_moves = legal_moves(puzzle, puzzle_coords, visited_coords[-1], visited_coords)
    num_legal_moves = len(first_legal_moves)
    while num_legal_moves > 0:
        all_legal_moves = legal_moves(puzzle, puzzle_coords, visited_coords[-1], visited_coords)
        num_legal_moves = len(all_legal_moves)
        if num_legal_moves > 0:
            visited_coords.append(all_legal_moves[np.random.randint(0,num_legal_moves)])
    return visited_coords

def traverse_in_order(puzzle, puzzle_coords):
    visited_coords = []
    start_coord = [0,0]
    visited_coords.append(start_coord)

def puzzle_generator(width,num_max):
    """randomly initialize a puzzle"""
    puzzle = []
    puzzle_coords = []
    for i in range(width):
        column = []
        for j in range(width):
            column.append(random.randint(1,num_max))
            puzzle_coords.append([i,j])
        puzzle.append(column)
    return np.asarray(puzzle), puzzle_coords

def binarize_moves(puzzle_coords,legal_list):
    binarized = np.zeros((6,6))
    for coord in puzzle_coords:
        if coord in legal_list:
            binarized[coord[0]][coord[1]] = 1
    return np.asarray(binarized).astype(np.int)

if __name__=="__main__":
    main()
