import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

ON = 1
OFF = 0
values = [ON, OFF]

def initialState(N):
  return np.random.choice(values, N * N, p=[0.15, 0.85]).reshape(N, N)

def updateGrid(frameNum, img, grid, ages, N, cmap):
  newGrid = grid.copy()
  newAges = ages.copy()

  for i in range(N):
    for j in range(N):
      n1 = grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, j] + grid[(i - 1) % N, (j + 1) % N]
      n2 = grid[i, (j - 1) % N] + grid[i, (j + 1) % N]
      n3 = grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, j] + grid[(i + 1) % N, (j + 1) % N]
      neighbours = n1 + n2 + n3

      if grid[i, j] == ON:
        if neighbours > 3 or neighbours < 2:
          newGrid[i, j] = OFF
        elif neighbours == 2 or neighbours == 3:
          newAges[i, j] += 1

      elif grid[i, j] == OFF and neighbours == 3:
        newGrid[i, j] = ON
        newAges[i, j] = 1

  color_map = np.zeros((N, N), dtype=int)

  for i in range(N):
    for j in range(N):
      if grid[i, j] == ON:
        if newAges[i, j] == 1:
          color_map[i, j] = 1
        elif newAges[i, j] == 2:
          color_map[i, j] = 2
        else:
          color_map[i, j] = 3

  img.set_data(color_map)
  img.set_cmap(cmap)
  img.set_clim(vmin=0, vmax=3)

  grid[:] = newGrid[:]
  ages[:] = newAges[:]

  return img

def main():
  N = 100
  grid = initialState(N)
  ages = np.zeros_like(grid)
  cmap = ListedColormap(['black', 'white', 'green', 'blue'])

  fig, ax = plt.subplots()
  ax.set_title("Gra w życie Conwaya")
  img = ax.imshow(grid, cmap=cmap)

  legend_labels = [
    mpatches.Patch(color='white', label="Przeżyła 1 generację"),
    mpatches.Patch(color='green', label="Przeżyła 2 generacje"),
    mpatches.Patch(color='blue', label="Przeżyła 3+ generacje"),
  ]
  ax.legend(handles=legend_labels, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)
  fig.subplots_adjust(bottom=0.2) 

  ani = animation.FuncAnimation(
    fig, updateGrid, fargs=(img, grid, ages, N, cmap),
    frames=None, interval=100, cache_frame_data=False)

  plt.show()

main()
