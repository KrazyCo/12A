import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel

class NumberConverter(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    
  def initUI(self):
    # Get the number and the base it is in
    num, ok = QInputDialog.getText(self, "Number Converter", "Enter a number:")
    if not ok:
      sys.exit()
    base, ok = QInputDialog.getText(self, "Number Converter", "Enter the base (binary, hex, or decimal):")
    if not ok:
      sys.exit()
    
    # Convert the base to lowercase
    base = base.lower()
    
    # Check the base and convert the number to decimal
    if base == "binary":
      num = int(num, 2)
    elif base == "hex":
      num = int(num, 16)
    elif base == "decimal":
      num = int(num)
    else:
      self.label = QLabel("Invalid base", self)
      self.label.move(50, 50)
      self.show()
      return
    
    # Output the number in the other two bases
    binary_str = ""
    while num > 0:
      binary_str = str(num % 2) + binary_str
      num = num // 2
    hex_str = ""
    hex_digits = "0123456789abcdef"
    original_num = num
    while original_num > 0:
      hex_str = hex_digits[original_num % 16] + hex_str
      original_num = original_num // 16
    self.label = QLabel("Binary: " + binary_str + "\nHexadecimal: " + hex_str, self)
    self.label.move(50, 50)
    self.show()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  converter = NumberConverter()
  sys.exit(app.exec_())
