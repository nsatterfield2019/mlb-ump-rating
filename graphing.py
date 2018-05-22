import matplotlib.pyplot as plt
import csv

def graph(player):

    player2 = []

    for i in range(len(player)): # assigns colors to strikes and balls
        if player[i][0] == "Called Strike" or player[i][0] == "Swinging Strike":
            player[i].append("red")
            player2.append(player[i])
        if player[i][0] == "Ball":
            player[i].append("blue")
            player2.append(player[i])

    print(player2)



    plt.figure(1)

    # strike zone ---

    x = [-8.5/12, 8.5/12]
    y = [3.4, 3.4]
    x2 = [8.5/12, -8.5/12]
    y2 = [1.5, 1.5]
    x3 = [-8.5/12, -8.5/12]
    y3 = [3.4, 1.5]
    x4 = [8.5/12, 8.5/12]
    y4 = [3.4, 1.5]
    plt.plot(x, y, color='black', linestyle='--')
    plt.plot(x2, y2, color='black', linestyle='--')
    plt.plot(x3, y3, color='black', linestyle='--')
    plt.plot(x4, y4, color='black', linestyle='--')

    # ----------------

    # graphing
    for x in range(len(player2)):
        plt.plot(player2[x][1], player2[x][2], color=player2[x][3], marker='.', markersize=22.2, alpha=0.3)
    # labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pitch-Plot', fontsize=30)
    plt.axis([-4, 4, 0, 6]) # xmin, xmax, ymin, ymax


    plt.show()