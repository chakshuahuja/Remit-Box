import sqlite3 as lite
import plotly.plotly as py
import plotly.graph_objs as go
import sys

con = lite.connect('testDB.db')

arr_action = {}
arr_action['SMS'] = 0
arr_action['mail'] = 0
arr_keywords = {}
keywords = []
y1 = []
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM actions")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        if str(row[4]) == "SMS": 
            arr_action['SMS'] += 1
        else:
            arr_action['mail'] += 1
            
            keywords.append(str(row[2]))
            
unique_keys = set(keywords)
for s in keywords:
    if s in arr_keywords:
        arr_keywords[s] += 1
    else:
        arr_keywords[s] = 1

print arr_action
print arr_keywords

data = [
    go.Bar(
        x=['SMS', 'MAIL'],
        y=[arr_action['SMS'], arr_action['mail']]
    )
]
plot_url = py.plot(data, filename='basic-bar')

for i in keywords:
    y1.append(arr_keyword[i])
    
    
data1 = [
    go.Bar(
        x = keywords,
        y = y1
    )
]
plt.show()
plot_url = py.plot(data1, filename='basic-bar1')
