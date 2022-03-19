import plotly.express as px
import csv

with open("Student Marks vs Days Present.csv") as a:
    data_f = csv.DictReader(a)
    fig = px.scatter(data_f, x="Marks In Percentage", y="Days Present")
    fig.show()

with open("cups of coffee vs hours of sleep.csv") as b:
    d_frame = csv.DictReader(b)
    fig2 = px.scatter(d_frame, x="Coffee in ml", y="sleep in hours")
    fig2.show()