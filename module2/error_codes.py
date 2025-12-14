# Error codes. Smartcycle components have unique sensors on each component. If a component on each component fails it will trigger an error codes. However due to the variety of components, some error codes are shared between components and some are unique to a specific component.
from tabulate import tabulate
error_codes = {
    "E101": {"description": "Over-voltage detected", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E102": {"description": "Under-voltage detected", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E103": {"description": "Cell temperature high", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E104": {"description": "Cell temperature low", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E105": {"description": "Pack current over limit", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E106": {"description": "Short circuit detected", "components": ["BMS001", "BMS002", "BMS003", "BMS004", "BMS005", "BMS006"]},
    "E107": {"description": "Cell imbalance above threshold", "components": ["BMS001", "BMS003", "BMS004", "BMS005"]},
    "E108": {"description": "Charge FET stuck on", "components": ["BMS002", "BMS006"]},
    "E109": {"description": "Discharge FET stuck on", "components": ["BMS002", "BMS006"]},
    "E110": {"description": "State-of-charge estimation fault", "components": ["BMS001", "BMS002", "BMS003"]},
    "E111": {"description": "Internal ADC fault", "components": ["BMS001", "BMS003", "BMS004"]},
    "E112": {"description": "EEPROM configuration error", "components": ["BMS002", "BMS005"]},
    "E113": {"description": "Balancing transistor overheat", "components": ["BMS004", "BMS005"]},
    "E114": {"description": "Pack harness disconnect", "components": ["BMS001", "BMS003", "BMS005"]},
    "E115": {"description": "Isolation fault to chassis", "components": ["BMS004", "BMS006"]},
    "E116": {"description": "Precharge failure", "components": ["BMS001", "BMS003", "BMS006"]},
    "E117": {"description": "Fuse blown", "components": ["BMS004", "BMS005", "BMS006"]},
    "E118": {"description": "Pack contactor welded", "components": ["BMS004", "BMS006"]},
    "E119": {"description": "Pack contactor open", "components": ["BMS004", "BMS006"]},
    "E120": {"description": "Cell voltage sensor fault", "components": ["BMS001", "BMS003", "BMS005"]},
    "E121": {"description": "Thermistor open", "components": ["BMS001", "BMS002", "BMS003", "BMS006"]},
    "E122": {"description": "Thermistor short", "components": ["BMS001", "BMS002", "BMS003", "BMS006"]},

    "E201": {"description": "GNSS antenna open", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E202": {"description": "GNSS antenna short", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E203": {"description": "No satellite lock", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E204": {"description": "Low signal-to-noise ratio", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E205": {"description": "Time-to-first-fix timeout", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E206": {"description": "Ephemeris download failure", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E207": {"description": "Antenna detuned", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006"]},
    "E208": {"description": "RTC backup battery low", "components": ["GPS001", "GPS002", "GPS003", "GPS004"]},
    "E209": {"description": "PPS output missing", "components": ["GPS005", "GPS006", "GPS007"]},
    "E210": {"description": "RTK correction timeout", "components": ["GPS005", "GPS007"]},
    "E211": {"description": "Multipath suspected", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E212": {"description": "IMU fusion fault", "components": ["GPS004", "GPS005"]},
    "E213": {"description": "Dead-reckoning drift high", "components": ["GPS004", "GPS005"]},
    "E214": {"description": "Firmware image corrupt", "components": ["GPS001", "GPS003", "GPS004", "GPS006"]},
    "E215": {"description": "GNSS L1 band blocked", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E216": {"description": "GNSS L2 band blocked", "components": ["GPS005", "GPS007"]},
    "E217": {"description": "Temperature out of range", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E218": {"description": "UART communication fault", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},
    "E219": {"description": "I2C communication fault", "components": ["GPS002", "GPS003", "GPS004", "GPS005"]},
    "E220": {"description": "SPI communication fault", "components": ["GPS003", "GPS004", "GPS005", "GPS006"]},
    "E221": {"description": "Data flash wearout warning", "components": ["GPS001", "GPS004", "GPS006"]},
    "E222": {"description": "Jamming detected", "components": ["GPS001", "GPS002", "GPS003", "GPS004", "GPS005", "GPS006", "GPS007"]},

    "E301": {"description": "Resistor open circuit", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E302": {"description": "Resistor drift beyond tolerance", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E303": {"description": "Resistor overheating", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E304": {"description": "Lead corrosion detected", "components": ["RST001", "RST003", "RST004", "RST005", "RST007"]},
    "E305": {"description": "Solder joint crack", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E306": {"description": "ESD damage suspected", "components": ["RST002", "RST006", "RST008", "RST009"]},
    "E307": {"description": "Moisture ingress", "components": ["RST003", "RST004", "RST005", "RST007"]},
    "E308": {"description": "Potentiometer wiper noise", "components": ["RST008"]},
    "E309": {"description": "Fusible link blown", "components": ["RST007"]},
    "E310": {"description": "Wirewound hot spot", "components": ["RST004"]},
    "E311": {"description": "Thin film drift", "components": ["RST006"]},
    "E312": {"description": "Thick film drift", "components": ["RST005"]},
    "E313": {"description": "Carbon film noise", "components": ["RST001"]},
    "E314": {"description": "Metal film noise", "components": ["RST002", "RST009"]},
    "E315": {"description": "Oxide film value shift", "components": ["RST003"]},
    "E316": {"description": "Temperature coefficient exceeded", "components": ["RST002", "RST004", "RST006", "RST009"]},
    "E317": {"description": "Mechanical vibration loosened lead", "components": ["RST001", "RST003", "RST004", "RST005", "RST007"]},
    "E318": {"description": "SMD tombstoning", "components": ["RST005", "RST006"]},
    "E319": {"description": "Lead wire fatigue", "components": ["RST001", "RST003", "RST004", "RST007"]},
    "E320": {"description": "Overpower condition", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E321": {"description": "Hotspot detected near pad", "components": ["RST005", "RST006"]},
    "E322": {"description": "Wiper end-stop overrun", "components": ["RST008"]},
    "E323": {"description": "Precision tolerance exceeded", "components": ["RST002", "RST009"]},
    "E324": {"description": "Strain-induced value shift", "components": ["RST001", "RST003", "RST004"]},
    "E325": {"description": "Overvoltage surge", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E326": {"description": "Thermal runaway risk", "components": ["RST003", "RST004", "RST005", "RST006", "RST007"]},
    "E327": {"description": "Coating delamination", "components": ["RST003", "RST004", "RST005"]},
    "E328": {"description": "Core saturation (wirewound)", "components": ["RST004"]},
    "E329": {"description": "Noise floor elevated", "components": ["RST001", "RST002", "RST003", "RST009"]},
    "E330": {"description": "Contact resistance high", "components": ["RST008"]},
    "E331": {"description": "Lead short to chassis", "components": ["RST001", "RST003", "RST004", "RST005", "RST007"]},
    "E332": {"description": "Open via to resistor pad", "components": ["RST005", "RST006"]},
    "E333": {"description": "Laser trim drift", "components": ["RST002", "RST006", "RST009"]},
    "E334": {"description": "Value mismatch in parallel network", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E335": {"description": "Value mismatch in series network", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E336": {"description": "Potentiometer dead spot", "components": ["RST008"]},
    "E337": {"description": "Precision drift beyond 1%", "components": ["RST002", "RST009"]},
    "E338": {"description": "Fusible element ageing", "components": ["RST007"]},
    "E339": {"description": "Lead plating corrosion", "components": ["RST001", "RST003", "RST004", "RST005", "RST007"]},
    "E340": {"description": "Pad lift from PCB", "components": ["RST005", "RST006"]},
    "E341": {"description": "Mechanical shock damage", "components": ["RST001", "RST003", "RST004", "RST005", "RST007", "RST008"]},
    "E342": {"description": "Vibration-induced microcracks", "components": ["RST001", "RST003", "RST004", "RST005", "RST007", "RST008"]},
    "E343": {"description": "High humidity resistance drift", "components": ["RST001", "RST003", "RST005", "RST006"]},
    "E344": {"description": "Temperature cycling stress", "components": ["RST002", "RST004", "RST006", "RST009"]},
    "E345": {"description": "Hot spot from adjacent component", "components": ["RST005", "RST006"]},
    "E346": {"description": "Substrate microfracture", "components": ["RST002", "RST006", "RST009"]},
    "E347": {"description": "Terminal oxidation", "components": ["RST001", "RST003", "RST004", "RST005", "RST007"]},
    "E348": {"description": "PCB contamination leakage", "components": ["RST005", "RST006"]},
    "E349": {"description": "Overcleaning removed coating", "components": ["RST003", "RST004", "RST005"]},
    "E350": {"description": "Calibration required", "components": ["RST008", "RST009"]},
    "E351": {"description": "Thermal coefficient mismatch in network", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E352": {"description": "Noise exceeds specification", "components": ["RST001", "RST002", "RST003", "RST009"]},
    "E353": {"description": "Current noise in potentiometer", "components": ["RST008"]},
    "E354": {"description": "Contact lift-off detected", "components": ["RST004", "RST007"]},
    "E355": {"description": "Thermal fuse nuisance trip", "components": ["RST007"]},
    "E356": {"description": "Value shift after surge", "components": ["RST001", "RST002", "RST003", "RST004", "RST005", "RST006", "RST007", "RST008", "RST009"]},
    "E357": {"description": "High-frequency self-resonance issue", "components": ["RST002", "RST004", "RST006", "RST009"]},
    "E358": {"description": "Lead inductance too high", "components": ["RST004"]},
    "E359": {"description": "PCB pad voiding", "components": ["RST005", "RST006"]},
    "E360": {"description": "Potentiometer track wear", "components": ["RST008"]},
    "E361": {"description": "Value jump during adjustment", "components": ["RST008"]},
    "E362": {"description": "Precision resistor humidity drift", "components": ["RST009"]},
    "E363": {"description": "Metal film microcracks", "components": ["RST002", "RST009"]},
    "E364": {"description": "Wirewound vibration rattle", "components": ["RST004"]},
    "E365": {"description": "Fusible resistor temperature creep", "components": ["RST007"]},
    "E366": {"description": "Carbon film burn spot", "components": ["RST001"]},
}

# function to lookup multiple error codes from usage logs
def lookup_error_codes(error_codes_list=None):
    # paste in csv format error codes you want to lookup if error codes are not provided in the function call
    if error_codes_list is None:
        error_codes_list = input("Enter the error codes you want to lookup (comma-separated): > ")
        error_codes_list = error_codes_list.split(",")
    for code in error_codes_list:
        # if error code does not follow the pattern E### then raise an error saying that it must follow the apttern
        if not code.startswith("E") or len(code) != 5 or not code[1:].isdigit():
            raise ValueError(f"Error code {code} must folow the pattern E###")
        # if error code does not exist in the error codes list then also raise an error saying that there exists no such error code
        if code not in error_codes:
            raise ValueError(f"Error code {code} does not exist in the error codes list")
        # print the description and components associated with the error code in a table format we can use the tabulate library for this
        print(tabulate([[code, error_codes[code]['description'], ", ".join(error_codes[code]['components'])]], headers=["Error Code", "Description", "Components"], tablefmt="grid"))

# this will be a funtion to do a sweep and automatically remove any duplicate error codes from the list of error codes
def clean_error_codes():
    # paste in csv format error codes you want to lookup
    error_codes_list = input("Enter the error codes you want to lookup (comma-separated): > ")
    error_codes_list = error_codes_list.split(",")
    # remove any duplicate error codes from the list of error codes
    error_codes_list = list(set(error_codes_list))
    # print the cleaned list of error codes
    print("Cleaned list of error codes:")
    for code in error_codes_list:
        print(code)
    # at the descretion of the user, ask if they want the error codes to be looked up
    lookup = input("Do you want to look up the error codes? (y/n): > ")
    lookup = lookup.lower()
    if lookup == "y":
        lookup_error_codes()