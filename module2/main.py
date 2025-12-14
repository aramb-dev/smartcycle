from components import smartcycle_components, lookup, update, add, delete
from error_codes import error_codes


def summarize_inventory():
    print(f"Loaded {len(smartcycle_components)} components.")
    print(f"Loaded {len(error_codes)} error codes.")


def list_components():
    for cid, entry in smartcycle_components.items():
        print(f"{cid}: {entry['name']} (qty {entry['quantity']})")


def list_error_codes():
    for code, info in error_codes.items():
        targets = ", ".join(info["components"])
        print(f"{code}: {info['description']} -> {targets}")


if __name__ == "__main__":
    summarize_inventory()
    print("\nUse lookup/add/update/delete for component operations.")
    print("Use list_error_codes() to review error mappings.")
