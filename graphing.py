import matplotlib.pyplot as plt


def graph(player):

    player2 = []
    score = 0

    # Creating new pitch list and assigning attributes ----
    for i in range(len(player)):  # assigns colors to strikes and balls
        if player[i][0] == "Called Strike":
            if player[i][1] >= -8.5/12 and player[i][1] <= 8.5/12 and player[i][2] >= 1.5 and player[i][2] <= 3.4:
                score += 1
                player[i].append(".")
                player[i].append('22.2')
                player[i].append("red")
                player[i].append(0.3)
            else:
                player[i].append("x")
                player[i].append('6')
                player[i].append("black")
                player[i].append(1)
            player2.append(player[i])
        if player[i][0] == "Ball":
            if player[i][1] <= -8.5/12 or player[i][1] >= 8.5/12 or player[i][2] <= 1.5 or player[i][2] >= 3.4:
                score += 1
                player[i].append(".")
                player[i].append('22.2')
                player[i].append("blue")
                player[i].append(0.3)
            else:
                player[i].append("x")
                player[i].append('6')
                player[i].append("black")
                player[i].append(1)
            player2.append(player[i])

    print(player2)
    # -----------------------------------------------------

    # Ump acc ---
    print(score, '/', len(player2))
    try:
        acc = (score/len(player2)) * 100
    except:
        acc = "ERROR"
    print(acc)
    # -----------

    # matplotlib stuff VVV

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

    # plotting the pitches
    for x in range(len(player2)):
        plt.plot(player2[x][1], player2[x][2], color=player2[x][5], marker=player2[x][3], markersize=player2[x][4], alpha=player2[x][6])

    # labels/legend
    plt.xlabel('x(ft)')
    plt.ylabel('y(ft)')
    plt.title('Pitch-Plot', fontsize=30)
    plt.axis([-4, 4, 0, 6])
    plt.annotate('= Ball', xy=(2.5, 5.6))
    plt.annotate('= Strike', xy=(2.5, 5.3))
    plt.annotate('= Bad Call', xy=(2.5, 5))
    plt.annotate(str(round(acc, 2)) + '% accurate calls', xy=(-3.9, 5.8))
    plt.plot(2.3, 5.7, color='blue', marker='.', markersize=15, alpha=0.3)
    plt.plot(2.3, 5.4, color='red', marker='.', markersize=15, alpha=0.3)
    plt.plot(2.3, 5.1, color='black', marker='x', markersize=6, alpha=1)

    # legend box ---
    q = [2, 4]
    z = [4.7, 4.7]
    q2 = [2, 2]
    z2 = [4.7, 6]
    plt.plot(q, z, color='black')
    plt.plot(q2, z2, color='black')
    # --------------

    plt.show()
