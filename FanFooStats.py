#!python3

import requests, bs4, os, numpy
from collections import defaultdict

fooDict = defaultdict(list)
d3List = []

#Iterate over each week
for i in range(1, 14):
    week = requests.get('http://games.espn.com/ffl/scoreboard?leagueId=125892&matchupPeriodId=' + str(i))
    try:
        week.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    #Get the abbrev and score
    theSource = bs4.BeautifulSoup(week.text, "html.parser")
    scoreSource = theSource.select('.score')
    abbrevSource = theSource.select('span[class="abbrev"]')

    #Iterate over each score/abbrev, storing in dictionary, abbrev key: [score list]
    for j in range(10):
        abbrev = abbrevSource[j].getText()
        score = scoreSource[j].getText()
        fooDict[abbrev].append(score)
        #print(fooDict)

#Convert to dictionary, then list
fooDict = dict(fooDict)
fooList = list(fooDict.items())

#Iterate over each abbrev/score tuple
for k in fooList:

    #Get team name, then convert string scores to floats
    abbrev = k[0]
    scoreFloat = []
    for m in k[1]: 
        scoreFloat.append(float(m))
        
    #Calculate quartiles
    q1 = numpy.around(numpy.percentile(scoreFloat, 25))
    q2 = numpy.around(numpy.percentile(scoreFloat, 50))
    q3 = numpy.around(numpy.percentile(scoreFloat, 75))
    whisker_low = numpy.around(numpy.percentile(scoreFloat, 0))
    whisker_high = numpy.around(numpy.percentile(scoreFloat, 100))
    tempDict = {"Q1": q1, "Q2": q2, "Q3": q3, "whisker_low": whisker_low, "whisker_high": whisker_high}
    d3Dict = {}
    d3Dict["label"] = abbrev
    d3Dict["values"] = tempDict
    d3List.append(d3Dict)
    
#Sort by median
d3List.sort(key=lambda e: e["values"]["Q2"], reverse=True)

#Write the data to a text file
footballFile = open('footballData.txt', 'w')
footballFile.write(str(d3List))
footballFile.close()
