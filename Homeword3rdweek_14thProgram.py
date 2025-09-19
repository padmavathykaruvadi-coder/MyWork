class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

payments = [CreditCardPayment(), PayPalPayment(), BankTransferPayment()]
amounts = [100, 200, 300]

for p, a in zip(payments, amounts):
    make_payment(p, a)