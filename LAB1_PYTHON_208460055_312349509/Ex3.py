"""
______________________________________________________________________________

                                EX 3

                        Rock Paper Scissors

_____________________________________________________________________________

"""
# print an ASCII art. want one for yourself? try googling "ASCII art"!!
print( """____   __    ___  __ _        ____   __   ____  ____  ____        ____   ___   __   ____  ____   __   ____  ____ 
(  _ \ /  \  / __)(  / )      (  _ \ / _\ (  _ \(  __)(  _ \      / ___) / __) (  ) / ___)/ ___) /  \ (  _ \/ ___)
 )   /(  O )( (__  )  (        ) __//    \ ) __/ ) _)  )   /      \___ \( (__   )(  \___ \\___ \(  O ) )   /\___ \\
(__\_) \__/  \___)(__\_)      (__)  \_/\_/(__)  (____)(__\_)      (____/ \___) (__) (____/(____/ \__/ (__\_)(____/""")

players = [0,0]
result = 0

# as long as there's a tie:
while result == 0:

    # get input from both players
    for i in range(2):
        players[i] = int(input(f"\n\nPLAYER {i+1}:\n\nplease choose your weapon: \n1:rock\n2:paper\n3:scissors\n "))

    # check for a tie brake
    if players[0] == players[1]:
        result = 0
        print('\nITS A TIE!!    ')

    else:
        # check for yourself! why does this line determine the winner?
        result = (players[0] - players[1]) % 3

print(f'player {result} wins!!!!!!!')



