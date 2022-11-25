import json #we need this library to read json files
import psycopg2 #we need this library to communicate with PostgreSQL

jsonfile = open('configClear_v2.json','r') #it opens the file in reading mode!
mydata = jsonfile.read() #it reads the file

object = json.loads(mydata) #it parse the data
uniconfig = object['frinx-uniconfig-topology:configuration'] #gets uniconfig data
Cisco_ios_xe = uniconfig['Cisco-IOS-XE-native:native'] # gets Cisco_ios_xe data
interfaces = Cisco_ios_xe['interface'] # gets interfaces

Port_channel = interfaces['Port-channel'] # go to Port Channel
TenGigabitEthernet = interfaces['TenGigabitEthernet'] # go to TenGigabitEthernet
GigabitEthernet = interfaces['GigabitEthernet']# go to GigabitEthernet

first_interface_port_channel = Port_channel[0] # go to first interface
second_interface_port_channel = Port_channel[1]# go to second interface

if "Cisco-IOS-XE-ethernet:channel-group" in first_interface_port_channel: #checks if channel group exist
    port_channel_channel_group_1 = first_interface_port_channel['Cisco-IOS-XE-ethernet:channel-group']
    port_channel_channel_id_1 = port_channel_channel_group_1['number'] # if it exists, get the number
else:
    port_channel_channel_id_1 = None # if not, write None

if "description" in first_interface_port_channel: #checks if description exist
    port_channel_description_1 = first_interface_port_channel['description'] # if yes, get this description
else:
    port_channel_description_1 = "description doesn't exist" # if not, write description doesn't exist

if "mtu" in first_interface_port_channel: #checks if mtu exist
    port_channel_mtu_1 = first_interface_port_channel['mtu'] # if yes, get this value
else:
    port_channel_mtu_1 = None # if not, assign this value as None


if "Cisco-IOS-XE-ethernet:channel-group" in second_interface_port_channel:
    port_channel_channel_group_2 = second_interface_port_channel['Cisco-IOS-XE-ethernet:channel-group']
    port_channel_channel_id_2 = port_channel_channel_group_2['number']
else:
    port_channel_channel_id_2 = None

if "description" in second_interface_port_channel:
    port_channel_description_2 = second_interface_port_channel['description']
else:
    port_channel_description_2 = "description doesn't exist"

if "mtu" in second_interface_port_channel:
    port_channel_mtu_2 = second_interface_port_channel['mtu']
else:
    port_channel_mtu_2 = None


first_interface_TenGigabitEthernet = TenGigabitEthernet[0] # go to first interface
second_interface_TenGigabitEthernet = TenGigabitEthernet[1] # go to second interface
third_interface_TenGigabitEthernet = TenGigabitEthernet[2] # go to third interface
fourth_interface_TenGigabitEthernet = TenGigabitEthernet[3] # go to last interface

if "Cisco-IOS-XE-ethernet:channel-group" in first_interface_TenGigabitEthernet:
    TenGigabitEthernet_channel_group_1 = first_interface_TenGigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    TenGigabitEthernet_channel_id_1 = TenGigabitEthernet_channel_group_1['number']
else:
    TenGigabitEthernet_channel_id_1 = None

if "description" in first_interface_TenGigabitEthernet:
    TenGigabitEthernet_description_1 = first_interface_TenGigabitEthernet['description']
else:
    TenGigabitEthernet_description_1 = "description doesn't exist"

if "mtu" in first_interface_TenGigabitEthernet:
    TenGigabitEthernet_mtu_1 = first_interface_TenGigabitEthernet['mtu']
else:
    TenGigabitEthernet_mtu_1 = None



if "Cisco-IOS-XE-ethernet:channel-group" in second_interface_TenGigabitEthernet:
    TenGigabitEthernet_channel_group_2 = second_interface_TenGigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    TenGigabitEthernet_channel_id_2 = TenGigabitEthernet_channel_group_2['number']
else:
    TenGigabitEthernet_channel_id_2 = None

if "description" in second_interface_TenGigabitEthernet:
    TenGigabitEthernet_description_2 = second_interface_TenGigabitEthernet['description']
else:
    TenGigabitEthernet_description_2 = "description doesn't exist"

if "mtu" in second_interface_TenGigabitEthernet:
    TenGigabitEthernet_mtu_2 = second_interface_TenGigabitEthernet['mtu']
else:
    TenGigabitEthernet_mtu_2 = None


if "Cisco-IOS-XE-ethernet:channel-group" in third_interface_TenGigabitEthernet:
    TenGigabitEthernet_channel_group_3 = third_interface_TenGigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    TenGigabitEthernet_channel_id_3 = TenGigabitEthernet_channel_group_3['number']
else:
    TenGigabitEthernet_channel_id_3 = None

if "description" in third_interface_TenGigabitEthernet:
    TenGigabitEthernet_description_3 = third_interface_TenGigabitEthernet['description']
else:
    TenGigabitEthernet_description_3 = "description doesn't exist"

if "mtu" in third_interface_TenGigabitEthernet:
    TenGigabitEthernet_mtu_3 = third_interface_TenGigabitEthernet['mtu']
else:
    TenGigabitEthernet_mtu_3 = None


if "Cisco-IOS-XE-ethernet:channel-group" in fourth_interface_TenGigabitEthernet:
    TenGigabitEthernet_channel_group_4 = fourth_interface_TenGigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    TenGigabitEthernet_channel_id_4 = TenGigabitEthernet_channel_group_4['number']
else:
    TenGigabitEthernet_channel_id_4 = None

if "description" in fourth_interface_TenGigabitEthernet:
    TenGigabitEthernet_description_4 = fourth_interface_TenGigabitEthernet['description']
else:
    TenGigabitEthernet_description_4 = "description doesn't exist"

if "mtu" in fourth_interface_TenGigabitEthernet:
    TenGigabitEthernet_mtu_4 = fourth_interface_TenGigabitEthernet['mtu']
else:
    TenGigabitEthernet_mtu_4 = None

first_interface_GigabitEthernet = GigabitEthernet[0] # go to first interface
second_interface_GigabitEthernet = GigabitEthernet[1] # go to second interface
third_interface_GigabitEthernet = GigabitEthernet[2] # go to third interface

if "Cisco-IOS-XE-ethernet:channel-group" in first_interface_GigabitEthernet:
    GigabitEthernet_channel_group_1 = first_interface_GigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    GigabitEthernet_channel_id_1 = GigabitEthernet_channel_group_1['number']
else:
    GigabitEthernet_channel_id_1 = None

if "description" in first_interface_GigabitEthernet:
    GigabitEthernet_description_1 = first_interface_GigabitEthernet['description']
else:
    GigabitEthernet_description_1 = "description doesn't exist"

if "mtu" in first_interface_GigabitEthernet:
    GigabitEthernet_mtu_1 = first_interface_GigabitEthernet['mtu']
else:
    GigabitEthernet_mtu_1 = None


if "Cisco-IOS-XE-ethernet:channel-group" in second_interface_GigabitEthernet:
    GigabitEthernet_channel_group_2 = second_interface_GigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    GigabitEthernet_channel_id_2 = GigabitEthernet_channel_group_2['number']
else:
    GigabitEthernet_channel_id_2 = None

if "description" in second_interface_GigabitEthernet:
    GigabitEthernet_description_2 = second_interface_GigabitEthernet['description']
else:
    GigabitEthernet_description_2 = "description doesn't exist"

if "mtu" in second_interface_GigabitEthernet:
    GigabitEthernet_mtu_2 = second_interface_GigabitEthernet['mtu']
else:
    GigabitEthernet_mtu_2 = None



if "Cisco-IOS-XE-ethernet:channel-group" in third_interface_GigabitEthernet:
    GigabitEthernet_channel_group_3 = third_interface_GigabitEthernet['Cisco-IOS-XE-ethernet:channel-group']
    GigabitEthernet_channel_id_3 = GigabitEthernet_channel_group_3['number']
else:
    GigabitEthernet_channel_id_3 = None

if "description" in third_interface_GigabitEthernet:
    GigabitEthernet_description_3 = third_interface_GigabitEthernet['description']
else:
    GigabitEthernet_description_3 = "description doesn't exist"

if "mtu" in third_interface_GigabitEthernet:
    GigabitEthernet_mtu_3 = third_interface_GigabitEthernet['mtu']
else:
    GigabitEthernet_mtu_3 = None

x = "Port-channel" # we need this to write name column
y = "TenGigabitEthernet" 
z = "GigabitEthernet"

#database connection credentials. Please change these with yours to test the program properly!
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'yucelb27'
port_id = '5432'
connect = None
cursor = None

try: # firstly, system needs to try connection and if it fails, it has to write the error to fix!
    connect = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cursor = connect.cursor() # cursor enable us to write SQL commands from python interface
    create_script = '''CREATE TABLE IF NOT EXISTS interfaces(
        id SERIAL PRIMARY KEY,
    	connection INTEGER,
    	name VARCHAR(255) NOT NULL,
    	description VARCHAR(255),
    	config json,
    	type VARCHAR(50),
    	infra_type VARCHAR(50),
    	port_channel_id INTEGER,
    	max_frame_size INTEGER)'''
    cursor.execute(create_script) # execute : it runs the command we wrote 
    insert_script = 'INSERT INTO interfaces (connection,name,description,config,type,infra_type,port_channel_id,max_frame_size) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    insert_value1 = (None,x + str(first_interface_port_channel['name']),port_channel_description_1,json.dumps(first_interface_port_channel),None , None,port_channel_channel_id_1,port_channel_mtu_1)
    insert_value2 = (None,x + str(second_interface_port_channel['name']),port_channel_description_2,json.dumps(second_interface_port_channel),None , None,port_channel_channel_id_2,port_channel_mtu_2)
    insert_value3 = (None,y + str(first_interface_TenGigabitEthernet['name']),TenGigabitEthernet_description_1,json.dumps(first_interface_TenGigabitEthernet),None , None,TenGigabitEthernet_channel_id_1,TenGigabitEthernet_mtu_1)
    insert_value4 = (None,y + str(second_interface_TenGigabitEthernet['name']),TenGigabitEthernet_description_2,json.dumps(second_interface_TenGigabitEthernet),None , None,TenGigabitEthernet_channel_id_2,TenGigabitEthernet_mtu_2)
    insert_value5 = (None,y + str(third_interface_TenGigabitEthernet['name']),TenGigabitEthernet_description_3,json.dumps(third_interface_TenGigabitEthernet),None , None,TenGigabitEthernet_channel_id_3,TenGigabitEthernet_mtu_3)
    insert_value6 = (None,y + str(fourth_interface_TenGigabitEthernet['name']),TenGigabitEthernet_description_4,json.dumps(fourth_interface_TenGigabitEthernet),None , None,TenGigabitEthernet_channel_id_4,TenGigabitEthernet_mtu_4)
    insert_value7 = (None,z + str(first_interface_GigabitEthernet['name']),GigabitEthernet_description_1,json.dumps(first_interface_GigabitEthernet),None , None,GigabitEthernet_channel_id_1,GigabitEthernet_mtu_1)
    insert_value8 = (None,z + str(second_interface_GigabitEthernet['name']),GigabitEthernet_description_2,json.dumps(second_interface_GigabitEthernet),None , None,GigabitEthernet_channel_id_2,GigabitEthernet_mtu_2)
    insert_value9 = (None,z + str(third_interface_GigabitEthernet['name']),GigabitEthernet_description_3,json.dumps(third_interface_GigabitEthernet),None , None,GigabitEthernet_channel_id_3,GigabitEthernet_mtu_3)
    cursor.execute(insert_script,insert_value1)
    cursor.execute(insert_script,insert_value2)
    cursor.execute(insert_script,insert_value3)
    cursor.execute(insert_script,insert_value4)
    cursor.execute(insert_script,insert_value5)
    cursor.execute(insert_script,insert_value6)
    cursor.execute(insert_script,insert_value7)
    cursor.execute(insert_script,insert_value8)
    cursor.execute(insert_script,insert_value9)
    connect.commit() # we need to commit changes to see them in database
    print("Data has been inserted successfully!")

except Exception as error: # if system can not connect the database
    print(error) # it will print the error!
finally:
    if cursor is not None: # if cursor run successfully
        cursor.close() # it closes the cursor
    if connect is not None: # if connect function run successfully
        connect.close() # it closes connect function

