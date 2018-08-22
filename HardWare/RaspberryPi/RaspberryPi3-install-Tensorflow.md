# RaspberryPi 3 B+ install Tensorflow

## Version
- Board Raspberry Pi3 B+
- OS 2018-06-27-raspbian-stretch-lite
- Python 3.5.2

## install

### Raspbian Update
```shell
$ sudo apt-get update
$ sudo apt-get upgrade -y
```

### Compile lib install
```shell
$ sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
$ sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
$ sudo apt-get install libssl-dev openssl
```

### Python3.5 Download, Comaplie and install
```shell
$ cd /home/pi/
$ mkdir temppython
$ cd temppython
$ wget "https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz"
$ tar xvf Python-3.5.2.tgz
$ cd Python-3.5.2
$ ./configure
$ make
$ sudo make install
```

### pip install
```shell
$ sudo apt-get install python3-pip
$ pip3 -V
```

### Altas install
- 선형 대수 라이브러리 
- numpy 의존성
```shell
$ sudo apt install libalas-base-dev
```

### Tensorflow install
```shell
$ pip3 intall tensorflow
```
