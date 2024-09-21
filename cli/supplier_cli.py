import click
from db.database import get_db
from models.supplier import Supplier
from tabulate import tabulate

@click.group()
def supplier():
    """Supplier management commands"""
    pass

@supplier.command("add")
@click.argument('name')
@click.argument('contact_info')
def add_supplier(name, contact_info):
    """Add a new supplier"""
    db = next(get_db())
    new_supplier = Supplier(name=name, contact_info=contact_info)
    db.add(new_supplier)
    db.commit()
    click.echo(f"Supplier '{name}' added.")

@supplier.command("list")
def list_suppliers():
    """List all suppliers"""
    db = next(get_db())
    suppliers = db.query(Supplier).all()

    if suppliers:
        data = [[supplier.id, supplier.name, supplier.contact_info] for supplier in suppliers]
        headers = ["ID", "Name", "Contact Info"]
        click.echo(tabulate(data, headers, tablefmt="grid"))
    else:
        click.echo("No suppliers found.")
