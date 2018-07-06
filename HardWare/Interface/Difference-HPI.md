# HPI (Host Port Interface)



## HPI

- Host Processor 와 병렬로 데이터를 주고 받을 수있는 병렬포트
- DSP는 Slave로 동작하기 때문에 Data 전송을 주도 할 수 없음
- Host Processor는 DSP Processor의 동작에 최소한 영향을 주며 DSP Processor의 내부 및 외부 메모리 액세스 가능

### HPI Address register (HPIA)

- Host만 액세스
- Host가 액세스 하는 HPI RAM의 Address를 세트

### HPI Control register (HPIC)

- Host, C54x 쌍방 액세스
- HPI를 위한 제어 및 Status bit 포함

### HPI Data register (HPID)

- Host만 액세스
- Host는 이 register를 통해 HPI RAM에 액세스



## Host 에서 HPI 액세스 순서

1. HPIC (Control register)의 설정
2. HPIA (Address register)의 설정
3. HPID (Data register)경유에서 데이터의 read/write



## HPID 액세스 주의 사항

