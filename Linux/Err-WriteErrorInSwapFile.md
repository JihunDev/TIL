# Write error in swap file

## Error

```
E297: Write error in swap file
E303: Unable to open swap file for "filename"recovery impossible
```

- Swap File을 사용불가

- 디스크가 꽉차서 사용할수없는 상태

  

## 해결

불필요한 파일을 삭제



```shell
 $ df     
```

파일 시스템의 사용률 확인



```shell
$ rm
```

rm 이용하여 불필요한 화일들을 삭제  



```shell
$ rm -f -r *.gz    
```

끝에 확장자가 .gz인 모든 화일을 찾아서 삭제할지 여부를 묻지 않고 일괄 삭제 함