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
        man_split[1] = '#Maghaze'
        my_lst_str = ''.join(map(str, man_split))

        man1 = open("config1", "a")
        man2 = open("config2", "a")
        man3 = open("config3", "a")
        man1 = open("config1", "a")
        man4 = open("config4", "a")
        man5 = open("config5", "a")
        man6 = open("config6", "a")
        man7 = open("config7", "a")
        man8 = open("config8", "a")
        man9 = open("config9", "a")
        man10 = open("config10", "a")

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
