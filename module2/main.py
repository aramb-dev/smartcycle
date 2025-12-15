from datetime import datetime
from components import smartcycle_components, lookup, update, add, delete
from error_codes import error_codes

# Activity logs list to store all function calls
activity_logs = []


def log_activity(user_id="system"):
    """Decorator to automatically log function calls to activity_logs."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            action = f"called {func.__name__}"
            timestamp = datetime.now().isoformat()
            activity_logs.append({
                "user_id": user_id,
                "action": action,
                "timestamp": timestamp
            })
            return func(*args, **kwargs)
        return wrapper
    return decorator


def view_recent_logs(n=10):
    """Display the most recent n activity log entries in reverse chronological order."""
    if not activity_logs:
        print("No activity logs found.")
        return
    print(f"\nRecent {min(n, len(activity_logs))} activity logs:")
    for log in activity_logs[-n:][::-1]:
        print(f"{log['timestamp']} | User: {log['user_id']} | {log['action']}")


def find_action(action_keyword):
    """Search activity logs for entries containing a specific action keyword."""
    matches = [log for log in activity_logs if action_keyword.lower() in log['action'].lower()]
    if not matches:
        print(f"No logs found containing '{action_keyword}'.")
        return []
    print(f"\nFound {len(matches)} log entries with '{action_keyword}':")
    for log in matches:
        print(f"{log['timestamp']} | User: {log['user_id']} | {log['action']}")
    return matches


@log_activity()
def summarize_inventory():
    print(f"Loaded {len(smartcycle_components)} components.")
    print(f"Loaded {len(error_codes)} error codes.")


@log_activity()
def list_components():
    for cid, entry in smartcycle_components.items():
        print(f"{cid}: {entry['name']} (qty {entry['quantity']})")


@log_activity()
def list_error_codes():
    for code, info in error_codes.items():
        targets = ", ".join(info["components"])
        print(f"{code}: {info['description']} -> {targets}")


if __name__ == "__main__":
    summarize_inventory()
    print("\nUse lookup/add/update/delete for component operations.")
    print("Use list_error_codes() to review error mappings.")
    print("\nActivity Logging:")
    print("  - view_recent_logs(n=10) to see recent activity")
    print("  - find_action(keyword) to search logs")
