# Message Queue 사이즈 업그레이드

## 현재 Message Queue 사이즈
```shell
# sysctl -a | grep kernel.msg

kernel.msgmax=8192 (최대 허용 크기)
kernel.msgmni=16 (최대 허용 Queue 갯수)
kernel.msgmnb=16384 (Queue당 최대 허용크기)
```

## Message Queue 사이즈 변경
```shell
# sysctl -w kernel.msgmax=2097152
# sysctl -w kernel.msgmnb=1048576
```

설정 파일에 저장
```shell
# vi /etc/sysctl.conf

(하단에 추가)
kernel.msgmax=65536
kernel.msgmnb=1048576
```
