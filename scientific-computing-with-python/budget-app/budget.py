import scipy as sp


class Category:
    ledger = []

    def __init__(self, category):
        self.ledger = []
        self.category = category
        pass

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        pass

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        pass

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
        pass

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False
        pass

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
        pass

    def __str__(self):
        title = self.category.center(30, "*")
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = str("{:.2f}".format(item["amount"]))
            amount = amount.rjust(30 - len(description))
            items += description + amount + "\n"
        total = "Total: " + str(self.get_balance())
        return title + "\n" + items + total


# Example:
"""
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g   
"""


def create_spend_chart(categories):
    # Calculate total spent
    spend = []
    for category in categories:
        temp = 0
        for item in category.ledger:
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend.append(temp)

    # Calculate percentage spent
    total = sum(spend)
    percentage = [i/total * 100 for i in spend]

    # Create chart
    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                s += " o "
            else:
                s += "   "
        # Spaces
        s += " "
    s += "\n    ----------"

    # Create labels
    cat_length = []
    for category in categories:
        cat_length.append(len(category.category))
    max_length = max(cat_length)

    # Create chart
    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                s += " " + categories[j].category[i] + " "
            else:
                s += "   "
        # Spaces
        s += " "
    return s
