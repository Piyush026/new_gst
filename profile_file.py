import re

"""
ui = ['08AAACH1004N2ZT', '32AAACH1004N2Z2', '37AAACH1004N1ZT', '18AAACH1004N2ZS', '07AAACH1004N1ZW', '27AAACH1004N3ZS',
      '30AAACH1004N1Z7', '08AAACH1004N1ZU', '19AAACH1004N2ZQ', '33AAACH1004N2Z0', '04AAACH1004N1Z2', '09AAACH1004N2ZR',
      '20AAACH1004N1Z8', '29AAACH1004N2ZP', '25AAACH1004N1ZY', '18AAACH1004N4ZQ', '24AAACH1004N1Z0', '27AAACH1004N2ZT',
      '36AAACH1004N2ZU', '02AAACH1004N1Z6', '18AAACH1004N1ZT', '03AAACH1004N2Z3', '26AAACH1004N1ZW', '21AAACH1004N1Z6',
      '27AAACH1004N1ZU', '19AAACH1004N1ZR', '06AAACH1004N2ZX', '03AAACH1004N1Z4', '24AAACH1004N2ZZ', '34AAACH1004N1ZZ',
      '01AAACH1004N1Z8', '20AAACH1004N2Z7', '10AAACH1004N2Z8', '21AAACH1004N2Z5', '18AAACH1004N5ZP', '10AAACH1004N1Z9',
      '02AAACH1004N3Z4', '05AAACH1004N1Z0', '32AAACH1004N1Z3', '22AAACH1004N1Z4', '36AAACH1004N1ZV', '23AAACH1004N1Z2',
      '22AAACH1004N2Z3', '06AAACH1004N1ZY', '33AAACH1004N1Z1', '18AAACH1004N3ZR', '02AAACH1004N2Z5', '35AAACH1004N1ZX',
      '09AAACH1004N1ZS', '26AAACH1004N2ZV', '29AAACH1004N1ZQ', '37AAACH1004N2ZS', '37AAACH1004N3ZR', '23AAACH1004N2Z1']
print(len(ui))
ci = ['', '', '', 'Legal Name of Business', 'PARTHA  MUKHOPADHYAY', '', '', 'Trade Name', 'SENTEX,M/S GALAXY HONDA', '',
      '', 'Effective Date of registration', '01/07/2017', '', '', '']
fi = ['', '', '', 'Administrative Office', '', '', '                                       (JURISDICTION - CENTER)',
      '                                       Commisionerate - KOLKATA-NORTH',
      '                                       Division - KALYANI - NADIA DIVISION',
      '                                       Range - RANGE-IV ', '', '', '', 'Other Office', '', '',
      '                                       (JURISDICTION - STATE)',
      '                                       Commisionerate - West Bengal',
      '                                       Circle - BAHARAMPUR',
      '                                       Charge - KRISHNANAGAR', '', '', '', 'Principal Place of Business',
      '4, MAITRA PARA LANE, SANTIPUR, Nadia, West Bengal, 741404', '', '', '']
"""


def profile_list(ci, fi):
    address_list = [i.strip() for i in fi if i]
    ad_office = address_list.index('Administrative Office')
    other_office = address_list.index('Other Office')
    principal_place = address_list.index('Principal Place of Business')
    name_list = [i.strip() for i in ci if i]
    l_name = name_list.index('Legal Name of Business')
    t_name = name_list.index('Trade Name')
    date = name_list.index('Effective Date of registration')

    profile = {'Legal Name of Business': " ".join(name_list[l_name + 1:t_name]),
               'Trade Name': " ".join(name_list[t_name + 1:date]),
               'date': " ".join(name_list[date + 1:]),
               "Administrative Office": " ".join(address_list[ad_office + 1:other_office]),
               "Other Office": " ".join(address_list[other_office + 1:principal_place]),
               "Principal Place of Business": " ".join(address_list[principal_place + 1:])}
    return profile
