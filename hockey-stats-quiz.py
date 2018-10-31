print 'Hockey Vocab Quiz!'
hockey_stats_easy = [['GP', 'Games Played', 'The number of games the player has set foot on the ice in the current season.'],
['G', 'Goals', 'The total number of goals the player has scored in the current season.'],
['A', 'Assists', 'The number of goals the player has assisted on in the current season.'],
['P', 'Points', 'The number of scoring points, calculated as the sum of G and A.']]
hockey_stats_med = [['+/-', 'Plus/Minus', 'The number of team even strength or shorthanded goals for minus the number of team even strength or shorthanded goals against while the player is on the ice'],
['SV%', 'Save Percentage', 'The percentage of the total shots faced the goaltender has saved'],
['PIM', 'Penalties In Minutes', 'The number of penalty minutes the player has been assessed.'],
['GAA', 'Goals Against Average','The mean goals-per-60 minutes scored on the goaltender']]
hockey_stats_hard = [['SAT', 'Corsi', 'The sum of shots on goal, missed shots and blocked shots.'],
['USAT', 'Fenwick', 'A variant of Corsi that counts only shots on goal and missed shots; blocked shots are not included.'],
['SPSV%', 'PDO', "The sum of a team's shooting percentage and its save percentage."],
['ZS', 'Zone Starts', 'The ratio of how many face-offs a player is on for in the offensive zone relative to the defensive zone.']]
easy_options = ["easy", "Easy", "EASY"]
med_options = ["medium", "Medium", "MEDIUM"]
hard_options = ["hard", "Hard", "HARD"]
user_input = raw_input('Select Level Easy, Medium, Hard: ')
def Select_Level(user_input):
    """
        Behavior: This function sets the level by taking user input and defining hockey_stats with one of three lists
        Inputs: Inputs user input asking for a level select
        Outputs: outputs the variable hockey_stats
    """
    if user_input in easy_options:
        hockey_stats = hockey_stats_easy
    else:
        if user_input in med_options:
            hockey_stats = hockey_stats_med
        else:
            if user_input in hard_options:
                hockey_stats = hockey_stats_hard
            else:
                hockey_stats = 'none'
    return hockey_stats

def Beat_Game(level):
    """
        Behavior: This function checks to see the level the game was played on and either congratulates them on beating the
        hardest level or encourages them to try a harder level
        Inputs: One input, the level chosen by user input running through the Select_Level function
        Outputs: Outputs one string of varying congratulations
    """
    if level == hockey_stats_hard:

        return 'Congrats! You beat the game!'
    else:
        return 'Congrats! You beat this level. Try the game on a harder level.'

acronym = 0
vocab = 1
desc = 2
def play_game(hockey_stats):
    """
        Behavior: This function asks the user to fill in the blank of a vocab word based on an acronym and if the user
        entry is correct fills in the blank with the correct vocab and a description of the word. If it is incorrect is asks the user
        to try again. The user is also able to enter in the number of guesses before game over.
        Inputs: One input, a variable that will be used in the function to ask the questions and check the answers
        Outputs: Outputs one string of varying congratulations or announcement of the player losing the game
    """
    while hockey_stats == 'none': #checks that the user entered a valid variation on the level options. If not asks them to select
    #level again and runs that input through the Select_Level function. This will continue until a valid entry is made.
        user_input = raw_input('Invalid Entry. Select Level Easy, Medium, Hard: ')
        hockey_stats = Select_Level(user_input)
    guesses = input('Enter Number of Guesses Before Game Over ')
    print 'Please Note All User Input Must Be Capitalized!'
    index = 0
    while index < len(hockey_stats): #checks the length of the list and stops the game when every item in the list is used
        wrong_answers = 0
        user_input = raw_input(hockey_stats[index][acronym] + ' ' + "denotes the player's ") #prompt for user to fill in the blank
        while user_input != hockey_stats[index][vocab]: #checks whether user input matches answer in the list
            wrong_answers += 1
            if wrong_answers == guesses: #checks to see if user is out of guesses and ends game if they are
                return 'Out of guesses... you lose.'
            user_input = raw_input('Sorry, Try Again: ' + hockey_stats[index][acronym] + " denotes the player's ")
        print 'Correct! ' + hockey_stats[index][acronym] + " denotes the player's " + hockey_stats[index][vocab] + ": " + hockey_stats[index][desc]
        index += 1 #moves the index so that the game moves to the next fill in the blank
    return Beat_Game(hockey_stats)
print play_game(Select_Level(user_input))
