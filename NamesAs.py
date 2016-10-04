#Part I:
thelog = {
 'students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]}

for key, data in thelog.items():
	for value in data:
		fullname = value["first_name"] + " " + value["last_name"]
		uppercasenames = fullname.upper()
		print "%s" %(uppercasenames)

#Part II:
thelog = {
 'students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }

for key, data in thelog.items():
	print "\n%s" %key.title()
	count = 0

	for value in data:
		count = count +1
		fullname = value["first_name"] + " " + value["last_name"]
		uppercasenames = fullname.upper()
		namelength = len(value["first_name"]) + len(value["last_name"])
		
		print "%d - %s - %d" %(count, uppercasenames, namelength)