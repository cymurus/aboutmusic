## About Music
  一些乐理上常用的功能

* #### tuner.py
  调音用，也可以获取计算特定的音程

        tuner('C', -2) # => 'A#'，将 C 降 2 度
        perfect_4th('C#') # => 'F#'，计算 C# 的纯四度  
        minor_3rd('D') # => 'F'，计算 D 的小三度
* #### chord.py
  输出和弦

        输出 Cmaj7和弦
        $ python chord.py CM7
        >> C E G B
        输出 Em和弦
        $ python chorder.py Em
        >> E G B
* #### scale.py
  输出音阶

        输出 D小调音阶
        $ python scale.py Dm
        >> B C# D E F# G A
* #### to_qwerty.py
  将音名转化为 qwert y键盘按键

        TODO