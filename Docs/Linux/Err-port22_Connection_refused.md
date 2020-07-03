# ERR port 22: Connection refused 

## Error Code
``` shell
$ port 22: Connection refused 
```

## Solution
- 아래 명령어로 ssh 서버를 설치 후 22번 포트를 sshd를 위해 사용하도록 허락

``` shell
$ sudo apt-get update
$ sudo apt-get install openssh-server
$ sudo ufw allow 22
```
