# SSH root Login Access denied



리눅스의 보안 강화로 root권한 로그인이 회피됨



```
login as: root
root@~~~~~~~`s password:
Access denied
```

root 로그인시 Access denied가 발생



```shell
$ vi /etc/ssh/sshd_config

# PermitRootLogin의 옵션을 yes로변경
```



이후 

```shell
$ service ssh restart
```

