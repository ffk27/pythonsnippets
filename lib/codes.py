stationnumbers = {
    42: 'Zwanenburg',
    43: 'Utrecht', 
    44: 'Haarlem', 
    45: 'Delft',
    46: 'Alkmaar', 
    47: 'Bergen', 
    48: 'Haarlem2', 
    49: 'Delft/Rijnsburg', 
    50: 'Leiden', 
    51: 'Leiden2', 
    52: 'Amsterdam', 
    53: 'Amsterdam2', 
    54: 'Vlissingen', 
    55: 'Middelburg', 
    56: 'Breda', 
    57: 'Breda2'
}

def date(YYYYMMDD):
    return [int(YYYYMMDD[0:4]),int(YYYYMMDD[4:6]),int(YYYYMMDD[6:8])]

# Fahrenheit naar celcius
def F2C(T):
    return (int(T) - 320) / 18

columnnames = ['STN','YYYYMMDD','M','P','T','DD','FH','WW','RH','W2']
datatypes = [int, date, int, float, F2C, str, float, str, float, str]

columncodes = {
    'STN': 'national station number',
    'YYYYMMDD': 'datum / date (YYYY=year MM=month DD=day)',
    'M': 'meting volgnummer / measurement number (1,2 or 3)',
    'P': 'luchtdruk in Rijnlandse of Engelse duimen en lijnen / surface air pressure in "Rijnlandse" or "English" inches and lines toelichting: eerste 2 cijfers is aantal duimen, volgende 2 cijfers is aantal lijnen, laatste cijfer is het aantal kwarten van lijnen. explanation: first 2 numbers is number of inches, next 2 numbers is number of lines, last number is number of quarters of lines. 1 "Rijnlandse" inch(duim) = 12 lines = 48 kwarten = 2.62 cm; 1 "English" inch = 2.54 cm',
    'T': 'temperatuur in Fahrenheit / temperature in Fahrenheit  (Fahrenheit -32 * (5/9)= Celsius)',
    'DD': 'windrichting / winddirection (N=North, O=East, Z=South, W=West, T=at)',
    'FH': 'windsnelheid in diverse schalen het laatste cijfer is het aantal kwarten / windspeed in several scales see the metadata, the last number is number of quarters of degrees (example: 552 = 55 + 2/4 = 55,5)',
    'WW': 'luchtgesteldheid in 3 lettercodes/ weather conditions in three letter code See for code downwards',
    'RH': 'neerslag in lijnen / precipitation in lines ( 1 line = 2.62/12 = 0.22 cm )',
    'W2': 'bijzondere weersverschijnselen / special weather conditions in code'
}

weathercodes = {
    'BET': 'betrokken / cloudy',
    'BLI': 'bliksem / lightning',
    'BUY': 'bui / shower',
    'BYN': 'bijna / almost',
    'DAM': 'dampig / hazy',
    'DAU': 'dauw / dew',
    'DON': 'donder / thunder',
    'DOK': 'donker / dark',
    'DRO': 'droog / dry',
    'ENN': 'en / and',
    'GEH': 'geheel / whole',
    'HAG': 'hagel / hail',
    'HEL': 'helder / clear',
    'MEE': 'meest / mostly',
    'MIS': 'mist / fog',
    'MIG': 'mistig / foggy',
    'MOT': 'motregen / drizzle',
    'NAT': 'natte / wet',
    'NEV': 'nevel / hazy',
    'NOO': 'noorderlicht / northern lights',
    'OMT': 'omtrent / about',
    'MOG': 'mottig / thick',
    'ONW': 'onweer / thunderstorm',
    'REG': 'regen / rain',
    'RET': 'regenachtig / rainy',
    'RYP': 'rijp / rime',
    'SNE': 'sneeuw / snow',
    'STO': 'stofregen / drizzle',
    'VEE': 'veel / much',
    'VOG': 'vochtig / moist',
    'WAT': 'wat / somewhat',
    'WEE': 'weerlicht / heat lightning',
    'YSS': 'ijs / ice',
    'YZL': 'ijzelig / glazed frost',
    'ZEE': 'zeer / very',
    'ZEV': 'zeevlam / seafog',
    'ZWA': 'zwaar / heavy'
}
