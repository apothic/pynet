from ciscoconfparse import CiscoConfParse



mohc_parse = CiscoConfParse("MOHC-FW01.txt")
sra_parse = CiscoConfParse("SRA_ASA.txt")
efin_parse = CiscoConfParse("EFIN.txt")

mohc_acl = mohc_parse.find_objects(r"^access")
sra_acl = sra_parse.find_objects(r"^access")
efin_acl = efin_parse.find_objects(r"^access")

print "mohc"
for line in mohc_acl:
     print line

print "sra"
for line in sra_acl:
     print line

print "efin"
#for line in efin_acl:
     #print line

