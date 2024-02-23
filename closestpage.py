import sys
from helpers import get_closest_link, spinner, DEBUG_MODE

def solve_wiki_game(current_page, end_page, depth, path_taken): # recursive function for solving the game, it is what is called to get the search started
    sys.stdout.write('\b')
    sys.stdout.write(next(spinner))
    sys.stdout.flush()  # code to add a spinner to the console so the user can tell its working
    if depth < 0:   # base case for if over the set depth amount of paths has been traversed, meaning a solution was not found
        print("DEPTH REACHED 0")
        return
    if current_page.lower() == end_page.lower():    # base case for if the current page is our goal page
        return
    closest_link = get_closest_link(current_page, end_page, path_taken) # finds the next best page using the above function
    path_taken.append(closest_link[0])  # updates the path taken with the new best page
    if DEBUG_MODE: print("current path:",path_taken)
    depth -= 1  # counts down the depth so program doesnt run forever
    if closest_link[0].lower() == end_page.lower(): # case for if the closest link is our solution to the game
        return
    else:
        return solve_wiki_game(closest_link[0], end_page, depth, path_taken)    # recursive call to check the next level for a result