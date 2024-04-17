# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IG9zLCB4Ym1jLCB4Ym1jYWRkb24NCg0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQojIyMgR2xvYmFsIFZhcmlhYmxlcyAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KUEFUSCAgICAgICAgICAgPSB4Ym1jYWRkb24uQWRkb24oKS5nZXRBZGRvbkluZm8oJ3BhdGgnKQ0KQVJUICAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oUEFUSCwgJ3Jlc291cmNlcycsICdhcnQnKQ0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQoNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KIyMjIFVzZXIgRWRpdCBWYXJpYWJsZXMgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCkFERE9OX0lEICAgICAgID0geGJtY2FkZG9uLkFkZG9uKCkuZ2V0QWRkb25JbmZvKCdpZCcpDQpBRERPTlRJVExFICAgICA9ICdbQ09MT1Igb3JjaGlkXVtCXVRIRSBDUkVXIFdJWkFSRFsvQl1bL0NPTE9SXScNCkJVSUxERVJOQU1FICAgID0gJ1tDT0xPUiB3aGl0ZV1bQl1UaGUgQ3Jld1svQl1bL0NPTE9SXScNCkVYQ0xVREVTICAgICAgID0gW0FERE9OX0lELCAncmVwb3NpdG9yeS50aGVjcmV3JywgJ3NjcmlwdC5tb2R1bGUua29kaS1zaXgnLCAnc2NyaXB0Lm1vZHVsZS5zaXgnXQ0KIyBFbmFibGUvRGlzYWJsZSB0aGUgdGV4dCBmaWxlIGNhY2hpbmcgd2l0aCAnWWVzJyBvciAnTm8nIGFuZCBhZ2UgYmVpbmcgaG93IG9mdGVuIGl0IHJlY2hlY2tzIGluIG1pbnV0ZXMNCkNBQ0hFVEVYVCAgICAgID0gJ1llcycNCkNBQ0hFQUdFICAgICAgID0gMzANCiMgVGV4dCBGaWxlIHdpdGggYnVpbGQgaW5mbyBpbiBpdC4NCkJVSUxERklMRSAgICAgID0gJ2h0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wb3NhZGthL2J1aWxkcy9tYWluL2J1aWxkcy9idWlsZHMudHh0Jw0KIyBIb3cgb2Z0ZW4geW91IHdvdWxkIGxpa2UgaXQgdG8gY2hlY2sgZm9yIGJ1aWxkIHVwZGF0ZXMgaW4gZGF5cw0KIyAwIGJlaW5nIGV2ZXJ5IHN0YXJ0dXAgb2Yga29kaQ0KVVBEQVRFQ0hFQ0sgICAgPSAwDQojIFRleHQgRmlsZSB3aXRoIGFwayBpbmZvIGluIGl0LiAgTGVhdmUgYXMgJ2h0dHBzOi8vJyB0byBpZ25vcmUNCkFQS0ZJTEUgICAgICAgID0gJ2h0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9wb3NhZGthL2J1aWxkcy9tYWluL2J1aWxkcy9idWlsZHMudHh0Jw0KIyBUZXh0IEZpbGUgd2l0aCBZb3V0dWJlIFZpZGVvcyB1cmxzLiAgTGVhdmUgYXMgJ2h0dHBzOi8vJyB0byBpZ25vcmUNCllPVVRVQkVUSVRMRSAgID0gJycNCllPVVRVQkVGSUxFICAgID0gJ2h0dHBzOi8vJw0KIyBUZXh0IEZpbGUgZm9yIGFkZG9uIGluc3RhbGxlci4gIExlYXZlIGFzICdodHRwczovLycgdG8gaWdub3JlDQpBRERPTkZJTEUgICAgICA9ICdo'
love = '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'
god = 'dGhlIHRleHQgZnJvbSB0aGUgbWVudSBpdGVtDQpDT0xPUjEgICAgICAgICA9ICdvcmNoaWQnDQpDT0xPUjIgICAgICAgICA9ICd3aGl0ZScNCiMgUHJpbWFyeSBtZW51IGl0ZW1zICAgLyAlcyBpcyB0aGUgbWVudSBpdGVtIGFuZCBpcyByZXF1aXJlZA0KVEhFTUUxICAgICAgICAgPSAnW0NPTE9SICcrQ09MT1IxKyddKlsvQ09MT1JdICBbQ09MT1IgJytDT0xPUjIrJ10lc1svQ09MT1JdJw0KIyBCdWlsZCBOYW1lcyAgICAgICAgICAvICVzIGlzIHRoZSBtZW51IGl0ZW0gYW5kIGlzIHJlcXVpcmVkDQpUSEVNRTIgICAgICAgICA9ICdbQ09MT1IgJytDT0xPUjIrJ10lc1svQ09MT1JdJw0KIyBBbHRlcm5hdGUgaXRlbXMgICAgICAvICVzIGlzIHRoZSBtZW51IGl0ZW0gYW5kIGlzIHJlcXVpcmVkDQpUSEVNRTMgICAgICAgICA9ICdbQ09MT1IgJytDT0xPUjErJ10lc1svQ09MT1JdJw0KIyBDdXJyZW50IEJ1aWxkIEhlYWRlciAvICVzIGlzIHRoZSBtZW51IGl0ZW0gYW5kIGlzIHJlcXVpcmVkDQpUSEVNRTQgICAgICAgICA9ICdbQ09MT1IgJytDT0xPUjErJ11DdXJyZW50IEJ1aWxkOlsvQ09MT1JdIFtDT0xPUiAnK0NPTE9SMisnXSVzWy9DT0xPUl0nDQojIEN1cnJlbnQgVGhlbWUgSGVhZGVyIC8gJXMgaXMgdGhlIG1lbnUgaXRlbSBhbmQgaXMgcmVxdWlyZWQNClRIRU1FNSAgICAgICAgID0gJ1tDT0xPUiAnK0NPTE9SMSsnXUN1cnJlbnQgVGhlbWU6Wy9DT0xPUl0gW0NPTE9SICcrQ09MT1IyKyddJXNbL0NPTE9SXScNCg0KIyBNZXNzYWdlIGZvciBDb250YWN0IFBhZ2UNCiMgRW5hYmxlICdDb250YWN0JyBtZW51IGl0ZW0gJ1llcycgaGlkZSBvciAnTm8nIGRvbnQgaGlkZQ0KSElERUNPTlRBQ1QgICAgPSAnTm8nDQojIFlvdSBjYW4gYWRkIFxuIHRvIGRvIGxpbmUgYnJlYWtzDQpDT05UQUNUICAgICAgICA9ICdLRUVQIENBTE0gYW5kIEVYUEVDVCBVU1xuXG5XaGl0ZWhhdC4uLlxuXG5HcmV5aGF0Li4uXG5cbkJsYWNraGF0XG5cbkJsdWVoYXQuLi5cblxuR3JlZW5oYXQuLi4nDQojSW1hZ2VzIHVzZWQgZm9yIHRoZSBjb250YWN0IHdpbmRvdy4gIGh0dHBzOi8vIGZvciBkZWZhdWx0IGljb24gYW5kIGZhbmFydA0KQ09OVEFDVElDT04gICAgPSBvcy5wYXRoLmpvaW4oQVJULCAncXJpY29uLnBuZycpDQpDT05UQUNURkFOQVJUICA9ICdodHRwczovLycNCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMjIyBBdXRvIFVwZGF0ZSAgICAgICAgICAgICAgICAgICAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KIyMjICAgICAgICBGb3IgVGhvc2UgV2l0aCBObyBSZXBvICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCiMgRW5hYmxlIEF1dG8gVXBkYXRlICdZZXMnIG9yICdObycNCkFVVE9VUERBVEUgICAgID0gJ25vJw0KIyBVcmwgdG8gd2l6YXJkIHZlcnNpb24NCldJWkFSREZJTEUgICAgID0gQlVJTERGSUxFDQojIyMjIyMjIyMjIyMjIyMjIyMj'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))