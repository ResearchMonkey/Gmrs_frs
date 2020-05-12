ctcss = {
    '67.0': '1 ',
    '71.9': '2 ',
    '74.4': '3 ',
    '77.0': '4 ',
    '79.7': '5 ',
    '82.5': '6 ',
    '85.4': '7 ',
    '88.5': '8 ',
    '91.5': '9 ',
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
    '462.5625': '1',
    '462.5875': '2',
    '462.6125': '3',
    '462.6375': '4',
    '462.6625': '5',
    '462.6875': '6',
    '462.7125': '7',
    '467.5625': '8',
    '467.5875': '9',
    '467.6125': '10',
    '467.6375': '11',
    '467.6625': '12',
    '467.6875': '13',
    '467.7125': '14',
    '462.5500': '15',
    '462.5750': '16',
    '462.6000': '17',
    '462.6250': '18',
    '462.6500': '19',
    '462.6750': '20',
    '462.7000': '21',
    '462.7250': '22'}

gmrs_frs_list = (
    '462.5625',
    '462.5875',
    '462.6125',
    '462.6375',
    '462.6625',
    '462.6875',
    '462.7125',
    '467.5625',
    '467.5875',
    '467.6125',
    '467.6375',
    '467.6625',
    '467.6875',
    '467.7125',
    '462.5500',
    '462.5750',
    '462.6000',
    '462.6250',
    '462.6500',
    '462.6750',
    '462.7000',
    '462.7250')

gmrs_frs_pw_2 = (
    '462.5625',
    '462.5875',
    '462.6125',
    '462.6375',
    '462.6625',
    '462.6875',
    '462.7125',
    '462.5500',
    '462.5750',
    '462.6000',
    '462.6250',
    '462.6500',
    '462.6750',
    '462.7000',
    '462.7250')

gmrs_frs_pw_0_5 = (
    '467.5625',
    '467.5875',
    '467.6125',
    '467.6375',
    '467.6625',
    '467.6875',
    '467.7125')

# https://chirp.danplanet.com/projects/chirp/wiki/MemoryEditorColumns
Loc = 0
Frequency = ''
Tone_Mode = ''
Tone = ''
ToneSql = ''
DTCS_Code = ''
DTCS_Rx_Code = ''
DTCS_Pol = ''
Duplex = ''
Offset = ''
Mode = ''
Tune_Step = ''
Skip = ''
Cross_Mode = ''
channel_name = ''
freq_channel_number = ''
freq_sub_channel = ''
watts = ''

# try:
#     f = open("chirp_GMRS_FRS.csv", "x")
# except FileExistsError:
#     print("File already existed")

print(
    "Loc, freq, Tone_Mode, Tone, ToneSql, DTCS_Code, DTCS_Rx_Code, DTCS_Pol, Duplex, Offset, Mode, Tune_Step, Skip, Cross_Mode, channel_name, watts")

for freq in gmrs_frs_list:
    for tone_ctcss in ctcss_list:
        # Sets the channel
        if freq in gmrs_frs:
            freq_channel_number = gmrs_frs[freq]
        # sets the sub channel
        if tone_ctcss in ctcss:
            freq_sub_channel = ctcss[tone_ctcss]
        channel_name = f"CH_{freq_channel_number}_{freq_sub_channel}"
        if freq in gmrs_frs_pw_2:
            watts = "2"
        else:
            watts = '0.5'
        Loc += 1

        # FIle for CHIRP
        f = open("chirp_GMRS_FRS.csv", "a")
        file_file_chirp = f"{Loc}, {freq}, {Tone_Mode}, {tone_ctcss}, {ToneSql}, {DTCS_Code}, {DTCS_Rx_Code}, {DTCS_Pol}, {Duplex}, {Offset}, {Mode}, {Tune_Step}, {Skip}, {Cross_Mode}, {channel_name}, {watts}\n"
        # print(file_file)
        f.write(file_file_chirp)
        f.close()

        # File for KG-UV9D(Plus)
        if watts == "2":
            watts = 'High'
        else:
            watts = "Low"
        f = open("wouxun_GMRS_FRS.csv", "a")
        file_file_wou = f"{Loc}, {freq}, {channel_name}, {Tone_Mode}, {tone_ctcss}, {ToneSql}, {DTCS_Code}, {DTCS_Rx_Code}, {DTCS_Pol}, {Duplex}, {Offset}, {Mode}, {Tune_Step}, {Skip}, {Cross_Mode}, {watts}\n"
        # print(file_file)
        f.write(file_file_wou)
        f.close()
