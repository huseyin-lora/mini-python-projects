import random
playerSwords = 3
playerPotions = 3
playerPoints = 0
print('You are in the middle of a maze.')
print('')
validMoveDirections = ['l', 'r', 'u', 'd']
events = ['M', 'P', 'T', 'E']
while (playerSwords >= 0) or (playerPotions >= 0):
    print('Where to go?')
    moveDirection = input('Left[L] Right[R] Up[U] Down[D]: ').lower()
    if moveDirection not in validMoveDirections:
        print('Invalid move. Game ends.')
        break
    else:
        event = random.choice(events)
        if event == 'M':
            print('A Monster!')
            if playerSwords > 0:
                playerSwords -= 1
                playerPoints += 1
                print('You saved yourself with a sword.')
            else:
                print('You die. No swords left.')
                break
        elif event == 'P':
            print('A Poison!')
            if playerPotions > 0:
                playerPotions -= 1
                playerPoints += 1
                print('You saved yourself with a potion.')
            else:
                print('You die. No potions left.')
                break
        elif event == 'T':
            print('A Treasure!')
            print('You earned two points!')
            playerPoints += 2

        elif event == 'E':
            print('An empty road. Go ahead!')
            playerPoints += 1
        print('')
        print('Points: ' + str(playerPoints))
        print('')
print('')
print('You lost. Game ends. Your points: ' + str(playerPoints))
