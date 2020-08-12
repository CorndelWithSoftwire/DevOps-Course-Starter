expected_result = [{'id': 1, 'status': 'Not Started', 'title': 'test 2'}, {'id': 2, 'status': 'Not Started', 'title': '1'}, {'id': 3, 'status': 'Not Started', 'title': '2'}, {'id': 4, 'status': 'Not Started', 'title': '2'}, {'id': 5, 'status': 'Not Started', 'title': '3'}]

def get_existing_items():
	return [{'id': 1, 'status': 'Not Started', 'title': 'test 1'}, {'id': 1, 'status': 'Not Started', 'title': 'test 2'}, {'id': 2, 'status': 'Not Started', 'title': '1'}, {'id': 3, 'status': 'Not Started', 'title': '2'}, {'id': 4, 'status': 'Not Started', 'title': '2'}, {'id': 5, 'status': 'Not Started', 'title': '3'}]

item_id = 0


print ("Method 1")
new_items=[]
for item in get_existing_items():
	if item.get('id') != item_id:
		new_items.append(item)

print ("=========Result 1")
print (new_items)
assert new_items == expected_result


print ("Method 2")
todo_list = get_existing_items()
for item in todo_list:
	if item.get('id') == item_id:
		todo_list.remove(item)
		break
print ("=========Result 2")
print (todo_list)
assert todo_list == expected_result


print ("Method 3")
result = [ items for items in get_existing_items() if items.get('id') != item_id ]
print ("Result 3")
print (result)
assert result == expected_result


