# AutoHotKey

## 저장위치
C:\Users\Com\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

## CapsLock 한영전환

```c
capslock::

KeyWait,capslock

if A_TimeSinceThisHotkey >= 1000 ; in milliseconds.

SetCapsLockState, % (State:=!State) ? "On" : "Off"

else

Send, {vk15sc1F2}

return
```

 