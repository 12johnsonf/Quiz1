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
			WRITE questions[i][0], questions[i][2], "RIGHT"
		ELSE
			WRITE questions[i][0], questions[i][2], "WRONG"
		ENDIF
	ENDWHILE
	WRITE name, " your score is " score
	f = open leaderboard.txt r+
	b = f - line 10 [:1]
	IF b < score
		b = name, score
	ENDIF
	WRITE f (lines 1-10)
	IF score > 6
		k = 0
		WHILE k > 5
			k += 1
			print "Well done"
		ENDWHILE
	ENDIF
```

questions = [["""1) What system is used to refer to UK trains?
MOTS
TPOS
TOPS
GURA

Answer: ""","TOPS",],
["""2) What was the earliest mechanised meathod of hauling trains?
Horse
Electricity
Diesel
Steam

Answer: ""","Steam",],
["""3) Who was in charge of Britian's railways in 1960?
National Rail
British Rail
Regional Rail
English Rail

Answer: ""","British Rail",],
["""3) What class of trains are nicknamed "dusty bins"?,,],
[,,],
[,,],
[,,],
[,,],
[,,],
[,,]]
