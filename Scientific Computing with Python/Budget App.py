class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -1 * amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self):
        objects = (self.name.center(30, "*") + "\n")
        for entry in self.ledger:
            objects = objects + f"{entry['description'][0:23].ljust(23)}{format(entry['amount'], '.2f').rjust(7)}\n"
        objects = objects + f"Total: {format(self.get_balance(), '.2f')}"
        return objects

    def total_withdrawn(self):
        subtotal = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                subtotal += entry["amount"]
        return subtotal


def create_spend_chart(categories):
    bar_chart = "Percentage spent by category\n"
    total = 0
    subtotals = {}
    percentages = {}
    name_length = 0

    for category in categories:
        subtotal = category.total_withdrawn()
        subtotals[category.name] = subtotal
        total = total + subtotal

    for name, subtotal in subtotals.items():
        percent = subtotal / total * 100
        percent = percent - (percent % 10)
        percentages[name] = percent

    x = 100
    for number in range(11):
        bar_row = f"{x}".rjust(3) + "| "
        for name, percent in percentages.items():
            if percent >= x:
                bar_row += "o  "
            else:
                bar_row += "   "
        bar_chart += bar_row + '\n'
        x -= 10

    x_axis = "    -"
    for _ in categories:
        x_axis += "---"
    bar_chart += x_axis + "\n"

    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)

    y = 0
    while y <= name_length:
        row = "     "
        for key, value in percentages.items():
            category_name = key
            try:
                row += category_name[y] + "  "
            except :
                row += "   "

        if y <= name_length - 1:
            bar_chart += row + '\n'
        else:
            bar_chart += row.strip(" ")

        y = y + 1
    bar_chart = bar_chart.rstrip("\n")
    return bar_chart
