ctcss = {
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

ctcss_list = (
    '67.0',
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
    '162.2',
    '167.9',
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
    '250.3')

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

gmrs_frs_list = (
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
    '462.725000')

gmrs_frs_pw_2 = (
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

gmrs_frs_pw_0_5 = (
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

# https://chirp.danplanet.com/projects/chirp/wiki/MemoryEditorColumns
Location = 40
Frequency = ''
Name = ''
Tone_Mode = ''
Tone = 'TSQL'
ToneSql = ''
DTCS_Code = ''
DTCS_Pol = ''
Duplex = ''
Offset = '0.000000'
Mode = 'FM'
Tune_Step = ''
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
DtcsCode = '023'
DtcsPolarity = 'NN'
TStep = '5.00'
DVCODE = ''

# try:
#     f = open("chirp_GMRS_FRS.csv", "x")
# except FileExistsError:
#     print("File already existed")

print('Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,Mode,TStep,Skip,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE')
f = open("chirp_GMRS_FRS.csv", "w")
f.write(f'Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,Mode,TStep,Skip,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE\n')
f.close()

for freq in gmrs_frs_list:
    for tone_ctcss in ctcss_list:
        rToneFreq = tone_ctcss
        cToneFreq = tone_ctcss
        # Sets the channel
        if freq in gmrs_frs:
            freq_channel_number = gmrs_frs[freq]
        # sets the sub channel
        if tone_ctcss in ctcss:
            freq_sub_channel = ctcss[tone_ctcss]
            rToneFreq = tone_ctcss
            cToneFreq = tone_ctcss
        channel_name = f"CH {freq_channel_number} {freq_sub_channel}"
        # if freq in gmrs_mode_NFM:
        #     Mode = 'NFM'
        # else:
        #     Mode = 'FM'
        if freq in gmrs_frs_pw_2:
            Power = "L"
        else:
            Power = 'L'
        Location += 1

        # FIle for CHIRP
        f = open("chirp_GMRS_FRS.csv", "a")
        file_file_chirp = f"{Location},{channel_name},{freq},{Duplex},{Offset},{Tone},{rToneFreq},{cToneFreq},{DtcsCode},{DtcsPolarity},{Mode},{TStep},{Skip},{Comment},{URCALL},{RPT1CALL},{RPT2CALL},{DVCODE}\n"
        # print(file_file)
        f.write(file_file_chirp)
        f.close()

