from foo import target

'''
TODO
- 3つ縦か横に同じ色がそろうと消える
- 消えた後は空間になり、上から落ちてくる
- 一番上の空間には、ランダムに画面外から落ちてくる
- 移動できる制限時間は4秒間
- ドロップを指で掴んで動かせる
- ドロップはタテヨコ斜めに動かせる
- 動かした先のドロップと入れ替わる
- 指を離すと移動がおわる
- 移動が終わると消える
- ドロップは横6列縦5行
- 初期状態はドロップはランダム
- ドロップは5色＋ハートの6種類
'''

def test_func_42():
    assert target.func_42() == 42
