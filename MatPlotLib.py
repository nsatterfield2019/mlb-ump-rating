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

# strike zone ---

x = [-0.85, 0.85]
y = [3.4, 3.4]
x2 = [0.85, -0.85]
y2 = [1.5, 1.5]
x3 = [-0.85, -0.85]
y3 = [3.4, 1.5]
x4 = [0.85, 0.85]
y4 = [3.4, 1.5]
plt.plot(x, y, color='black', linestyle='--')
plt.plot(x2, y2, color='black', linestyle='--')
plt.plot(x3, y3, color='black', linestyle='--')
plt.plot(x4, y4, color='black', linestyle='--')


for x in range(len(player)):
    plt.plot(player[x][1], player[x][2], color=player[x][3], marker='^', markersize=4)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pitch-Plot', fontsize=30)
plt.axis([-4, 4, 0, 6]) # xmin, xmax, ymin, ymax




plt.show()