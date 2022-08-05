import csv
import re

ctcss_gmrs_frs_sub = {
    '67.0': '1',
    '71.9': '2',
    '74.4': '3',
    '77.0': '4',
    '79.7': '5',
    '82.5': '6',
    '85.4': '7',
    '88.5': '8',
    '91.5': '9',
    '94.8': '10',
    '97.4': '11',
    '100.0': '12',
    '103.5': '13',
    '107.2': '14',
    '110.9': '15',
    '114.8': '16',
    '118.8': '17',
    '123.0': '18',
    '127.3': '19',
    '131.8': '20',
    '136.5': '21',
    '141.3': '22',
    '146.2': '23',
    '151.4': '24',
    '156.7': '25',
    '162.2': '26',
    '167.9': '27',
    '173.8': '28',
    '179.9': '29',
    '186.2': '30',
    '192.8': '31',
    '203.5': '32',
    '210.7': '33',
    '218.1': '34',
    '225.7': '35',
    '233.6': '36',
    '241.8': '37',
    '250.3': '38'}

ctcss = (
    '67.0',
    '69.3'
    '71.9',
    '74.4',
    '77.0',
    '79.7',
    '82.5',
    '85.4',
    '88.5',
    '91.5',
    '94.8',
    '97.4',
    '100.0',
    '103.5',
    '107.2',
    '110.9',
    '114.8',
    '118.8',
    '123.0',
    '127.3',
    '131.8',
    '136.5',
    '141.3',
    '146.2',
    '151.4',
    '156.7',
    '159.8',
    '162.2',
    '165.5',
    '167.9',
    '171.3',
    '173.8',
    '179.9',
    '186.2',
    '192.8',
    '203.5',
    '210.7',
    '218.1',
    '225.7',
    '233.6',
    '241.8',
    '250.3',
    '254.1')

gmrs_frs = {
    '462.562500': '1',
    '462.587500': '2',
    '462.612500': '3',
    '462.637500': '4',
    '462.662500': '5',
    '462.687500': '6',
    '462.712500': '7',
    '467.562500': '8',
    '467.587500': '9',
    '467.612500': '10',
    '467.637500': '11',
    '467.662500': '12',
    '467.687500': '13',
    '467.712500': '14',
    '462.550000': '15',
    '462.575000': '16',
    '462.600000': '17',
    '462.625000': '18',
    '462.650000': '19',
    '462.675000': '20',
    '462.700000': '21',
    '462.725000': '22'}

gmrs_frs_power_2 = (
    '462.562500',
    '462.587500',
    '462.612500',
    '462.637500',
    '462.662500',
    '462.687500',
    '462.712500',
    '462.550000',
    '462.575000',
    '462.600000',
    '462.625000',
    '462.650000',
    '462.675000',
    '462.700000',
    '462.725000')

gmrs_frs_power_2 = (
    '467.562500',
    '467.587500',
    '467.612500',
    '467.637500',
    '467.662500',
    '467.687500',
    '467.712500')

gmrs_mode_NFM = (
    '462.562500',
    '462.587500',
    '462.612500',
    '462.637500',
    '462.662500',
    '462.687500',
    '462.712500',
    '467.562500',
    '467.587500',
    '467.612500',
    '467.637500',
    '467.662500',
    '467.687500',
    '467.712500',
    '462.550000',
    '462.575000',
    '462.600000',
    '462.625000',
    '462.650000',
    '462.675000',
    '462.700000',
    '462.725000',
    '467.562500',
    '467.587500',
    '467.612500',
    '467.637500',
    '467.662500',
    '467.687500',
    '467.712500')

freq_tx_range1 = range(400, 512)
freq_tx_range2 = range(136, 174)
freq_tx_range = freq_tx_range1, freq_tx_range2

freq__rx_range_AM1 = range(76, 108)
freq__rx_range_AM2 = range(108, 136)
freq__rx_range_FM1 = range(136, 180)
freq__rx_range_FM2 = range(230, 250)
freq__rx_range_FM3 = range(350, 400)
freq__rx_range_FM4 = range(400, 512)
freq__rx_range_FM5 = range(700, 985)

# https://chirp.danplanet.com/projects/chirp/wiki/MemoryEditorColumns
Location = 1
# Frequency format = 140.125000
Frequency = ''
Name = ''
Tone_Mode = ''
# Tone options 'Tone', 'TSQL', 'DTCS', 'Cross', ''
Tone = ''
ToneSql = ''
DTCS_Code = ''
DTCS_Pol = ''
Duplex = ''
Offset = ''
Mode = ''
Tune_Step = ''
# Skip options = 'S', ''
Skip = ''
Comment = ''
URCALL = ''
RPT1CALL = ''
RPT2CALL = ''
DTCS_Rx_Code = ''
Cross_Mode = ''
channel_name = ''
freq_channel_number = ''
freq_sub_channel = ''
Power = ''
rToneFreq = ''
cToneFreq = ''
DtcsCode = ''
DtcsPolarity = ''
TStep = ''
DVCODE = ''
# file_format_chirp = f"{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"


def write_to_file(file_name, file_values):
    # file_file_chirp_2 = f"{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
    print(file_values)
    f = open(file_name, "a")
    f.write(file_values)
    f.close()

def csv_to_chirp_import(file_to_read, file_to_write):
    with open(file_to_read, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        f = open(file_to_write, "w")
        f.write(
            f'Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,Mode,TStep,Skip,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE\n')
        f.close()
        Location = 1
        for row in csv_reader:
            if line_count == 0:
                # print(f'column headers are {", ".join(row)}')
                line_count += 1
            Frequency = row["Frequency Output"]
            abc1 = float(Frequency)
            abc2 = int(abc1)
            channel_name = row["Alpha Tag"]
            # will only process lines with in the defined freq range
            # file_file_chirp_2 = f"{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
            if abc2 in freq_tx_range1\
                    or abc2 in freq_tx_range2\
                    or abc2 in freq__rx_range_AM1\
                    or abc2 in freq__rx_range_AM2\
                    or abc2 in freq__rx_range_FM1\
                    or abc2 in freq__rx_range_FM2\
                    or abc2 in freq__rx_range_FM3\
                    or abc2 in freq__rx_range_FM4\
                    or abc2 in freq__rx_range_FM5:
                channel_name = row["Alpha Tag"]
                if "AM" in row["Mode"]:
                    Mode = "AM"
                    Frequency = row["Frequency Output"]
                    Offset = '0.000000'
                    Tone = ''
                    Duplex = 'off'
                    rToneFreq = '88.5'
                    cToneFreq = '88.5'
                    DtcsCode = '023'
                    DtcsPolarity = 'NN'
                    TStep = '5.00'
                    Location += 1
                    file_file_chirp_2 = f"{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
                    write_to_file(file_to_write, file_file_chirp_2)
                if 'PL' in row["PL Tone"]:
                    a_rToneFreq = re.sub('[^0-9.]', '', row["PL Tone"])
                    print(a_rToneFreq)
                    if 'DPL' in row["PL Tone"]:
                        Mode = 'DTCS'
                        Tone = 'DTCS'
                        print("DPL in PL tone")
                        DtcsCode = a_rToneFreq
                    elif "CC" in row["PL Tone"]:
                        ctcss_type = 'unknown'
                    else:
                        Mode = 'TSQL'
                        Tone = 'TSQL'
                        print("PL in PL tone")
                        DtcsCode = '0'
                        rToneFreq = a_rToneFreq
                        cToneFreq = a_rToneFreq
                    Offset = '0.000000'
                    if "FM" in row["Mode"]:
                        Mode = "FM"
                    DtcsPolarity = 'NN'
                    TStep = '5.00'
                    Duplex = ''
                    Location += 1
                    file_file_chirp_2 = f"{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
                    write_to_file(file_to_write, file_file_chirp_2)


def add_frs_channels():
    # TODO add logic to read the file created above and start the location numbering form where it leaves off
    print("{Location},{channel_name},{Frequency},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n")
    f = open("chirp_GMRS_FRS.csv", "w")
    f.write(f'Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,Mode,TStep,Skip,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE\n')
    f.close()
    Location = 65
    Tone = 'TSQL'
    Offset = '0.000000'
    Mode = 'FM'
    DtcsCode = '023'
    DtcsPolarity = 'NN'
    TStep = '5.00'
    for freq, freq_value in gmrs_frs.items():
        # print(f'Freq {freq} is channel number {freq_value}')
        for ctss_freq, ctss_freq_vl in ctcss_gmrs_frs_sub.items():
            rToneFreq = ctss_freq
            cToneFreq = ctss_freq
            channel_name = f"CH {freq_value} {ctss_freq_vl}"
            if ctss_freq == '67.0':
                Skip = ''
            else:
                Skip = 'S'
            Location += 1
            file_format_chirp = f"{Location},{channel_name},{freq},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
            print(file_format_chirp)
            f = open("chirp_GMRS_FRS.csv", "a")
            f.write(file_format_chirp)
            f.close()


add_frs_channels()

csv_to_chirp_import('ctid_2502.csv', 'ruth.csv')
# csv_to_chirp_import('ctid_2487.csv', 'import_csv_dowload3.csv')
# csv_to_chirp_import('ctid_2446.csv', 'import_csv_dowload4.csv')
