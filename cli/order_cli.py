import click
from db.database import get_db
from models.order import Order
from models.inventory import Inventory
from models.supplier import Supplier
from tabulate import tabulate

@click.group()
def order():
    """Order management commands"""
    pass

@order.command("place")
@click.argument('product_name')
@click.argument('supplier_name')
@click.argument('quantity')
@click.argument('order_date')
def place_order(product_name, supplier_name, quantity, order_date):
    """Place an order to restock inventory"""
    db = next(get_db())
    product = db.query(Inventory).filter_by(name=product_name).first()
    supplier = db.query(Supplier).filter_by(name=supplier_name).first()

    if not product:
        click.echo(f"Product '{product_name}' not found.")
        return
    if not supplier:
        click.echo(f"Supplier '{supplier_name}' not found.")
        return

    new_order = Order(product_id=product.id, supplier_id=supplier.id, quantity=quantity, order_date=order_date)
    db.add(new_order)
    product.stock_level += int(quantity)  # Increase the stock
    db.commit()
    click.echo(f"Order placed for {quantity} units of '{product_name}' from '{supplier_name}'.")

@order.command("list")
def list_orders():
    """List all orders placed"""
    db = next(get_db())
    orders = db.query(Order).all()

    if orders:
        data = [[order.id, order.product.name, order.supplier.name, order.quantity, order.order_date] for order in orders]
        headers = ["Order ID", "Product", "Supplier", "Quantity", "Order Date"]
        click.echo(tabulate(data, headers, tablefmt="grid"))
    else:
        click.echo("No orders found.")
