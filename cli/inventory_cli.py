import click
from db.database import get_db
from models.inventory import Inventory
from models.supplier import Supplier

@click.group()
def inventory():
    """Inventory management commands"""
    pass

@inventory.command("add")
@click.argument('name')
@click.argument('stock_level', type=int)  # Ensure stock_level is an integer
@click.argument('price', type=float)      # Ensure price is a float
@click.argument('supplier_name')
def add_product(name, stock_level, price, supplier_name):
    """Add a new product to the inventory"""
    db = next(get_db())  # Get the database session
    
    # Find the supplier by name
    supplier = db.query(Supplier).filter_by(name=supplier_name).first()
    
    if not supplier:
        click.echo(f"Supplier '{supplier_name}' not found.")
        return
    
    # Create new product
    new_product = Inventory(name=name, stock_level=stock_level, price=price, supplier_id=supplier.id)
    db.add(new_product)
    
    # Commit the changes to the database
    try:
        db.commit()
        click.echo(f"Product '{name}' added to inventory.")
    except Exception as e:
        db.rollback()  # Rollback in case of any error
        click.echo(f"Error adding product: {str(e)}")

@inventory.command("list")
def list_products():
    """List all products in the inventory"""
    db = next(get_db())  # Get the database session
    products = db.query(Inventory).all()

    if products:
        # Just show the number of products
        click.echo(f"Found {len(products)} products in the inventory.")
    else:
        click.echo("No products in the inventory.")

@inventory.command("update-stock")
@click.argument('product_name')
@click.argument('new_stock', type=int)  # Ensure new_stock is an integer
def update_stock(product_name, new_stock):
    """Update the stock level of a product"""
    db = next(get_db())  # Get the database session
    
    # Find the product by name
    product = db.query(Inventory).filter_by(name=product_name).first()

    if product:
        product.stock_level = new_stock  # Update stock level
        
        try:
            db.commit()  # Commit the changes
            click.echo(f"Stock level of '{product_name}' updated to {new_stock}.")
        except Exception as e:
            db.rollback()  # Rollback in case of any error
            click.echo(f"Error updating stock: {str(e)}")
    else:
        click.echo(f"Product '{product_name}' not found.")
