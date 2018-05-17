import matplotlib.pyplot as plt
import csv


player = [["S", -0.7658482420671984, 1.6747617772755894], ["B", 1.439627916358238, 2.2601938107350796]] #[type, px, pz]

for i in range(len(player)): # assigns colors to strikes and balls
    if player[i][0] == "S":
        player[i].append("red")
    else:
        player[i].append("blue")

print(player[1])


plt.figure(1)



for x in range(len(player)):
    plt.plot(player[x][1], player[x][2], color=player[x][3], marker='^', markersize=4)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pitch-Plot', fontsize=30)
plt.axis([-4, 4, 0, 6]) # xmin, xmax, ymin, ymax




plt.show()