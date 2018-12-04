# wiringPi

[WiringPi]([https://github.com/WiringPi/WiringPi](https://github.com/WiringPi/WiringPi))

## wiringPi 설치
```shell
    $ sudo apt-get install git-core
    $ git clone git://git.drogon.net/wiringPi
    $ cd wiringPi
    $ ./bulid
    $ gpio -v  #버전 확인
    $ gpio readall #gpio pin header 확인
```
## wiringPi 컴파일 및 실행방법
```shell
    $ gcc -o [실행 파일명] [파일명].c -lwiringPi
    $ sudo ./[실행파일명]
```
## wiringPi 예제
```shell
    $ cd wiringPi/example
    $ make [예제파일명]
    $ sudo ./[실행파일명]
```
- Uart를 사용하는 실행파일은 관리자 권한이 필요하여 sudo으로 실행
