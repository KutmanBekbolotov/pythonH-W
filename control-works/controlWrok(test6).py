price = int(input("Enter the price: 2500, 5000, 500: "))

price_to_item = {
    
    2500: "стол",
    5000: "кровать",
    500: "табурет"
}


if price in price_to_item:

    item_name = price_to_item[price]
    print(f"Назавние предмета: {item_name}")
else:
    print("Ошибка")