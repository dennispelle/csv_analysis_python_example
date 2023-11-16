# Importing library
import plotly.express as px
import pandas as pd
# initialise data of lists.
csv_data = pd.read_csv("blabla.csv", delimiter=';', decimal=',',header=0,encoding='utf-16',skiprows=31)
print(csv_data.columns)


# Plotting Bar Plot für die tatsächlichen Daten mit aktiviertem Scroll-Zoom
plot = px.line(csv_data, x=csv_data.columns[0], y=csv_data.columns[1:16],
              title="Plot With Enabled Scroll Zoom")

# Zeigen Sie das Balkendiagramm mit Scroll-Zoom an
plot.show(config={'scrollZoom': True})
