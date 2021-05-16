import pyautogui as pgui
import time
import platform
def beep(freq, dur=100):
    """
        ビープ音を鳴らす.
        @param freq 周波数
        @param dur  継続時間（ms）
    """
    if platform.system() == "Windows":
        # Windowsの場合は、winsoundというPython標準ライブラリを使います.
        import winsound
        winsound.Beep(freq, dur)
    else:
        # Macの場合には、Macに標準インストールされたplayコマンドを使います.
        import os
        os.system('play -n synth %s sin %s' % (dur/1000, freq))

#画像の認識で判定
while pgui.locateOnScreen('NGshot.png' , confidence=0.9) is None:
    time.sleep(1)
#座標を取得
position=pgui.locateOnScreen('NGshot.png' , confidence=0.9)
beep(2000,2000)