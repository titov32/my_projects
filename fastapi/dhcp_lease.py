def lease(path):
    list_ip = []
    dict_ip = {}
    counter_bracket = 0
    with open(path, 'r') as file:
        for line in file:

            if '{' in line:
                counter_bracket += 1
            if '}\n' in line:
                counter_bracket -= 1

            if counter_bracket:
                if 'lease' in line:
                    ip = line[6:-2]
                    dict_ip['ip']=ip
                if 'hardware ethernet' in line:
                    hw = line.split('hardware ethernet')[-1][1:-2]
                    dict_ip['hw'] = hw
                if 'client-hostname' in line:
                    hostname = line[18:-2]
                    dict_ip['hostname'] = hostname
            else:
                list_ip.append(dict_ip.copy())
 #               del dict_ip
                dict_ip['hostname'] = ''
                dict_ip['ip'] = ''
                dict_ip['hw'] = ''
    return list_ip





if __name__=='__main__':

    list_ip=lease('dhcpd.leases')
    newlist = sorted(list_ip, key=lambda k: k['ip'])
    for i in newlist:
        print(i)

