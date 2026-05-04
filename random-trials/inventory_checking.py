def is_in_stock(product_name: str) -> bool:
   inventory = [
      {"name": "Laptop", "qty": 10},
      {"name": "Mouse", "qty": 5},
      {"name": "Keyboard", "qty": 0}
   ]

   for product in inventory:
      if product["name"] == product_name.lower():
         print(f"product '{product_name}' exits in inventory.")
         #return product["qty"] > 0
      return f"product '{product_name}' does not exit in inventory", False
   #return

product_name = "Mouse"
if __name__ == "__main__":
   print(is_in_stock(product_name))