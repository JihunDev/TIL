# RaspberryPi 3 B+

## 모니터 없이 Pi 접속

1. SD카드 boot폴더 접속
2. wpa_supplicant.conf 생성
3. SSH 생성
4. wpa_supplicant.conf에 Code 작성

```c
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
	ssid="SSID NAME"
	psk="Password"
	key_mgmt=WPA-PSK
}
```

5. 공유기에서 RaspberryPi ip확인후 SSH 이용하여 접속
6. 초기 ID : pi, PW: raspberry
