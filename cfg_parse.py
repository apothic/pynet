from ciscoconfparse import CiscoConfParse

#Program Being Developed to Parse Cisco Configs
#In Progess

config = raw_input("Enter cfg filename: ")
     

cfg_parse = CiscoConfParse(config)

cfg_acl = cfg_parse.find_objects(r"^access")
cfg_users = cfg_parse.find_objects(r"^user")
cfg_nat = cfg_parse.find_objects(r"^nat")
cfg_cm = cfg_parse.find_objects(r"^crypto map")
cfg_ikev1 = cfg_parse.find_objects(r"set ikev1 transform-set")
cfg_ikev2 = cfg_parse.find_objects(r"set ikev2 ipsec-proposal")
cfg_ikev1_pol = cfg_parse.find_objects(r"crypto ikev1 policy")
cfg_ikev2_pol = cfg_parse.find_objects(r"crypto ikev2 policy")
cfg_route = cfg_parse.find_objects(r"route ")
cfg_serial = cfg_parse.find_objects(r"Serial Number:")
options = ""
sa_pol = [] # Security Association List for Children of Policy Config
def choices(options):
    options = raw_input("""
1. Access Control Lists
2. Local Users
3. NAT Config
4. Crypto Map
5. ikev1 transform-set
6. ikev2 ipsec-proposal
7. ikev1 policy
8. ikev2 policy
9. Routes
10. Serial Number
11. Quit

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
    elif options == "7":
        print "ikev1 Policy\n"
        for line in cfg_ikev1_pol:
            sa_pol = line
            print line.text
            for i in sa_pol.all_children:
                print i.text
        choices(options)
    elif options == "8":
        print "ikev2 Policy\n"
        for line in cfg_ikev2_pol:
            sa_pol = line
            print line.text
            for i in sa_pol.all_children:
                print i.text
        choices(options)
    elif options == "9":
        print "Routes"
        for line in cfg_route:
            print line.text
        choices(options)
    elif options == "10":
        print "Serial Number"
        for line in cfg_serial:
             print line.text
        choices(options)
    elif options == "11":
        exit()
    else:
        print "Pick Another Option"
        choices(options)

choices(options)
