import getpass
import telnetlib
import datetime
import os.path
import router_excel_list

routers = router_excel_list.routers

now = datetime.datetime.now()

save_path = 'C:/Users/adraper/'

for router in routers:
	working_router = router
	print "Saving config from: " + working_router
	HOST = working_router
	user = raw_input('Enter your remote account: ')
	password = getpass.getpass()

	tn = telnetlib.Telnet(HOST)

	tn.read_until('Username: ')
	tn.write(user + '\r')

	tn.read_until('Password: ')
	tn.write(password + '\r')

	tn.read_until('#')

	tn.write('terminal length 0\r')
	tn.write('sh run\r')
	tn.write('exit\r')

	output = tn.read_all()


	hostname = output.splitlines()[1].split('#')[0]

	config = output.splitlines()[4:-2]
	config = '\n'.join(config)

	filename = '%s_backup_%s-%s-%s.txt' % (hostname, now.day, now.month, now.year)
	complete_name = os.path.join(save_path, filename)
	file = open(complete_name, 'w')
	file.write(config)
	file.close()








