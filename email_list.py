#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:17:52 2021

@author: ece
"""
def email_list(domains):
	emails = []
	for domain in domains:
	  for user in domains[domain]:
	    emails.append( user + '@' + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
