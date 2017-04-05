from ciscoconfparse import CiscoConfParse

#Program Being Developed to Parse Cisco Configs
#In Progess

config = raw_input("Enter cfg filename: ")
     

cfg_parse = CiscoConfParse(config)

cfg_acl = cfg_parse.find_objects(r"^access")
cfg_users = cfg_parse.find_objects(r"^user")
cfg_nat = cfg_parse.find_objects(r"^nat")
cfg_cm = cfg_parse.find_objects(r"^crypto map")
cfg_route = cfg_parse.find_objects(r"route ")
cfg_serial = cfg_parse.find_objects(r"^Serial Number:")
options = ""
def choices(options):
     options = raw_input("""
1. Access Control Lists
2. Local Users
3. NAT Config
4. Crypto Map
5. Routes
6. Serial Number
10. Quit

Please Select an Option:""")

     if options == "1":
          print "ACL Config"
          for line in cfg_acl:
               print line.text
          choices(options)
     elif options == "2":
          print "Local Users"
          for line in cfg_users:
               print line.text
          choices(options)
     elif options == "3":
          print "NAT Config"
          for line in cfg_nat:
               print line.text
          choices(options)
     elif options =="4":
          print "Crypto Map"
          for line in cfg_cm:
               print line.text
          choices(options)
     elif options == "5":
          print "Routes"
          for line in cfg_route:
               print line.text
          choices(options)
     elif options == "6":
          print "Serial Number"
          for line in cfg_serial:
               print line.text
          choices(options)
     elif options == "10":
          exit()
     else:
          print "Pick Another Option"
          choices(options)

choices(options)
