questions = [["""1) What system is used to refer to UK trains?
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
["""3) Who was in charge of Britian's railways in 1960?
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

Answer: """, "Middleton" ,""],
["""6) What is the UK's longest station name?
Llanfairpwllgwyndgll-gogerychayrndrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrsafrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch
Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gomogoch

Answer (you can copy and paste): ""","Llanfairpwllgwyngyll-gogerychwyrndrobwll-llantysilio-gogogoch",],
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

Answer: ""","Mallard",""],
["""9) When did the 1973 stock enter service?
1973
1974
1975
1976

Answer: ""","1975",""],
["""10) What is the fastest conventional (wheel on rail) train?
French TGV POS
German ICE 3
Japansese E5/6 Shinkansen
All of the above

Answer: ""","All of the above",""]]

global score
score = 0
for i in range(10)
    answer = input(questions[i][0])
    if answer == questions[i][1]
        score += 1
        questions[i][2] = answer
