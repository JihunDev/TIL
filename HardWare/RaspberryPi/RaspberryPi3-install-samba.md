# Samba

## install
```shell
$sudo apt-get install samba samba-common-bin
```

## 유저 및 비밀번호 생성

```shell
$ sudo sambapasswd -a pi
New SMB password:
Retype new SMB password:
Added user pi.
```

## samba 설정
```shell
$ sudo vi /etc/samba/smb.conf


[pi]
comment = Samba
path = /home/pi
valid user = pi
read only = no
browseable = yes
```

### 옵션
- read only : Samba사용 디렉토리를 읽기만 가능
- comment : 코멘트
- path : Samba사용 디렉토리 경로
- writable :쓰기 가능
- wirte list : 쓰기 허용할 계정 또는 유저 그룹
- create mask : 생성될 파일들 권한 수준
- diretory mask : 생성될 폴더 권한 수준

## 재실행
```shell
$ sudo service samba restart
```

### Trouble Shooting
#### Err Message
Failed to restart samba.service: Unit samba.service is masked.

```shell
$ sudo /etc/init.d/samba restart
```
