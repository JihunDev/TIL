# Application Installation Failed

## Error 코드

Application Installation Failed

Installation Failed since the device possibly has stale dexed jars that don’t match the current version (dexopt error).
In order to proceed, you have to uninstall the existing application.

WARNING: Uninstalling will remove the application data!

Do you want to uninstall the existing application?

## Error 상황

- TensorFlow Lite 사용중
- AVD에 App Install 중 Err발생


## 해결 방법

1. Build Clean & Rebuild
   1. 상단 Build - Clean Project
   2. 상단 Build - Rebuild Project
2. VDB Wipe
   1. VDB 종료후 VDB 메니져에서 wipe data 클릭



## 참조

[Stack overflow](https://stackoverflow.com/questions/42219784/installation-failed-with-message-invalid-file/42226014#42226014)