"""
Customer Management System
"""
from customer import Customer

class CMS:
	def __init__(self):
		# Dictionary to store customer info by ID: k:c_id  v:customer
		self.customer_id_dict = {}
		# Dictionary to store customer info by Name: k:name  v:{k:c_id, v:customer}
		self.customer_name_dict = {}

	def set_customer_id(self):
		customer_id = None
		for i in range(3):
			if i < 2:
				customer_id = input('Please enter customer ID:')
				if Customer.check_id(customer_id):
					break
				else:
					print('ID must be numeric only, please enter carefully.')
			else:
				customer_id = input('Last chance, Please enter carefully:')
				if Customer.check_id(customer_id):
					break
				else:
					print('3 attempts exhausted.Exiting....')
					return False
		
		if customer_id in self.customer_id_dict:
			print('This Customer ID alreadt exists')
			return False
		else:
			return customer_id

	def set_customer_name(self):
		customer_name = None
		for i in range(3):
			if i < 2:
				customer_name = input('Please enter customer name:')
				if Customer.check_name(customer_name):
					break
				else:
					print('Name must contain letters only. Please try again.')
			else:
				customer_name = input('Last chance, please enter carefully:')
				if Customer.check_name(customer_name):
					break
				else:
					print('3 attempts exhausted. Exiting.')
					return False
		
		return customer_name

	def set_customer_age(self):
		cusomer_age = input('Please enter customer age:')
		if Customer.check_age(cusomer_age):
			return cusomer_age
		else:
			print('Invalid age input. Using default value.')
			return "None"

	def set_customer_email(self):
		customer_email = input('Please input customer email:')
		if Customer.check_email(customer_email):
			return customer_email
		else:
			print('Invalid email format. Using default value.')
			return "None"
	
	def set_customer_phone(self):
		customer_phone = input('Please enter customer phone:')
		if Customer.check_phone(customer_phone):
			return customer_phone
		else:
			print('Invalid phone format. Using default value.')
			return "None"

	def add_customer(self):
		if not (customer_id := self.set_customer_id()):
			return
		
		if not (customer_name := self.set_customer_name()):
			return
		
		customer_age = self.set_customer_age()
		customer_email = self.set_customer_email()
		customer_phone = self.set_customer_phone()

		customer = Customer(customer_id, customer_name, customer_age, customer_phone, customer_email)

		self.customer_id_dict[customer_id] = customer

		customer_inner_dict = self.customer_name_dict.get(customer_name)
		if customer_inner_dict is None:
			self.customer_name_dict[customer_name] = {customer_id:customer}
		else:
			customer_inner_dict[customer_id] = customer
		print('Customer added successfully!')

	def delete_customer(self):
		customer_id = input('Please enterthe customer ID to delete:')
		if not Customer.check_id(customer_id):
			print('Invalid ID input')
			return

		if customer_id not in self.customer_id_dict:
			print('Customer ID does not exist')
			return
		
		customer = self.customer_id_dict[customer_id]
		customer_name = customer.name

		inner_dict = self.customer_name_dict[customer_name]
		if len(inner_dict) == 1:
			del self.customer_name_dict[customer_name]
		else:
			del inner_dict[customer_id]

		del self.customer_id_dict[customer_id]

		print('Customer deleted successfully!')

	def update_customer(self):
		customer_id = input('Please enter the customer ID to update:')

		if not Customer.check_id(customer_id):
			print('Invalid ID format.')
			return

		if customer_id not in self.customer_id_dict:
			print('Customer ID does not exist.')
			return

		customer = self.customer_id_dict[customer_id]
		while True:
			print(f'Current Info: {customer}')
			print('which field to upate?')
			print('1. Name 2. Age 3. Phone 4. Email 0. Exit/Done')
			choice = input('Enter choice:')

			match choice:
				case "1":
					new_name = self.set_customer_name()
					if new_name:
						old_name = customer.name
						inner_dict = self.customer_name_dict[old_name]
						if len(inner_dict) == 1:
							del self.customer_name_dict[old_name]
						else:
							del inner_dict[customer_id]

						if new_name in self.customer_name_dict:
							self.customer_name_dict[new_name][customer_id] = customer
						else:
							self.customer_name_dict[new_name] = {customer_id: customer}

						customer.name = new_name
						print('Name updated successfully!')
				
				case "2":
					new_age = self.set_customer_age()
					if new_age:
						customer.age = new_age
						print('Age updated successfuly!')

				case "3":
					new_phone = self.set_customer_phone()
					if new_phone:
						customer.phone = new_phone
						print('Phone updated successfully')

				case "4":
					new_email = self.set_customer_email()
					if new_email:
						customer.email = new_email
						print('Email updated successfuly')
				
				case "0":
					print('Updated completed')
					break

				case _:
					print('Invalid choice.')

	def search_customer(self):
		while True:
			print('Search by 1. ID 2. Name 0. Done/Exit')
			search_type = input('Enter choice:')
			match search_type:
				case "1":
					customer_id = input('Please input the customer ID to search:')
					if not Customer.check_id(customer_id):
						print("Invalid ID format.")
						return
					
					if customer_id not in self.customer_id_dict:
						print('Customer ID does not exist')
						return

					customer = self.customer_id_dict[customer_id]
					print(f'Customer Info: {customer}')

				case "2":
					customer_name = input('Please input the customer name to search:')
					if customer_name not in self.customer_name_dict:
						print('Customer does not exist')
						return
					
					inner_dict = self.customer_name_dict[customer_name]
					for cid, customer in inner_dict.items():
						print(f'Customer Info:{customer}')
				
				case "0":
					print("Search completed")
					break

				case _:
					print('Invalid choice.')

	def display_customer(self):
		"""Display all customers"""
		if len(self.customer_id_dict) == 0:
			print('The system currently has no customers.')
			return
		else:
			for k in self.customer_id_dict.keys():
				print(self.customer_id_dict[k])
	
	def display_menu(self):
		"""Display the Menu"""
		print("""
			~~~~~~~~~~~~~~~~~ Customer Management System ~~~~~~~~~~~~~~~~~~~~~~~
                                    1. Add Customer
                                    2. Delete Customer
                                    3. Modify Customer
                                    4. Search Customer
                                    5. Display All Customers
                                    6. Exit System	
		""")
		
		
	def start(self):
		"""Start the system menu and enter menu loop"""
		while True:
			self.display_menu()
			choice = input('Please enter your choice： ')
			match choice:
				case '1':
					print('Adding Customer...')
					self.add_customer()
				case '2':
					print('Deleting Customer...')
					self.delete_customer()
				case '3':
					print('Modifying Customer...')
					self.update_customer()
				case '4':
					print('Searching Customer...')
					self.search_customer()
				case '5':
					print('Displaying all Customers')
					self.display_customer()
				case '6':
					print('You have successfully exited the system')
					break
				case _:
					print('Invalid input, please try again.')
			


if __name__ == '__main__':
	cms = CMS()
	cms.start()
		 