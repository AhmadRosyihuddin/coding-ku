// import 'dart:io';

void main(List<String> arguments) {
  // stdout.write('Masukkan Suhu Farenheit : ');
  // var farenheit = int.parse(stdin.readLineSync()!);
  // var konversi = (farenheit - 32) * 5 / 9;
  // print('Koneversi Suhu dari $farenheit F Ke Celcius Adalah = $konversi C');
  // print(average(2, 2));
  // greetNewUser(age: 2, isVerified: true);
  var isAvailableForDiscount = true;
  var price = 300000;
  var discount = 0;
  if (isAvailableForDiscount) {
    discount = 50000;
  }
  print('You need to pay: ${price - discount}');
}

String average(num num1, num num2) => ((num1 + num2) ~/ 2).toString();

void greetNewUser({String? name, int? age, required bool? isVerified}) {
  print('$name $age $isVerified');
}
