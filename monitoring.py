Basic Configuration
enable
configure terminal
hostname SW1
service password-encryption
enable secret encisco
no ip domain-lookup
ip domain-name digitalent.com
banner motd #AUTHORIZED ACCESS ONLY#
crypto key generate rsa general-keys modulus 1024
username admin secret sshcisco
ip ssh ver 2
line console 0
password linecisco
login
exec-time 4
line vty 0 15
transport input ssh
exec-time 4
login local
exit
ip routing
ip default-gateway 10.10.10.113

VLAN
vlan 10
name Mahasiswa
vlan 20
name Dosen
vlan 60
name Management
vlan 99
name native

Konfigurasi IP vlan 
interface vlan 10
desc vlan mahasiswa
ip address 10.10.10.1 255.255.255.192
no sh
interface vlan 20
desc vlan dosen
ip address 10.10.10.65 255.255.255.240
no sh
interface vlan 60
desc vlan Management
ip address 10.10.10.81 255.255.255.240
no sh
interface vlan 99
desc native
ip address 10.10.10.97 255.255.255.240
no sh

konfigurasi interface dan switchport
interface g1/0/1 
desc Tersambung ke R1
no switchport
ip address 10.10.10.114 255.255.255.252
no sh
interface g1/0/2
desc tersambung ke SW2
switchport mode trunk
switchport non
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,60,99

interface range gigabitEthernet 1/0/3-10,  g1/0/14-24, g1/1/1-4
switchport mode access
switchport non
desc tidak digunakan
sh

interface range g1/0/11-12
switchport mode access
switchport non
switchport access vlan 10
interface g1/0/13
switchport mode access
switchport non
switchport access vlan 20

Routing OSPF
router ospf 1
network 10.10.10.112 0.0.0.3 area 0
network 10.10.10.0 0.0.0.63 area 0
network 10.10.10.64 0.0.0.15 area 0
network 10.10.10.80 0.0.0.15 area 0
network 10.10.10.96 0.0.0.15 area 0

do copy run start

SW2 
Basic Configuration
enable
configure terminal
hostname SW2
service password-encryption
enable secret encisco
no ip domain-lookup
ip domain-name digitalent.com
banner motd #AUTHORIZED ACCESS ONLY#
crypto key generate rsa general-keys modulus 1024
username admin secret sshcisco
ip ssh ver 2
line console 0
password linecisco
login
exec-time 4
line vty 0 15
transport input ssh
exec-time 4
login local
exit
ip routing
ip default-gateway 10.10.10.117

VLAN
vlan 10
name Mahasiswa
vlan 20
name Dosen
vlan 60
name Management
vlan 99
name native

Konfigurasi IP vlan 
interface vlan 10
desc vlan mahasiswa
ip address 10.10.10.2 255.255.255.192
no sh
interface vlan 20
desc vlan dosen
ip address 10.10.10.66 255.255.255.240
no sh
interface vlan 60
desc vlan Management
ip address 10.10.10.82 255.255.255.240
no sh
interface vlan 99
desc native
ip address 10.10.10.98 255.255.255.240
no sh

konfigurasi interface dan switchport
interface g1/0/1 
desc Tersambung ke R1
no switchport
ip address 10.10.10.118 255.255.255.252
no sh
interface g1/0/2
desc tersambung ke SW1
switchport mode trunk
switchport non
switchport trunk native vlan 99
switchport trunk allowed vlan 10,20,60,99

interface range gigabitEthernet 1/0/3-10,  g1/0/14-24, g1/1/1-4
desc tidak digunakan
switchport mode access
switchport non
sh

interface range g1/0/11-12
switchport mode access
switchport non
switchport access vlan 10
interface g1/0/13
switchport mode access
switchport non
switchport access vlan 20

Routing OSPF
router ospf 1
network 10.10.10.116 0.0.0.3 area 0
network 10.10.10.0 0.0.0.63 area 0
network 10.10.10.64 0.0.0.15 area 0
network 10.10.10.80 0.0.0.15 area 0
network 10.10.10.96 0.0.0.15 area 0

do copy run start