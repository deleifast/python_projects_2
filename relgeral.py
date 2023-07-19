#encoding: iso-8859-1
import os, os.path
    
#Loja01#

try:
    if os.path.exists('relsat_loja01.txt'):
        os.remove('relsat_loja01.txt')
    else:
        pass
    os.chdir('c:\\remarca\lojas')
    with open('lj01.sat_101.txt', 'r') as f1, open('lj01.sat_120.txt', 'w') as f2: 
        f2.write(f1.read())
#        print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
'''
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relsat_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.sat_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('relimp_loja01.txt'):
        os.remove('relimp_loja01.txt')
    else:
        pass
    with open("relimp_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relimp_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.imp_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('relcpu_loja01.txt'):
        os.remove('relcpu_loja01.txt')
    else:
        pass
    with open("relcpu_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relcpu_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.cpu_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('reldns_loja01.txt'):
        os.remove('reldns_loja01.txt')
    else:
        pass
    with open("reldns_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("reldns_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.dns_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('relip_loja01.txt'):
        os.remove('relip_loja01.txt')
    else:
        pass
    with open("relip_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relip_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.ip_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('relkey_loja01.txt'):
        os.remove('relkey_loja01.txt')
    else:
        pass
    with open("relkey_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relkey_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.key_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    if os.path.exists('relverpdv_loja01.txt'):
        os.remove('relverpdv_loja01.txt')
    else:
        pass
    with open("relverpdv_loja01.txt", "w") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_101.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass

try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_102.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass    
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_103.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_129.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_105.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_106.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_107.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_108.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_109.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_110.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_111.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_112.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_113.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_114.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_115.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_116.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_117.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_118.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_119.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_120.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_121.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_122.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
try:
    with open("relverpdv_loja01.txt", "a") as stream:
        for line in open('C:\REMARCA\lojas\lj01.verpdv_123.txt'):
            print((line.rstrip()), file=stream)
except FileNotFoundError:
    pass
    
'''