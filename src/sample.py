from __future__ import annotations
from abc import ABC, abstractmethod


class Product():
  def __init__(self) -> None:
    print("インスタンス化しました")


global_string = "グローバルなHELLO"

class Program():
  def __init__(self) -> None:
    self.int = 10
    self.str = "hello"
    
  # インスタンスメソッド
  def get_int(self) -> int:
    return "hello"
  
  # 静的メソッド
  @staticmethod
  def get_str_static() -> int:
    return global_string


number = Program().get_str_static()

print(number)
