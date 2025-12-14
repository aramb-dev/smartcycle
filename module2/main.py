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
