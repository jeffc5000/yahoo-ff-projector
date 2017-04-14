#!/usr/bin/python

import itertools
import operator

# snapshot of league as it stands after week 13
current = {
"STR": (8,5,1417.24),
"NTF": (8,5,1122.20),
"TEV": (7,6,1280.14),
"MAX": (7,6,1199.88),
"AAA": (7,6,1087.22),
"RAM": (6,7,1234.18),
"DAM": (6,7,1214.94),
"CHK": (6,7,1178.06),
"JTT": (6,7,1154.40),
"KRA": (4,9,1154.76) 
}

# matchups for week 14
wk14games = (["STR","DAM"],["AAA","TEV"],["NTF","CHK"],["JTT","KRA"],["RAM","MAX"])

allOutcomes = list(itertools.product(*wk14games))

# we need to iterate through each possible set of outcomes for the 5 matchups
for outcomeNo in range(len(allOutcomes)):
	outcome = allOutcomes[outcomeNo]
	print "######################################################"
	print "# Model", ('%2d' % (outcomeNo + 1)), ":", outcome, "    #"
	print "######################################################"
	# set up dict for future season results 
	modelFuture = {}
	#have to now split the list of 5 matchups so we can update standings  
	for i in range(len(outcome)):

		#determine the winner & loser from the wk14games
		if ( outcome[i] == wk14games[i][0]):
			winner = wk14games[i][0]
			loser = wk14games[i][1]
		else:
			winner = wk14games[i][1]
			loser = wk14games[i][0]

		# do math to calc new w/l for each team
		modelFuture[winner] = ( current[winner][0] + 1, current[winner][1], current[winner][2] )
		modelFuture[loser] = ( current[loser][0], current[loser][1] + 1, current[loser][2] )

	# be able to sort by top winner
	s_future = sorted(modelFuture.items(), key=operator.itemgetter(1), reverse=True)		
	
	# now print updated league results
	print "============================="
	print "#  | Team | W | L | Pts     |"
	print "============================="
	for k in range(len(s_future)):
		print ('%2d' % (k + 1)), "|", s_future[k][0], " |", s_future[k][1][0], "|", s_future[k][1][1],"|", ('%.2f' % s_future[k][1][2]), "|"
	print "============================="

