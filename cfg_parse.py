#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

#Program Being Developed to Parse Cisco Configs
#In Progess
config=""
options = ""
def choices(options,config):

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
    cfg_obj_net_nat = cfg_parse.find_objects_w_child(parentspec=r"object network",childspec=r"nat")
    cfg_obj_net_host = cfg_parse.find_objects_w_child(parentspec=r"object network",childspec=r"host")
    options = ""
    sa_pol = [] # Security Association List for Children of Policy Config
    obj_net = []

    options = raw_input("""
1. Access Control Lists
2. Local Users
3. NAT Outside Object Config
4. NAT Inside Object Config
4. Crypto Map
5. ikev1 transform-set
6. ikev2 ipsec-proposal
7. ikev1 policy
8. ikev2 policy
9. Routes
10. Serial Number
11. New Config to Parse
12. Quit

Please Select an Option:""")

    if options == "1":
        print "ACL Config\n"
        for line in cfg_acl:
            print line.text
        choices(options,config)
    elif options == "2":
        print "Local Users\n"
        for line in cfg_users:
             print line.text
        choices(options,config)
    elif options == "3":
        print "NAT Config\n"
        for line in cfg_nat:
             print line.text
        choices(options,config)
    elif options == "4":
        print "NAT Config\n"
        for line in cfg_obj_net_nat:
            obj_net = line
            print line.text
            for i in obj_net.all_children:
                print i.text
        choices(options,config)
    elif options == "12":
        print "Crypto Map\n"
        for line in cfg_cm:
             print line.text
        choices(options,config)
    elif options == "5":
        print "ikev1 transform-set\n"
        for line in cfg_ikev1:
            print line.text
        choices(options,config)
    elif options == "6":
        print "ikev2 ipsec-proposal\n"
        for line in cfg_ikev2:
            print line.text
        choices(options,config)
    elif options == "7":
        print "ikev1 Policy\n"
        for line in cfg_ikev1_pol:
            sa_pol = line
            print line.text
            for i in sa_pol.all_children:
                print i.text
        choices(options,config)
    elif options == "8":
        print "ikev2 Policy\n"
        for line in cfg_ikev2_pol:
            sa_pol = line
            print line.text
            for i in sa_pol.all_children:
                print i.text
        choices(options,config)
    elif options == "9":
        print "Routes\n"
        for line in cfg_route:
            print line.text
        choices(options,config)
    elif options == "10":
        print "Serial Number"
        for line in cfg_serial:
             print line.text
        choices(options,config)
    elif options == "11":
        main()
    elif choice == "12":
        quit()
    else:
        print "Pick Another Option"
        choices(options,config)
        
def main():
    config = raw_input("Enter cfg filename: ")
    choices(options,config)

if __name__ == "__main__":
    main()
