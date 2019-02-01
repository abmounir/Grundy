def Grundy(dict_succ):
	sommets=list(reversed(sorted(dict_succ.keys())))
	g_dict={}
	g_list=[]
	for k in sommets:
		g_list=[]
		l=[]
		tmp_dic={}
		if len(dict_succ[k])==0 :
			g=0
			l.append(k)
			tmp_dic[g]=l
			if g in g_dict :
				if not isinstance(g_dict[g],list) :
					ls=list(g_dict[g])
				else:
					ls=g_dict[g]
				ls+=l
				g_dict[g]=ls
			else:
				g_dict[g]=l			
							
		elif len(dict_succ[k])>=1 :
			j=10000
			g_list=[j+x for x in range(1000)]
	
			jj=j+(1000)
			ind=0
			for i in dict_succ[k] :
				for m in g_dict:
					for n in g_dict[m] :
						if n==i:
							ind=m
				g_list[ind]=jj
				jj+=1
			#print(g_list)		
			min_list=min(g_list)
			g=g_list.index(min_list)
			l.append(k)
			if g in g_dict :
				if not isinstance(g_dict[g],list) :
					ls=list(g_dict[g])
				else:
					ls=g_dict[g]
				ls+=l
				g_dict[g]=ls
			else:
				g_dict[g]=l	


	print(g_dict)
		
	return g_dict					
		
