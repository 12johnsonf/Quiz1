import intro
import questions
import corrections
import wellDone
intro.greet()
a,b,c = questions.ask()
corrections.correct(a,b)
wellDone.congrats(c)
