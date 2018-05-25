import matplotlib.pyplot as plt
import csv

def graph(player):

    player2 = []
    score = 0

    for i in range(len(player)): # assigns colors to strikes and balls
        if player[i][0] == "Called Strike":
            player[i].append("red")
            player2.append(player[i])
            if player[i][1] >= -8.5/12 and player[i][1] <= 8.5/12 and player[i][2] >= 1.5 and player[i][2] <= 3.4:
                score += 1
        if player[i][0] == "Ball":
            player[i].append("blue")
            player2.append(player[i])
            if player[i][1] <= -8.5/12 or player[i][1] >= 8.5/12 or player[i][2] <= 1.5 or player[i][2] >= 3.4:
                score += 1

    print(player2)
    print(score, '/', len(player2))
    acc = (score/len(player2)) * 100
    print(acc)


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
    plt.xlabel('x(ft)')
    plt.ylabel('y(ft)')
    plt.title('Pitch-Plot', fontsize=30)
    plt.axis([-4, 4, 0, 6]) # xmin, xmax, ymin, ymax
    plt.annotate('= Ball', xy=(3, 5.6))
    plt.annotate('= Strike', xy=(3, 5.3))
    plt.annotate('Accuracy = ' + str(acc), xy=(2.7, 5.1))
    plt.plot(2.8, 5.7, color='blue', marker='.', markersize=15, alpha=0.3)
    plt.plot(2.8, 5.4, color='red', marker='.', markersize=15, alpha=0.3)

    #---------
    q = [2.5, 4]
    z = [4.7, 4.7]
    q2 = [2.5, 2.5]
    z2 = [4.7, 6]
    plt.plot(q, z, color='black')
    plt.plot(q2, z2, color='black')
    #----------

    plt.show()



player = [['Ball', 3, 2.5], ['Called Strike', 0, 3], ['Swinging Strike', 1, 1]]
graph(player)