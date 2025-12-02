#Crea in python due classi, Product e ShoppingCart, per simularee un carrello della spesa.
# La classe Product deve avere nome e prezzo, con metodi speciali per la stampaa e il confronto.
# La classe ShoppingCart deve permettere di aggiungere, rimuovere e calcolare il totale e stampare il contenuto del carrello.
# Implementa inoltre l'overloading degli operatori + (unione di carrelli), len() e str().
#Scrivi un programma che crei alcuni prodotti, li inserisca in due carrelli diversi e mostri le funzionalità richieste.

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price
    

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def total(self):
        return sum(product.price for product in self.products)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        if not self.products:
            return "Carrello vuoto"
        lines = []
        for product in self.products:
            lines.append(f" - {product}")
        lines.append(f"Totale: ${self.total():.2f}")
        return "\n".join(lines)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.products = self.products + other.products
        return new_cart
    
# Esempio di utilizzo
p1 = Product("Mela", 0.99)
p2 = Product("Banana", 0.59)
p3 = Product("Arancia", 0.79)

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_product(p1)
cart1.add_product(p2)
cart2.add_product(p3)

print("Carrello 1:")
print(cart1)
print(f"Numero di prodotti: {len(cart1)}\n")

print("Carrello 2:")
print(cart2)
print(f"Numero di prodotti: {len(cart2)}\n")

combined_cart = cart1 + cart2
print("Carrello Combinato:")
print(combined_cart)
print(f"Numero di prodotti: {len(combined_cart)}")

cart1.remove_product(p1)
print("\nCarrello 1 dopo la rimozione di un prodotto:")
print(cart1)

print(f"Numero di prodotti: {len(combined_cart)}")