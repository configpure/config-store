import requests

url = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vless'

r = requests.get(url, allow_redirects=True)

open('vless', 'wb').write(r.content)

#ss
data = open('vless', 'rb')
max = data.readlines()

for man in max:
    man = man.decode()
    man_split = man.split("#")

    try:
        man_split[1] = '#Store'
        my_lst_str = ''.join(map(str, man_split))

        man1 = open("erg345345", "a")
        man2 = open("gdafg45345", "a")
        man3 = open("gdf6456456", "a")
        man1 = open("corytrtynfig1", "a")
        man4 = open("cshonfshig4", "a")
        man5 = open("dcosdfhdfhnfig5", "a")
        man6 = open("coddsfhsdhnfig6", "a")
        man7 = open("cdonsdfhficvbg7", "a")
        man8 = open("codnfxcvbig8", "a")
        man9 = open("coxcnfigzbvcxvbn9", "a")
        man10 = open("con25fig12342350", "a")

        man1.writelines(str(my_lst_str) + "\n")
        man2.writelines(str(my_lst_str) + "\n")
        man3.writelines(str(my_lst_str) + "\n")
        man4.writelines(str(my_lst_str) + "\n")
        man5.writelines(str(my_lst_str) + "\n")
        man6.writelines(str(my_lst_str) + "\n")
        man7.writelines(str(my_lst_str) + "\n")
        man8.writelines(str(my_lst_str) + "\n")
        man9.writelines(str(my_lst_str) + "\n")
        man10.writelines(str(my_lst_str) + "\n")

    except:
        pass

man1.close()
man2.close()
man3.close()
man4.close()
man5.close()
man6.close()
man7.close()
man8.close()
man9.close()
man10.close()
