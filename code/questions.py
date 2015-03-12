questions = [["""1) What system is used to classify UK trains?
1 - MOTS
2 - TPOS
3 - TOPS
4 - GURA

Answer: ""","MOTS","TPOS","TOPS","GURA"],
["""2) What was the earliest mechanised meathod of hauling trains?
1 - Horse
2 - Electricity
3 - Diesel
4 - Steam

Answer: ""","Horse", "Electricity", "Diesel", "Steam"],
["""3) Who was in charge of Britian's railways in 1980?
1 - National Rail
2 - British Rail
3 - Regional Rail
4 - English Rail

Answer: ""","National Rail", "British Rail", "Reigonal Rail", "English Rail"],
["""4) What class of trains are nicknamed "dusty bins"?
1 - 123
2 - 455
3 - 287
4 - 321

Answer: ""","123","455","287","321"],
["""5) What was the first railway to use steam power?
1 - Middleton
2 - Stockton and Darlington
3 - Great Western
4 - Liverpool and Manchester

Answer: """, "Middleton","Stockton and Darlington", "Great Western", "Liverpool and Manchester"],
["""6) What is the UK's longest station name?
1 - Llanfairpwllgwyndgll-gogerychayrndrobwll-llantysilio-gogogoch
2 - Llanfairpwllgwyngyll-gogerychwyrsafrobwll-llantysilio-gogogoch
3 - Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch
4 - Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gomogoch

Answer: ""","Llanfairpwllgwyndgll-gogerychayrndrobwll-llantysilio-gogogoch", "Llanfairpwllgwyngyll-gogerychwyrsafrobwll-llantysilio-gogogoch","Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch", "Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gomogoch"],
["""7) What tube station has the least passenger usage?
1 - Swiss Cottage
2 - Roding Valley
3 - Epping
4 - Croxley

Answer: ""","Swiss Cottage", "Roding Valley", "Epping", "Croxley"],
["""8) What is the world's fastest steam locomotive?
1 - Sir Nigel Gresley
2 - City of Truro
3 - Swan
4 - Mallard

Answer: """, "Sir Nigel Gresley", "City of Truro", "Swan", "Mallard",],

["""9) When did the 1973 tube stock enter service?
1 - 1973
2 - 1974
3 - 1975
4 - 1976

Answer: ""","1973","1974","1975","1976"],
["""10) What is the fastest conventional (wheel on rail) train?
1 - French TGV POS
2 - German ICE 3
3 - Japansese E5/6 Shinkansen
4 - All of the above

Answer: ""","French TGV POS", "German ICE 3", "Japansese E5/6 Shinkansen", "All of the above",]]

answers = [[3,0],[4,0],[2,0],[4,0],[1,0],[3,0],[2,0],[4,0],[3,0]]

def ask():
    score = 0
    for i in range(9):
        while True:
            answer = int(input(questions[i][0]))
            if answer <= 4 or answer >= 1:
                break
            else:
                print("Enter answer between 1 and 4")
        answers[i][1] = answer
        if answer == answers[i][0]:
            score += 1
    return answers,questions,score
