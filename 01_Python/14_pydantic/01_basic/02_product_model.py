from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


# Example usage
if __name__ == "__main__":

    product1 = Product(id=1, name="Laptop", price=999.99)
    product2 = Product(id=2, name="Smartphone", price=499.49, in_stock=True)
    product3 = Product(id=3, name="mouse", price=19.99, in_stock=False)
    
    print(product1)
    print(product2)
    print(product3)