import pandas as pd
import numpy as np
import sys
from pprint import pprint




if __name__ == '__main__':
	assert len(sys.argv) == 4, "Error, correct usage: %s <rollup> <KC Model Name> <output>" % sys.argv[0]

	rollup = sys.argv[1]
	kc_model_name = sys.argv[2]
	output = sys.argv[3]
	df = pd.read_csv(rollup, sep='\t')
	L = int(df["Opportunity (%s)" % kc_model_name].max())
	KCs = df["KC (%s)"%kc_model_name].unique()
	KCs = [x for x in KCs if x == x]
	print(KCs)
	print(L)

	gb = df.groupby(["KC (%s)"%kc_model_name,"Opportunity (%s)" % kc_model_name])
	# error = (gb["First Attempt"] == "correct").count()/gb["First Attempt"].count()
	columns = ["KC Name"] #+ np.arange(1,L+1).tolist()
	columns = [str(x) for x in columns]
	out = pd.DataFrame(0, index=np.arange(len(KCs)), columns=columns)
	out['KC Name'] = KCs
	kc_index_map = {kc:i for i,kc in enumerate(KCs)}
	print(out.keys())
	curves = {x:[0.0]*L for x in KCs}
	for (kc,opp), g in gb:
		opp = int(opp)
		errors = g["First Attempt"] != 'correct'
		# s = sum(errors)
		# print(len(errors))
		print(kc,opp)
		out.at[kc_index_map[kc],str(opp)] = errors.mean()

		# print(name,g)
	out.to_csv(output,sep='\t',header=True,index=False,float_format='%.6f')
	# out = 
	# pprint(curves)
	print(out)
	# for g in gb:
