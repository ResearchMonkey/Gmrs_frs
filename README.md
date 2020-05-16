# Gmrs_frs
Creates a CSV of GMRS/FRS channels and CTCSS tones for upload to radio. I wanted to be able to pull down channel lists and upload them to my radio quickly and easly. I wanted to be able to have the GMRS/FRS channels in the radio.

https://www.radioreference.com/
https://chirp.danplanet.com/projects/chirp/wiki/Home

 add_frs_channels() creates a CSV file for uploading GMRS/FRS channels to a radio via chirp.
 csv_to_chirp_import(file_to_read, file_to_write) takes a downloaded csv file from https://www.radioreference.com and reformats it for upload to a radio. 
