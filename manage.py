import click
from cli.inventory_cli import inventory
from cli.supplier_cli import supplier
from cli.order_cli import order

@click.group()
def cli():
    """Retail Inventory Management System"""
    pass

# Register the inventory, supplier, and order command groups
cli.add_command(inventory)
cli.add_command(supplier)
cli.add_command(order)

if __name__ == "__main__":
    cli()
