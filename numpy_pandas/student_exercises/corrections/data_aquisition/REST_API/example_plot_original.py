def example_plot(x,y,label):
  import matplotlib.pyplot as plt

  fig = plt.figure
  plt.plot(x, y, label=label)
  plt.legend()
  plt.xlabel("Date")
  plt.ylabel("Unemployment rate")
  plt.title("Unemployment rate from 2015 to 2023")
  # show the x values only once per date
  plt.xticks(x[::12], rotation=90)

  return fig