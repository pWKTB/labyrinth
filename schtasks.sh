schtasks

schtasks /Create /tn "autoGame_sub" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame_sub.py'" /sc HOURLY /mo 2



schtasks /Create /tn "autoGame" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame_event042Raid.py'" /sc MINUTE /mo 50 /ST 20:40
schtasks /Create /tn "autoGame_sub" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame_event042Raid_sub.py'" /sc MINUTE /mo 50 /ST 21:30




      <Command>C:\Windows\system32\cmd.exe</Command>
      <Arguments>/c "python C:\User_Program\labyrinth\firefoxAutoGame.py"</Arguments>

schtasks /Delete /tn "autoGame"
schtasks /Delete /tn "autoGame_sub"


http://sp.isky.am/acp/shh/?guid=ON&url=http%3A%2F%2Flb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com%2Fhkt48%2Fquest%2FitemDrop%3Funq%3D145572642756c49f5b2b73b