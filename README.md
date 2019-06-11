# cgxSIPalg
Enable or disable SIP ALG on devices

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Setup authentication as listed below
* Create a csv file with the example at devicelist.csv
* run the script using: python3 cgxSIPalg --all --enable


Notice: only -all is implemented at the moment

cgxSIPalg.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)


Example of a run:
```
bash$ ./cgxSIPalg.py  --all --enable
INFO:cgxSIPalg:ION-VY- at Site Vineyard is being configured
INFO:cgxSIPalg:-- already have algconfig
INFO:cgxSIPalg:-- SIP alg found. Updating
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-MX- at Site MX is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-CO- at Site CO is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-HQC-Ion_3k at Site HQC is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-ES- at Site ES is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-CL- at Site CL is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-EC- at Site EC is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-ID- at Site ID is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-BO- at Site BO is being configured
INFO:cgxSIPalg:-- already have algconfig
INFO:cgxSIPalg:-- SIP alg found. Updating
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-PE- at Site PE is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-ID-SBY- at Site ID-SBY is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-JP- at Site JP is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-MY- at Site MY is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-TW- at Site TW is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-KR- at Site KR is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
INFO:cgxSIPalg:ION-Test- at Site Test Site is being configured
INFO:cgxSIPalg:-- creating algconfig name space
INFO:cgxSIPalg:-- SIP alg not found. adding sip rule
INFO:cgxSIPalg:-- updating alg entry
```