from __future__ import annotations
from abc import ABC, abstractmethod


global_parent_hello = "抽象クラスのstaticメソッドから呼び出したHELLOです"
global_child_hello = "具象クラスのstaticメソッドから呼び出したHELLOです"


# pythonでは抽象クラスは抽象クラスのベースクラス(ABC)を継承する事で定義できる
class Parent(ABC):
  def __init__(self, parent_str) -> None:
    print("抽象クラスのコンストラクタ実行")
    # __でPrivateを疑似的に実装できるが外部から"_Parent__parent_str"でアクセスできてしまう
    # (Pythonのインタプリンタが変数名を自動で変更してるだけ)
    self.__parent_str = parent_str

  # 抽象インスタンスメソッド
  @abstractmethod
  def get_my_str(self) -> str:
    pass
  
  @staticmethod
  def get_parent_hello():
    print(global_parent_hello)

  # private変数のgetterメソッド
  def get_parent_private_str(self):
    return self.__parent_str
  
  def get_parent_private_message(self):
    return self.__private_message

  # 抽象インスタンス変数 型注釈が必要
  # private
  __child_private_str: str
  # public
  child_public_str: str
  
  # クラス変数
  class_str = "どのクラスからでも参照できるクラス変数です。getter使わなくてもアクセスできます。"
  __private_message = "プライベートなクラス変数です。getterを使用して下さい"

class Child(Parent):
  # 子クラスのコンストラクタ
  def __init__(self, publick_str, private_str) -> None:
    # 親クラスのコンストラクタを呼び出す
    super().__init__("抽象クラスのコンストラクタで設定されたPrivateな変数です")
    self.child_public_str = publick_str
    self.__child_private_str = private_str

  # インスタンスメソッドのオーバーライド
  def get_my_str(self):
    return self.__child_private_str
  
  # 静的メソッドはインスタンス変数にはアクセスできない(selfを引数に渡せない)
  @staticmethod
  def get_child_hello():
    print(global_child_hello)



child = Child("子クラスのprivateなインスタンス変数に設定されたメッセージです", "子クラスのインスタンス変数に設定された文字です")

# 抽象クラスのクラス変数(親クラス(抽象クラス)に定義された共通変数)にアクセス
print(child.class_str)

# 抽象クラスのprivate変数へ継承したgetterを使用してアクセス
print(child.get_parent_private_str()) 
print(child.get_parent_private_message()) 

# 自動で変更されたインスタンス変数名を指定すればgetterを使用せず無理やりアクセスできる
print(child._Parent__parent_str) # type: ignore

# staticメソッドの実行
child.get_parent_hello()
child.get_child_hello()