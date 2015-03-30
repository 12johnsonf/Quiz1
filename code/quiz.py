import intro ,questions, corrections, wellDone, leaderboard
n = intro.greet()
a,b,c = questions.ask()
corrections.correct(a,b)
wellDone.congrats(c)
leaderboard.leader(c,n)
input('Press enter to exit')
