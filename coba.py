# Updated data based on the second table
v1 = [1.50, 1.20]  # kecepatan awal benda 1 (m/s)
p1 = [2.25, 1.80]  # momentum awal benda 1 (kg.m/s)
p2 = [-1.30, -0.65]  # momentum awal benda 2 (kg.m/s)
p1_prime = [-1.23, -0.57]  # momentum akhir benda 1 (kg.m/s)
p2_prime = [2.18, 1.72]  # momentum akhir benda 2 (kg.m/s)

# Re-plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(v1, p1, label="P1 (Awal)", marker='o', linestyle='--', color='blue')
plt.plot(v1, p2, label="P2 (Awal)", marker='o', linestyle='--', color='green')
plt.plot(v1, p1_prime, label="P1' (Akhir)", marker='o', linestyle='-', color='red')
plt.plot(v1, p2_prime, label="P2' (Akhir)", marker='o', linestyle='-', color='purple')

# Labeling axes and title
plt.xlabel("Kecepatan Benda 1 (v1) [m/s]")
plt.ylabel("Momentum [kg.m/s]")
plt.title("Pengaruh Kecepatan terhadap Momentum")
plt.legend()
plt.grid(True)
plt.show()

