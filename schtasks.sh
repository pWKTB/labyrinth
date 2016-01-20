schtasks

schtasks /Create /tn "autoGame_sub" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame_sub.py'" /sc HOURLY /mo 2



schtasks /Create /tn "autoGame" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame.py'" /sc MINUTE /mo 72 /ST 01:08
schtasks /Create /tn "autoGame_sub" /tr "C:\Windows\system32\cmd.exe /c 'python C:\User_Program\labyrinth\firefoxAutoGame_sub.py'" /sc MINUTE /mo 100 /ST 00:00




      <Command>C:\Windows\system32\cmd.exe</Command>
      <Arguments>/c "python C:\User_Program\labyrinth\firefoxAutoGame.py"</Arguments>