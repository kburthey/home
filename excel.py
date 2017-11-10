for i in range(1,10):
	try:
		sheet = work.get_sheet_by_name('Sheet1')
		if (sheet['B'+ str(i)].value) != 'Apples' and (sheet['B'+ str(i)].value) != 'None':
			print (sheet['B'+ str(i)].value + ' ' + str(sheet['C'+ str(i)].value))
	except TypeError:
		break
