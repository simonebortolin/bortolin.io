"""Terminal infographics for the ONT firmware article.

Every output line is real command output, collected on 19-22 November 2026
from the Hack GPON wiki, the kernel's vulns.git repository and firmware
dumps of the devices. Text is in Italian, like the article.
"""

POST = "2026-11-24-ont-gpon-xgs-pon-firmware-kernel-obsoleti-peter-pon"

INFOGRAPHICS = [
    dict(
        name="ont-kernel-2009",
        title="Dentro i firmware delle ONT in fibra c'è un kernel del 2009.",
        subtitle="Firmware compilati nel 2025 e nel 2026, sopra kernel e compilatori di quindici anni fa.",
        blocks=[
            ("FS ONU1710-1G · stick GPON Realtek · log di avvio",
             '$ grep "Linux version" fs-com-onu1710-1g/bootlog.txt\n'
             'Linux version [[2.6.30.9]] (root@svn-onu) ([[gcc version 4.4.6]] (Realtek RSDK-1.5.6p2) ) #1 [[Thu Mar 20 17:00:24 CST 2025]] 10.0.52B.2095_FS'),
            ("Zyxel PMG3000-D20B · stick GPON Lantiq · versioni firmware",
             '$ grep -o "OpenWrt 12.09 (kernel [0-9.]*)" ont-zyxel-pmg3000-d20b.md\n'
             '[[OpenWrt 12.09 (kernel 3.10.12)]]\n'
             '$ grep -A3 "ABVJ.1) (OpenWrt 12.09" ont-zyxel-pmg3000-d20b.md\n'
             '- V1.00(ABVJ.1) (OpenWrt 12.09, without ssh)\n'
             '  - V1.00(ABVJ.1)b1e (2023-07-26)\n'
             '  - V1.00(ABVJ.1)b1i ([[2026-02-06]])\n'
             '  - V1.00(ABVJ.1)b1j ([[2026-05-27]])'),
        ],
        sources=["Dati: Hack GPON, log di avvio", "e pagine dei dispositivi"],
    ),
    dict(
        name="ont-cve-rami",
        title="Le ONT girano su rami del kernel che nessuno corregge più.",
        subtitle="CVE del kernel ancora aperte sull'ultima versione di ogni ramo, secondo i dati ufficiali del kernel.",
        blocks=[
            # Produced with scripts/kernel-cves/cve_open.py on vulns.git.
            ("Repository vulns.git del kernel · dati al 19 novembre 2026",
             '$ python3 cve_open.py published/ 2.6.30.9 3.10.108 3.18.140 \\\n'
             '      4.4.302 4.14.333 5.10.274 6.18.64\n'
             '2.6.30.9     [[1430]]   {{← Luna SDK 1.9 · ramo chiuso dal 2009}}\n'
             '3.10.108     [[2897]]   {{← FALC ON · fine supporto 2017}}\n'
             '3.18.140     [[3544]]   {{← Luna SDK 3.3 · fine supporto 2019}}\n'
             '4.4.302      [[4041]]   {{← Saturn SDK (XGS-PON) · fine 2022}}\n'
             '4.14.333     [[4587]]   {{← XGS-PON · fine supporto 2024}}\n'
             '5.10.274     2187   {{← XGS-PON · supportato fino a dic. 2026}}\n'
             '6.18.64       112   {{← Peter Pon · ramo mantenuto}}'),
        ],
        sources=["Dati: git.kernel.org, linux/security/vulns.git",
                 "Conteggio sull'intero codice del kernel.",
                 "In blu le annotazioni, non output."],
    ),
    dict(
        name="ont-tim-iliad-afm0003",
        title="Una ONT di TIM e una di Iliad: firmware fino al 2023, componenti del 2008-2011.",
        subtitle="Vantiva AFM0003, stick GPON Realtek, nelle varianti distribuite da TIM e da Iliad. Rootfs letti senza eseguire nulla; in entrambi due script sono modificati dalla community, il resto è originale.",
        blocks=[
            ("Modello e versione del firmware",
             '$ grep -ao "AFM0003[A-Z]*" */bin/configd\n'
             'iliad/bin/configd:[[AFM0003ILD]]\n'
             'tim/bin/configd:[[AFM0003]]\n'
             '$ grep . */etc/version\n'
             'iliad/etc/version:V1.7.6_230105 --  [[Wed Jan 18 09:56:00 CST 2023]]\n'
             'tim/etc/version:V1_7_8_220201 --  [[Tue Feb 1 15:30:17 CST 2022]]'),
            ("Kernel, BusyBox, libreria C",
             '$ grep -ao "vermagic=[^ ]*" */lib/modules/omcidrv.ko\n'
             'iliad/lib/modules/omcidrv.ko:vermagic=[[2.6.30.9]]\n'
             'tim/lib/modules/omcidrv.ko:vermagic=[[2.6.30.9]]   {{← giugno 2009}}\n'
             '$ grep -ao "BusyBox v[0-9.]*" */bin/busybox\n'
             'iliad/bin/busybox:BusyBox [[v1.12.4]]\n'
             'tim/bin/busybox:BusyBox [[v1.12.4]]   {{← dicembre 2008}}\n'
             '$ ls */lib/libuClibc-*\n'
             'iliad/lib/libuClibc-[[0.9.30.3]].so\n'
             'tim/lib/libuClibc-[[0.9.30.3]].so   {{← marzo 2010}}'),
            ("Servizi di rete",
             '$ grep telnet */etc/inetd.conf\n'
             'iliad/etc/inetd.conf:telnet  stream tcp nowait [[root /bin/telnetd]]\n'
             'tim/etc/inetd.conf:telnet  stream tcp nowait [[root /bin/telnetd]]'),
        ],
        sources=["Dati: dump dei rootfs (SquashFS), estratti",
                 "con unsquashfs. Date: kernel.org, busybox.net,",
                 "uclibc.org. In blu le annotazioni, non output."],
    ),
    dict(
        name="ont-ma5671a-stock",
        title="Il firmware di serie del MA5671A: un 2016 fermo al 2014.",
        subtitle="Huawei MA5671A, stick GPON Lantiq FALC ON. Partizione image0 (SFP_7.5.3), CRC dell'immagine verificati, letta senza eseguire nulla.",
        blocks=[
            ("Kernel",
             '$ strings kernel.bin | grep "Linux version"\n'
             'Linux version [[3.10.49]] (jack@GPON-DEV) (gcc version 4.8.3 (OpenWrt/Linaro GCC 4.8-2014.04 [[14.07_ltq]]) ) #1 [[Tue Oct 25 17:24:32 CST 2016]]'),
            ("BusyBox, libreria C, SSH",
             '$ strings bin/busybox | grep -E "BusyBox v[0-9]"\n'
             'BusyBox [[v1.22.1]] (2016-10-25 17:19:46 CST)   {{← gennaio 2014}}\n'
             '$ ls lib | grep "uClibc-"\n'
             'ld-uClibc-[[0.9.33.2]].so   {{← maggio 2012}}\n'
             'libuClibc-0.9.33.2.so\n'
             '$ strings usr/sbin/dropbear | grep -m1 "SSH-2.0"\n'
             'SSH-2.0-[[dropbear_2016.73]]   {{← marzo 2016}}'),
            ("Algoritmi offerti dal server SSH",
             '$ strings usr/sbin/dropbear | grep -E "^(diffie-hellman|ssh-(rsa|dss)|3des-)"\n'
             'diffie-hellman-group14-sha1\n'
             '[[diffie-hellman-group1-sha1]]\n'
             'ssh-rsa\n'
             '[[ssh-dss]]\n'
             '3des-ctr\n'
             '[[3des-cbc]]'),
        ],
        sources=["Dati: dump della partizione image0.",
                 "Date: busybox.net, uclibc.org,",
                 "matt.ucc.asn.au. In blu le annotazioni."],
    ),
]
