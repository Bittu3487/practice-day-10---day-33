class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name , price , quantity):
        assert price >=0 , f"price is {price} not equal to and greater then 0"
        assert quantity >=0, f"quantity is {quantity} not equal to and greater then 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calc(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price*self.pay_rate
    def __repr__(self):
        return f"item({self.name} , {self.price} , {self.quantity})"
item1 = Item("mobile phone" , 500 , 6)
item2 = Item("laptop" , 3000 , 7)
item3 = Item("mouse" , 75 , 5)
item4 = Item("keyboard" , 125 , 8)
item5 = Item("pendrive" , 200 , 4)
print(Item.all)