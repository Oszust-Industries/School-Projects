## Space Adventure Game (School Project) - Oszust Industries
## Created on: 5-24-21 - Last update: 2-26-22
gameVersion = "v1.0.1"
import random
from random import randrange
 
def gameSetup():
    ## Setup game
    global playerDefense
    global playerAttack
    global playerSpeed
    global playerCargo
    global alreadyRead
    global crewChoosing
    global randomNumber
    global missionPlanet
    global missionTimer
    global engineFailure
    global scoutPlanet
    global menuOption
    global gameChoice
    playerDefense = 0
    playerAttack = 0
    playerSpeed = 0
    playerCargo = 0
    alreadyRead = False
    crewChoosing = 1
    randomNumber = 0
    missionPlanet = ""
    missionTimer = -1
    scoutPlanet = False
    engineFailure = False
    menuOption = ""
    gameChoice = ""
 
def startMenu():
    ## Game Start Menu
    global menuOption
    if menuOption == "":
        clearScreen()
        print("Welcome to Space Adventure. " + gameVersion)
        print("Created and published by Oszust Industries\n\n\n")
    else:
        storyClearScreen()
    print("1 - Start Game")
    print("2 - Game Help")
    print("3 - Quit Game")
    menuOption = input(str("\nType a number. (1/2/3) "))
    menuOption = menuOption.replace(" ", "")
    if menuOption.lower() in ["1", "start", "game"]:
        clearScreen()
        captainChoice()
    elif menuOption.lower() in ["2", "help", "tips"]:
        clearScreen()
        print("Game Help:\n")
        print("This game is a choose your own adventure game."
        "\nYou are a captain of a spaceship on a random mission."
        "\nYour choices will change the mission's outcome."
        "\n\nYou will start by picking a ship."
        "\nEach ship has their own stats that will affect your mission."
        "\n\nNext, you will pick crew members that will increase your ship's stats."
        "\nThe amount of crew members you can choose, is determined by how much your ship can hold."
        "\n\nYour ship's stats can change the story and cause random events to occur."
        "\nBe sure to balance your stats. All of the stats are equally important.")
        print("\n\n")
        startMenu()
    elif menuOption.lower() in ["3", "quit", "exit"]:
        print("\n\n\nQuitting Game...\n\n\n")
        quit()
    else:
        print("\n\nPlease type a number. (1/2/3)\n\n\n\n\n")
        startMenu()

def clearScreen():
    ## Clear User Screen
    print("\n" * 70)

def showUserStats():
    ## Show User Stats
    print("-" * 20)
    print("Ship Defense: " + str(playerDefense))
    print("Ship Attack: " + str(playerAttack))
    print("Ship Speed: " + str(playerSpeed))
    print("Ship Storage: " + str(playerCargo))
    if missionTimer > -1:
        print("Mission Time Remaining: " + str(missionTimer) + " hours")
    print("-" * 20 + "\n")

def storyClearScreen():
    print("-" * 80)
    print("\n\n")

def askToRestart():
    ## Quit to Menu
    gameChoice = input(str("\n\n\nPush Enter to Quit to Menu..."))
    gameChoice = ""
    if gameChoice == "":
        gameSetup()
        startMenu()

def checkMissionTime():
    ## Check Mission Time Left
    global storyLocation
    if storyLocation != 0:
        if missionTimer <= 0:
            storyLocation == -1
            print("You ran out of time and failed your mission.")
            askToRestart()

def packageMission():
    ## Package Pickup Mission
    global gameChoice
    global storyLocation
    global playerDefense
    global playerAttack
    global playerSpeed
    global playerCargo
    global missionTimer
    global engineFailure
    global scoutPlanet
    storyClearScreen()
    checkMissionTime()
    if storyLocation == 0:
        print("Your mission: Fly to planet " + str(missionPlanet) + " and retrieve a package. Return to Earth with the package. The package is being guarded by an enemy alien race. You have only 24 hours to complete your mission. Good Luck on your mission.")
        print("Type 'stats' at any time to see your ship's current stats and mission time remaining.")
        missionTimer = 24
        storyLocation = 1
    ## One section of the story
    elif storyLocation == 1:
        ## Launch
        print("One of your crew members tells you, 'We are ready for takeoff. Let us know when you are ready.' \n\n1-We are a go for launch \n2-Double-check the equipment(-0.5 hours)")
        gameChoice = input(str(""))
        print("\n")
        if gameChoice.lower() == "stats":
            showUserStats()
        elif gameChoice == "1":
            storyLocation = 2
            print("You decide that there is no time to double-check equipment and clear the ship for launch.")
        elif gameChoice == "2":
            storyLocation = 2
            print("Your crew spends the next half an hour checking the equipment aboard the ship. You find you're missing a few weapons and replace them before taking off. (+5 Ship Attack)")
            missionTimer -= 0.5
            playerAttack += 5
        else:
            print("This was not a choice.")
    ## End of section
    elif storyLocation == 2:
        ## Take-off
        print("Your spaceship takes off, and the launch is fairly smooth. You make your way to the ship bridge. The pilots ask you, 'Would you like me to fly directly to the planet or allow you to scout it out from a distance?' \n\n1-Fly straight to planet \n2-Let me scout out the planet out.")
        gameChoice = input(str(""))
        print("\n")
        if gameChoice.lower() == "stats":
            showUserStats()
        elif gameChoice == "1":
            storyLocation = 3
            print("You tell the pilot to fly directly to the planet. He says, 'You got it, captain.' He hits a few buttons at his console, and the ship takes off.")
            scoutPlanet = False
        elif gameChoice == "2":
            storyLocation = 3
            print("You tell the pilot to let you scout the planet first. He says, 'You got it, captain.' He hits a few buttons at his console, and the ship takes off.")
            scoutPlanet = True
        else:
            print("This was not a choice.")
    elif storyLocation == 3:
        ## Engine Failure
        if playerSpeed < 50:
            print("The flight to the planet is going well. Almost too perfect, suddenly red lights begin to flash around the bridge. Someone yells, 'Captain, we have engine problems. We are losing fuel fast.\nWe could attempt to continue flying or stop and make repairs. The repairs could take a few hours.' \n\n1-We better make repairs(-3 hours) \n2-Stay the course")
            gameChoice = input(str(""))
            print("\n")
            if gameChoice.lower() == "stats":
                showUserStats()
            elif gameChoice == "1":
                storyLocation = 4
                missionTimer -= 3
                print("You know better than to fly with a damaged ship. You tell the crew to stop and make repairs. The next three hours go by slowly.")
            elif gameChoice == "2":
                storyLocation = 4
                print("You tell the crew to stay the course. Nothing will stop you from achieving your mission. (-10 Ship Speed)")
                engineFailure = True
                playerSpeed -= 10
            else:
                print("This was not a choice.")
        else:
            print("The flight to the planet is smooth. It was a good thing you hired so many pilots.")
            storyLocation = 4
    elif storyLocation == 4:
        ## Approach Planet
        if engineFailure == False:
            if scoutPlanet == False:
                print("The pilot tells you, 'Captain, we are approaching the planet. The ship exits Hyperspeed and appears in the middle of three battleships.' \n\n1-Shields up \n2-Open fire!")
                gameChoice = input(str(""))
                print("\n")
                if gameChoice.lower() == "stats":
                    showUserStats()
                elif gameChoice == "1":
                    if playerDefense < 40:
                        print("You tell the crew to put shields up. Gunfire emerges from the other ships and begins hitting you. \nYour defense is too weak, and the opposing ships take a couple of blasts and leave your ship beyond repair. You failed your mission.")
                        askToRestart()
                    else:
                        storyLocation = 5
                        print("You tell the crew to put shields up. Gunfire emerges from the other ships and begins hitting you. Your defense is powerful, and you continue to fly by the other ships to the planet.")
                elif gameChoice == "2":
                    if playerAttack < 40:
                        print("You tell the crew to open fire. Gunfire emerges from your ship and begins hitting the other ships. \nYour attack is too weak. After a few blasts from the other ships, they leave your ship beyond repair. You failed your mission.")
                        askToRestart()
                    else:
                        storyLocation = 5
                        print("You tell the crew to open fire. Gunfire emerges from your ship and begins hitting the other ships. Your attack is powerful, and in no time, you destroy the other ships.")
                else:
                    print("This was not a choice.")
            else:
                print("The pilot tells you, 'Captain, we are approaching the planet. The ship exits Hyperspeed, and you are about 100,000 feet away from the planet. It was a good thing you scouted the planet. You see three vessels ahead blocking the planet.' \n\n1-Shields up \n2-Open fire!")
                missionTimer -= 1
                gameChoice = input(str(""))
                print("\n")
                if gameChoice.lower() == "stats":
                    showUserStats()
                elif gameChoice == "1":
                    if playerDefense < 40:
                        print("You tell the crew to put shields up. Gunfire emerges from the other ships and begins hitting you. \nYour defense is too weak, and the opposing ships take a couple of blasts and leave your ship beyond repair. You failed your mission.")
                        askToRestart()
                    else:
                        storyLocation = 5
                        print("You tell the crew to put shields up. Gunfire emerges from the other ships and begins hitting you. Your defense is powerful, and you continue to fly by the other ships to the planet.")
                elif gameChoice == "2":
                    if playerAttack < 40:
                        print("You tell the crew to open fire. Gunfire emerges from your ship and begins hitting the other ships. \nYour attack is too weak. After a few blasts from the other ships, they leave your ship beyond repair. You failed your mission.")
                        askToRestart()
                    else:
                        storyLocation = 5
                        print("You tell the crew to open fire. Gunfire emerges from your ship and begins hitting the other ships. Your attack is powerful, and in no time, you destroy the other ships.")
                else:
                    print("This was not a choice.")
        else:
            print("You continue your flight until suddenly, red lights brightly flash again around the cabin. A pilot says, 'Captain, we have lost all fuel and are now stranded.' You failed your mission.")
            askToRestart()
    elif storyLocation == 5:
        ## Finish
        print("You land on the planet and secure the package. You return to your ship and begin to head home. You begin to hear noises from the package. \n\n1-Open the package \n2-Better not touch it")
        gameChoice = input(str(""))
        print("\n")
        if gameChoice.lower() == "stats":
            showUserStats()
        elif gameChoice == "1":
            print("You decide to open the package. A weird slimy alien emerges and instantly makes a run for it. The alien is running loose on your ship causing issues. You failed your mission.")
            askToRestart()
        elif gameChoice == "2":
            storyLocation = 6
            print("You know whatever is in the package is well above your pay grade. You leave it alone and fly back to planet Earth.")
        else:
            print("This was not a choice.")
    elif storyLocation == 6:
        ## Story Done
        print("You land on planet Earth. You have successfully completed your mission. The commanders approach you and say, \n'We are surprised to see you again. We heard about the blockade and believed you wouldn't return home. You did it and got the package. Nice job!'")
        askToRestart()
    else:
        print("GAME ERROR(Broken Mission Hole - packageMission)")
        exit()
    packageMission()

def startMission():
    ## Pick Mission
    global randomNumber
    global missionPlanet
    global storyLocation
    planetNames = ["Mars", "Ego", "Coruscant"]
    missionPlanet = (random.choice(planetNames))
    storyLocation = 0
    randomNumber = randrange(1,2)
    if randomNumber == 1:
        packageMission()
    else:
        print("GAME ERROR(No Available Mission)")

def spaceLeft():
    ## Ship Space Left
    global crewMemberAmount
    crewMemberAmount = ((playerCargo - 10) / 5)
    crewMemberAmount = int(crewMemberAmount)
    print("\nYou have room for " + str(crewMemberAmount) + " crew members.")

def notEnoughSpace():
    ## Ship Space Unavailable
    global alreadyRead
    print("\nYou do not have enough room to fit the new crew members. Please pick a lower number.")
    alreadyRead = True
    crewSize()

def notANumber():
    ## User Types Not Number
    global alreadyRead
    print("\nPlease type a number.")
    alreadyRead = True
    crewSize()
 
def crewSize():
    ## User Picks Crew
    global gameChoice
    global playerDefense
    global playerAttack
    global playerSpeed
    global playerCargo
    global alreadyRead
    global crewChoosing
    if alreadyRead == False:
        print("Time to pick your crew members for your mission.\n\n\nThere are three types of people that you can recruit.\n\n\nRecruit Types:\n\nMechanic - Increases your ship's defense\n\nTactical Officers - Increases your ships's attack\n\nPilot - Increases your ship's speed\n")
    if crewChoosing == 1:
        print("-" * 80)
        spaceLeft()
        gameChoice = input("\n\nHow many mechanics would you like on your mission? (Type a number) ")
        if gameChoice.isdigit():
            if (playerCargo - (int(gameChoice) * 5)) >= 10:
                print("\n" + gameChoice + " mechanics have been added to your ship.")
                crewChoosing = 2
                alreadyRead = True
                playerCargo -= (int(gameChoice) * 5)
                playerDefense += (int(gameChoice) * 5)
                print("Your ship's defense is now: " + str(playerDefense))
                crewSize()
            else:
                notEnoughSpace()
        else:
            notANumber()
    if crewChoosing == 2:
        print("-" * 80)
        spaceLeft()
        if crewMemberAmount == 0:
            print("You don't have room for any tactical officers.")
            crewChoosing = 3
        else:
            gameChoice = input("\n\nHow many tactical officers would you like on your mission? (Type a number) ")
            if gameChoice.isdigit():
                if (playerCargo - (int(gameChoice) * 5)) >= 10:
                    print("\n" + gameChoice + " guards have been added to your ship.")
                    crewChoosing = 3
                    playerCargo -= (int(gameChoice) * 5)
                    playerAttack += (int(gameChoice) * 5)
                    print("Your ship's attack is now: " + str(playerAttack))
                    crewSize()
                else:
                    notEnoughSpace()
            else:
                notANumber()
    if crewChoosing == 3:
        print("-" * 80)
        spaceLeft()
        if crewMemberAmount == 0:
            print("You don't have room for any pilots.")
            crewChoosing = 4
        else:
            gameChoice = input("\n\nHow many pilots would you like on your mission? (Type a number) ")
            if gameChoice.isdigit():
                if (playerCargo - (int(gameChoice) * 5)) >= 10:
                    print("\n" + gameChoice + " pilots have been added to your ship.")
                    crewChoosing = 4
                    playerCargo -= (int(gameChoice) * 5)
                    playerSpeed += (int(gameChoice) * 5)
                    print("Your ship's speed is now: " + str(playerSpeed))
                    crewSize()
                else:
                    notEnoughSpace()
            else:
                notANumber()
    if crewChoosing == 4:
        print("-" * 80)
        print("\nUpdated Ship Stats:")
        showUserStats()
        gameChoice = input(str("\n\n\nPush Enter to Start your mission..."))
    gameChoice = ""
    if gameChoice == "":
        clearScreen()
        startMission()

def captainChoice():
    ## User Picks Ship
    global gameChoice
    global playerDefense
    global playerAttack
    global playerSpeed
    global playerCargo
    if gameChoice == "":
        print("Time to pick a captain with a spaceship.\n\n\nEach captain owns their own ship with its own specs.\n\n\nShip Specifications:\n\nDefense - How well the ship can withstand enemy attack\n\nAttack - How well the ship can attack other ships.\n\nSpeed - How fast the ship can fly.\n\nCargo - How many resources the ship can hold.")
        print("-" * 80)
        print("\n\nCaptains:\n\n1.Captain Morpheus - Ship Defense: 15, Ship Attack: 30, Ship Speed: 10, Ship Cargo: 65\n\n2.Captain Solo - Ship Defense: 15, Ship Attack: 10, Ship Speed: 20, Ship Cargo: 75\n\n3.Captain Kirk - Ship Defense: 25, Ship Attack: 15, Ship Speed: 10, Ship Cargo: 70\n\n4.Captain Star-Lord - Ship Defense: 10, Ship Attack: 15, Ship Speed: 40, Ship Cargo: 55\n")
        print("-" * 80)
    gameChoice = input(str("\n\nWhich captain would you like to use on your mission? (Type 1/2/3/4) "))
    if gameChoice == "1":
        playerDefense += 15
        playerAttack += 30
        playerSpeed += 10
        playerCargo += 65
    elif gameChoice == "2":
        playerDefense += 15
        playerAttack += 10
        playerSpeed += 20
        playerCargo += 75
    elif gameChoice == "3":
        playerDefense += 25
        playerAttack += 10
        playerSpeed += 20
        playerCargo += 70
    elif gameChoice == "4":
        playerDefense += 10
        playerAttack += 15
        playerSpeed += 40
        playerCargo += 55
    else:
        print("\nPlease type 1, 2, 3, or 4 to choose a captain.")
        print("-" * 80)
        captainChoice()
    clearScreen()
    crewSize()
 

## Start System
gameSetup()
startMenu()