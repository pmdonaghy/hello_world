
# Customer Record
customerNumber = []
global customerName: []
global customerAddress = []

# Package Record
global packageNumber = []
global packageHeight = []
global packageWidth = []
global packageLength = []
global packageWeight = []

# Consignment Record
global consignmentNumber = []
global packageNumberFK = []
global customerNumberFK = []

def menu():
    open = True
    while open:
        print('Pacel Force Menu\n')
        print('Press 1 to add a new customer')
        print('Press 2 to check a packge')
        print('Press 3 to send just one package')
        print('Press 4 to send a consignment of packages')
        print('Press 5 to quit \n')
        anyInput = input("What would you like to do 1..5")
        if anyInput = '1':
            getCustomerDetails()
        elif anyInput = '2':
            checkPackage()
        elif anyInput = '3':
            sendOne()
        elif anyInput = '4':
            sendConsignment()
        elif anyInput = '5':
            open = False
            
    def testFunction():
        print('This is a test')
        anyNumber = input('What is the test number?')
        print('the number is ', anyNumber)

def checkPackage():
    print('Package Checker')
    try:
        anyHeight = int(input('What is the height of the package?'))
    except:
        print('Please enter a number between 1 and 80')
    try:
        anyWidth = int(input('What is the height of the package?'))
    except:
        print('Please enter a number between 1 and 80')
    try:
        anyLength = int(input('What is the height of the package?'))
    except:
        print('Please enter a number between 1 and 80')
    try:
        anyWeight = int(input('What is the height of the package?'))
    except:
        print('Please enter a number between 1 and 80')

    
        
def getCustomerDetails():
    print('Adding a new customer to the database \n')
    anyNumber = int(input("What is the customer number? "))
    anyName = input("What is the Full Name ")
    anyAddress = input("What is the full addresss ")
    customerNumber.append(anyNumber)
    customerName.append(anyName)
    customerAddress.append(anyAddress)
    print('\n')
    print('Thank you, a new record has been added for customer ', anyNumber)
    customerNumber.append(anyNumber)
    customerName.append(anyName)
    customerAddress.append(anyAddress)



menu()
