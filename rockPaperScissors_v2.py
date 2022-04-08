# =========== OBJECT STORAGE =============================================================================
## Game Tittle and Rules ---------------------------------------------------------------------------------
gameTitleRules = """
+++++++++++++++++++++++++++++++++++++++
+++++ ROCK +++ PAPER +++ SCISSORS +++++
+++++++++++++++++++++++++++++++++++++++
+------------- Rules -----------------+
+        ROCK crushes SCISSORS        +
+      SCISSORS cut PAPER             +
+       PAPER covers ROCK             +
+++++++++++++++++++++++++++++++++++++++
"""

## Acceptable Answers Dictionary -------------------------------------------------------------------------
global acceptAnswers; acceptAnswers = {
    "rock": ["rock", "rocks", "r"],
    "paper": ["paper", "papers", "p"],
    "scissors": ["scissor", "scissors", "s"]
}
# print(acceptAnswers)
## Acceptable Answers Check List --------------------------------------------------------------------------
global answerCheckList; answerCheckList = [item for sublist in acceptAnswers.values() for item in sublist]
# print(answerCheckList)
## Outcome Rules ------------------------------------------------------------------------------------------
global outcomes; outcomes = {
    "rock": {"rock": "draw", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "draw", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "draw"}
}
# print(outcomes)
# =========== FUNCTIONS ===================================================================================
## Get keys (in dictionary) from players' input -----------------------------------------------------------
def get_answer_key(valueInput):
    for key, value in acceptAnswers.items():
        if valueInput in value:
            return key

## Confirm Solo or Muti-Players Game ----------------------------------------------------------------------
def get_playerNumber():
    while True:
        try:
            global playerNumber; playerNumber = int(input("Enter the Number of Player(s): "))
            if playerNumber == 1:
                # print("Solo-Player")
                return playerNumber
            elif playerNumber == 2:
                # print("Multi-Player")
                return playerNumber
            else:
                print("Error: Enter 1 or 2 only!! Try Again!!")
                continue
        except:
            print("Error: Enter 1 or 2 only!! Try Again!!")
            continue

## Get Users' Information ---------------------------------------------------------------------------------
def get_users_info():
    if playerNumber == 1:
        global playerName; playerName = input("Enter Your Name: ")
        print(f"\n=========== {playerName.upper()} VS. COMPUTER ============\n{gameTitleRules}")
    else:
        global p1Name; p1Name = input("Enter the name of Player 1: ")
        global p2Name; p2Name = input("Enter the name of Player 2: ")
        print(f"\n=========== {p1Name.upper()} VS. {p2Name.upper()} ============\n{gameTitleRules}")

## Start Multi-Player Game ---------------------------------------------------------------------------------
def startGame_multiPlayers():
    # Get Inputs
    while True:
        global p1Opt; p1Opt = input("{p1}, Rock, Paper, or Scissors? ".format(p1=p1Name.upper())).lower()
        global p2Opt; p2Opt = input("{p2}, Rock, Paper, or Scissors? ".format(p2=p2Name.upper())).lower()

        if p1Opt.lower() in answerCheckList and p2Opt.lower() in answerCheckList:
            p1Opt = get_answer_key(p1Opt)
            p2Opt = get_answer_key(p2Opt)
            print(f"\n> {p1Name.upper()} chose {p1Opt} & {p2Name.upper()} chose {p2Opt} <!")
            
            result = outcomes.get(p1Opt).get(p2Opt)
            if result == "draw":
                print("\nIt's a tie!!!")
            else:
                print("\n>> {p1} {result1}s, {p2} {result2}s! <<".format(p1=p1Name.upper(), result1=outcomes.get(p1Opt).get(p2Opt), p2=p2Name.upper(), result2=outcomes.get(p2Opt).get(p1Opt)))
            break
        else:
            print("Error: Enter Rock, Paper, or Scissors only!! Try Again!!")
            continue

## Start Solo-Player Game ---------------------------------------------------------------------------------
def startGame_soloPlayer():
    while True:
        import random
        playerOpt = input(f"{playerName.upper()}, Rock, Paper, or Scissors? ").lower()
        
        if playerOpt.lower() in answerCheckList:
            opts = list(acceptAnswers.keys())
            playerOpt = get_answer_key(playerOpt)
            computerOpt = random.choice(opts)
            print(f"{playerName.upper()}, You chose {playerOpt}, Computer chose {computerOpt}.\n")
            
            result = outcomes.get(playerOpt).get(computerOpt)
            if result == "draw":
                print("\nIt's a tie!!!")
            else:
                print("{playerName} {result}s!".format(playerName=playerName.upper(), result=outcomes.get(playerOpt).get(computerOpt)))
            break
        else:
            print("Error: Enter Rock, Paper, or Scissors only!! Try Again!!")
            continue

def check_urs_command():
    import sys
    while True:
        global urs_command; urs_command = str(input("\nWould you like to play again? (yes/no): ")).lower()
        if urs_command == "yes" or urs_command == "no":
            if urs_command == "no":
                print("""
          //////////////////////
 ========///  !!END GAME!!  ///==========
        //////////////////////
""")
                sys.exit()
            else:
                print(gameTitleRules)
                break
        else:
            print("Error: Please only type \"yes\" or \"no\"!!")
            continue

# =========== GAME ON ==================================================================================


if __name__ == '__main__':
    get_playerNumber()
    get_users_info()
    while True:
        if playerNumber == 1:
            startGame_soloPlayer()
        else:
            startGame_multiPlayers()
        check_urs_command()
        continue