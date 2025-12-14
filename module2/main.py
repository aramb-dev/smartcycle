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
    
}