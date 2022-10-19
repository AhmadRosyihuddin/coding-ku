void main(List<String> args) {
  var x = 5;

  x = 7;

// x--;
  print(x);
}

void penjumlahan(int? angka1, int? angka2) {
  if (angka1 != null && angka2 != null) {
    print(angka1 + angka2);
  } else {
    print('Else');
  }
}
