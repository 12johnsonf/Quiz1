Psuedocode:

```
	READ name
	WRITE "Welcome to the quiz, ", name
	WRITE "Answer questions with the exact text given"
	score = 0
	questions = 2D array
	i = 0
	WHILE i < 10
		count +=1
		WRITE questions[i][0]
		READ answer
		IF answer == questions[i][1]
			score += 1
			questions[i][2] = answer
		ENDIF
	ENDWHILE
	j = 0
	WHILE j > 10:
        	j += 1
		IF questions [i][1] == questions[i][2]
			WRITE questions[i][1], questions[i][2], "   RIGHT"
		ELSE
			WRITE questions[i][1], questions[i][2], "   WRONG"
		ENDIF
	ENDWHILE
	WRITE name, " your score is " score
	f = open leaderboard.txt r+
	l = 0
	WHILE l < 11
		IF score > f - line l[:1]
			f - line l = score, name
		ENDIF
	ENDWHILE
	WRITE f
	IF score > 6
		k = 0
		WHILE k > 5
			k += 1
			print "Well done"
		ENDWHILE
	ENDIF
```

Questions array:
```
questions = [["""1) What system is used to classify to UK trains?
MOTS
TPOS
TOPS
GURA

Answer: ""","TOPS",""],
["""2) What was the earliest mechanised meathod of hauling trains?
Horse
Electricity
Diesel
Steam

Answer: ""","Steam",""],
["""3) Who was in charge of Britian's railways in 1980?
National Rail
British Rail
Regional Rail
English Rail

Answer: ""","British Rail",""],
["""4) What class of trains are nicknamed "dusty bins"?
123
455
287
321

Answer: ""","321",""],
["""5) What was the first railway to use steam power?
Middleton
Stockton and Darlington
Great Western
Liverpool and Manchester

Answer: """, "Middleton",""],
["""6) What is the UK's longest station name?
Llanfairpwllgwyndgll-gogerychayrndrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrsafrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gomogoch

Answer (you can copy and paste): ""","Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch",""],
["""7) What tube station has the least passenger usage?
Swiss Cottage
Roding Valley
Epping
Croxley

Answer:  ""","Roding Valley",""],
["""8) What is the world's fastest steam locomotive?
Sir Nigel Gresley
City of Truro
Swan
Mallard

Answer: """, "Mallard", ""],

["""9) When did the 1973 tube stock enter service?
1973
1974
1975
1976

Answer: ""","1975",],
["""10) What is the fastest conventional (wheel on rail) train?
French TGV POS
German ICE 3
Japansese E5/6 Shinkansen
All of the above

Answer: ""","All of the above",]]
```
