cache = {}


def player(prev_play, opponent_history=[]):
    global cache # this is a global variable, so we can use it in the function

    n = 5 # number of previous plays to consider

    if prev_play in ["R", "P", "S"]: # if the opponent played
        opponent_history.append(prev_play) # add their move to the history

    guess = "R"  # default, until statistic kicks in

    if len(opponent_history) > n: # if we have enough history to make a prediction
        inp = "".join(opponent_history[-n:]) # get the last n moves

        if "".join(opponent_history[-(n+1):]) in cache.keys(): # if we have seen this sequence before
            cache["".join(opponent_history[-(n+1):])] += 1 # increment the count
        else: # if we haven't seen this sequence before
            cache["".join(opponent_history[-(n+1):])] = 1 # add it to the cache

        possible = [inp+"R", inp+"P", inp+"S"] # possible next moves

        for i in possible: 
            if not i in cache.keys(): 
                cache[i] = 0 # add possible moves to the cache if they aren't there

        predict = max(possible, key=lambda key: cache[key]) # predict the most likely next move

        if predict[-1] == "P": # if the most likely next move is paper
            guess = "S"
        if predict[-1] == "R": # if the most likely next move is rock
            guess = "P"
        if predict[-1] == "S": # if the most likely next move is scissors
            guess = "R"

    return guess
