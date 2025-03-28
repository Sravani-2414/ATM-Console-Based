# ATM-Console-Based
a simple text-based application that mimics the functionality of a real ATM. It allows users to perform basic banking operations such as checking account balance, withdrawing cash, depositing money, and changing their PIN.
# ATM Console Application

# Dictionary to store user details (Example data)
users = {
    '1234': {'pin': '0000', 'balance': 5000, 'transactions': []},
    '5678': {'pin': '1111', 'balance': 3000, 'transactions': []}
}

def authenticate(user_id, pin):
    return user_id in users and users[user_id]['pin'] == pin

def deposit(user_id, amount):
    users[user_id]['balance'] += amount
    users[user_id]['transactions'].append(f'Deposited: {amount}')
    print(f'Amount Deposited: {amount}')

def withdraw(user_id, amount):
    if users[user_id]['balance'] >= amount:
        users[user_id]['balance'] -= amount
        users[user_id]['transactions'].append(f'Withdrawn: {amount}')
        print(f'Amount Withdrawn: {amount}')
    else:
        print('Insufficient Balance!')

def generate_pin(user_id, new_pin):
    users[user_id]['pin'] = new_pin
    print('PIN Updated Successfully!')

def mini_statement(user_id):
    print('Mini Statement:')
    for transaction in users[user_id]['transactions'][-5:]:
        print(transaction)
    print(f'Current Balance: {users[user_id]["balance"]}')

def main():
    user_id = input('Enter User ID: ')
    pin = input('Enter PIN: ')
    
    if authenticate(user_id, pin):
        while True:
            print('\n1. Deposit\n2. Withdraw\n3. Generate PIN\n4. Mini-Statement\n5. Exit')
            choice = input('Enter your choice: ')
            
            if choice == '1':
                amount = float(input('Enter amount to deposit: '))
                deposit(user_id, amount)
            elif choice == '2':
                amount = float(input('Enter amount to withdraw: '))
                withdraw(user_id, amount)
            elif choice == '3':
                new_pin = input('Enter new PIN: ')
                generate_pin(user_id, new_pin)
            elif choice == '4':
                mini_statement(user_id)
            elif choice == '5':
                print('Thank you for using the ATM!')
                break
            else:
                print('Invalid choice! Please try again.')
    else:
        print('Invalid Credentials!')

if __name__ == '__main__':
    main()
