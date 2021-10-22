#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:37:53 2021

@author: ece
"""

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group in group_dictionary:
		# Now go through the users in the group
		for user in group_dictionary[group]:
			if user in user_groups:
				val=user_groups[user]
				val.append(group)
				user_groups[user]=val
			else:
				user_groups[user]=[group]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
