Psuedocode:
	```
	READ name
	WRITE "Welcome to the quiz, ", name
	score = 0
	questions = 2D array
	i = 0
	WHILE i < 5
		count +=1
		WRITE questions[i][0]
		READ answer
		IF answer == questions[i][1]
			score += 1
			questions[i][2] = answer
		ENDIF
	ENDWHILE
	j = 0
	WHILE j > 5:
		IF questions [i][1] == questions[i][2]
			WRITE questions[i][0], questions[i][2], "RIGHT"
		ELSE
			WRITE questions[i][0], questions[i][2], "WRONG"
		ENDIF
	ENDWHILE
	WRITE name, " your score is " score
	f = open leaderboard.txt r+
	b = f - line 10 [:1]
	IF f 
	```
