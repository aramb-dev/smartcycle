# Init storage
# we will store smartcycle components in a dictionary so the system can quick look them up
# the dictionary will have component ID as the key such as BAT001, or SEN102, value will contain component name and how much are available
smartcycle_components = {
    "RST001": {"name": "Carbon-Film Fixed Resistor 5% 1kΩ", "quantity": 45},
    "RST002": {"name": "Metal Film Fixed Resistor 1% 10kΩ", "quantity": 82},
    "RST003": {"name": "Metal Oxide Film Fixed Resistor 5% 2.2kΩ", "quantity": 23},
    "RST004": {"name": "Wire Wound Fixed Resistor 5% 100Ω", "quantity": 67},
    "RST005": {"name": "Thick Film SMD Fixed Resistor 5% 4.7kΩ", "quantity": 91},
    "RST006": {"name": "Thin Film SMD Fixed Resistor 1% 100kΩ", "quantity": 8},
    "RST007": {"name": "Fusible Fixed Resistor 5% 10Ω", "quantity": 0},
    "RST008": {"name": "Linear Potentiometer 10% 10kΩ", "quantity": 56},
    "RST009": {"name": "Precision Linear Resistor 1% 470Ω", "quantity": 34},
    "BMS001": {"name": "TI bq76952 16-Cell Battery Monitor - High accuracy voltage/temp monitoring for Li-ion packs", "quantity": 10},
    "BMS002": {"name": "Maxim MAX17320 ModelGauge m5 - Smart battery fuel gauge with protector", "quantity": 20},
    "BMS003": {"name": "Analog Devices LTC6811 Multi-Cell Monitor - 12-cell battery stack monitor IC", "quantity": 15},
    "BMS004": {"name": "Infineon TLE9012AQU - 12-channel battery cell controller with integrated balancing", "quantity": 5},
    "BMS005": {"name": "NXP MC33771B 14-Cell Monitor - Automotive grade battery management controller", "quantity": 3},
    "BMS006": {"name": "Renesas ISL94202 - Multi-cell Li-ion battery pack monitor with FET control", "quantity": 10},
    "GPS001": {"name": "u-blox NEO-M9N - Multi-GNSS receiver with concurrent GPS/GLONASS/Galileo/BeiDou", "quantity": 42},
    "GPS002": {"name": "Quectel L76-L - Ultra-compact GPS/GLONASS module with integrated antenna", "quantity": 67},
    "GPS003": {"name": "MediaTek MT3333 - High sensitivity GPS chipset with 99 channels", "quantity": 28},
    "GPS004": {"name": "STMicroelectronics Teseo-LIV3F - Tiny GNSS module with dead reckoning", "quantity": 15},
    "GPS005": {"name": "u-blox ZED-F9P - Multi-band RTK GNSS receiver with cm-level accuracy", "quantity": 8},
    "GPS006": {"name": "SkyTraq Venus638FLPx - Low power GPS receiver with 1Hz-10Hz update rate", "quantity": 53},
    "GPS007": {"name": "Trimble BD970 - Dual-frequency RTK GNSS OEM board for precision positioning", "quantity": 3},
}

# now to lookup a component by ID, we can use the following function
def lookup(component_id):
    if component_id in smartcycle_components:
        return f"ID: {component_id}, Name: {smartcycle_components[component_id]['name']}, Quantity: {smartcycle_components[component_id]['quantity']}"
    else:
        add_component = input(f"Component ID {component_id} not found. Would you like to add it to the SmartCycle component system? (y/n): > ")
        if add_component.lower() == 'y':
            component_name = input("Enter the component name: > ")
            component_quantity = int(input("Enter the component quantity: > "))
            smartcycle_components[component_id] = {"name": component_name, "quantity": component_quantity}
            return smartcycle_components[component_id]
        else:
            return None
def update(component_id):
    if component_id not in smartcycle_components:
        return f"Component ID {component_id} not found."

    new_ID = input("Enter the new component ID, or press Enter to keep the current ID: > ")
    new_name = input("Enter the new component name, or press Enter to keep the current name: > ")
    new_quantity = input("Enter the new component quantity, or press Enter to keep the current quantity: > ")

    if new_ID:
        if not (len(new_ID) == 6 and new_ID[0:3].isalpha() and new_ID[3:6].isdigit()):
            return "Invalid component ID format. It should be in the format AAA###."
        if new_ID in smartcycle_components and new_ID != component_id:
            return "Component ID already exists."

    current_entry = smartcycle_components[component_id]
    updated_entry = current_entry.copy()
    summary_lines = []

    if new_ID:
        summary_lines.append(f"ID: {component_id} -> {new_ID}")
    else:
        summary_lines.append(f"ID: unchanged ({component_id})")

    if new_name:
        updated_entry["name"] = new_name
        summary_lines.append(f"Name: '{current_entry['name']}' -> '{new_name}'")
    else:
        summary_lines.append(f"Name: unchanged ('{current_entry['name']}')")

    if new_quantity:
        try:
            proposed_qty = int(new_quantity)
        except ValueError:
            return "Invalid quantity. Please enter a number."
        updated_entry["quantity"] = proposed_qty
        summary_lines.append(f"Quantity: {current_entry['quantity']} -> {proposed_qty}")
    else:
        summary_lines.append(f"Quantity: unchanged ({current_entry['quantity']})")

    print("Summary of changes:")
    for line in summary_lines:
        print(f"- {line}")

    confirm = input("Apply these changes? (y/n): > ").strip().lower()
    if confirm != "y":
        return "Update cancelled."

    if new_ID and new_ID != component_id:
        smartcycle_components[new_ID] = updated_entry
        del smartcycle_components[component_id]
        component_id = new_ID
    else:
        smartcycle_components[component_id] = updated_entry

    return f"Updated {component_id}: {updated_entry['name']} (qty {updated_entry['quantity']})"

def add(component_id, component_name, component_quantity):
    # this will also be interactive, however component id will be the first required param and the rest if not therwe will be prompted
    if component_id in smartcycle_components:        
        return f"Component ID {component_id} already exists."
    if not (len(component_id) == 6 and component_id[0:3].isalpha() and component_id[3:6].isdigit()):
        return "Invalid component ID format. It should be in the format AAA###."
    if not component_name:        
        component_name = input("Enter the component name: > ")
    if not component_quantity:        
        component_quantity = int(input("Enter the component quantity: > "))
    smartcycle_components[component_id] = {"name": component_name, "quantity": component_quantity}

    return smartcycle_components[component_id]

def delete(component_id):
    if component_id not in smartcycle_components:
        return f"Component ID {component_id} not found."
    confirm = input(f"are you sure you would like to delete component {component_id}? (y/n): > ")
    confirm = confirm.strip().lower()
    if confirm != "y":
        return "Deletion cancelled."
    else:
        del smartcycle_components[component_id]
        return f"Component {component_id} has been successfully deleted."
    
# Error codes. Smartcycle components have unique sensors on each component. If a component on each component fails it will trigger an error codes. However due to the variety of components, some error codes are shared between compnents and some are unique to a specific compnent.
error_codes= {}