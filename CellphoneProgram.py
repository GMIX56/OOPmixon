import CellphoneClass as cp

def main():
    phone = cp.CellPhone("Apple", "16", 100)

    phone.set_manufact("Samsung")
    print(phone.get_manufact())
    phone.set_model("100")
    print(phone.get_model())
    phone.set_retail_price(200)
    print(phone.get_retail_price())


main()