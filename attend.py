import time

#取得原始出勤資料
f1=open('attend.txt','r')
txt=f1.readlines()
f1.close()
print(txt)
#計算出勤狀況
def attendStatus(t,ab_status):
	intime=time.strftime('09:00')
	outtime=time.strftime('18:00')
	
	ipt_time=time.strftime(t)
	 
	if  ipt_time=='' and ab_status=='A':
		return('No Sign-in')
	elif  ipt_time=='' and ab_status=='B':
		return('No Sign-out')
	elif ipt_time>intime and ab_status=='A':
		return('Late')
	elif ipt_time<outtime and ab_status=='B':
		return('Leave early')
	else:
		return('OK')


lst_txt=[]
f2=open('attend.csv','w')

#將原始資料寫入CSV檔案
for i in range(len(txt)):
	txt2=''
	#卡號
	for j in range(0,8,1):
		txt2+=txt[i][j]
	txt2+=','
	
	#年
	for m in range(8,12,1):
		txt2+=txt[i][m]
	txt2+=','
	#月
	for n in range(12,14,1):
		txt2+=txt[i][n]
	txt2+=','
	#日
	for o in range(14,16,1):
		txt2+=txt[i][o]
	txt2+=','
	#時
	for p in range(16,18,1):
		txt2+=txt[i][p]
	txt2+=':'
	#分
	for q in range(18,20,1):
		txt2+=txt[i][q]
	txt2+=','
	
	#簽到 簽退
	for l in range(20,21,1):
		txt2+=txt[i][l]
	txt2+=','
	lst_txt.append(txt2)
	#print(lst_txt[i].split(',')[4])
	#print(txt2)	
	print(lst_txt[i])
	

lst_card=[]
#取得卡號名單list
for r in range(len(lst_txt)):
	lst_card.append(lst_txt[r].split(',')[0])

#取得出勤異常資料：未簽到、未簽退、遲到、早退
for s in range(len(lst_txt)):
	unNormalStatus='OK'
	if lst_card.count(lst_txt[s].split(',')[0])<2:
		unNormalStatus=attendStatus('',lst_txt[s].split(',')[5])
	else:
		unNormalStatus=attendStatus(lst_txt[s].split(',')[4],lst_txt[s].split(',')[5])
	if unNormalStatus!='OK':		
		csv=f2.write(lst_txt[s]+unNormalStatus+'\n')
	else:
		csv=f2.write(lst_txt[s]+''+'\n')

f2.close()
	
