
class Visible:
    def __init__(self,name) -> None:
        self.name = name
        self.is_visible = True

    def delete(self):
        self.is_visible = False

class Bar(Visible):
    def __init__(self,name,weight):
        super.__init__(self,name)
        self.weight = weight
        self.decrease_speed = 0 #バーの減少する速度

    def change_size(self):
        #バーの見た目の長さを減らす
        self.bar -= self.decrease_speed

    def calc_decrease_speed(self):
        #バーの長さが減る速さを求めて設定する。
        return

class Button(Visible):
    def __init__(self,name,type):
        super.__init__(self,name)
        self.type = type

    def push(self):
        #ボタンが押されて時のアニメーションなどをどこに書こうか
        return

class Model:
    def __init__(self,view):
        self.visibles = []
        self.remain_time
        self.view = view

    def update(self):
        #毎秒呼び出すような処理（どのくらいの頻度で呼び出すかは割と重要）
        for v in self.visibles[:]:
            self.view.draw(v)

            if v.is_visible == False:
                self.visibles.remove(v)