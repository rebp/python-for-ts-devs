"""Break the import cycle between pricing and inventory.

Move the shared Product dataclass from inventory.py into this module.
Change pricing.py and inventory.py to import it from here. Keep total() and
inventory_value() working, and make both modules importable in either order.
"""
