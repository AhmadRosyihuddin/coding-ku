class Animal {
  String _name = '';
  int _age = 0;
  double _weight = 0;

  Animal(this._name, this._age, this._weight);
  Animal.name(this._name);
  Animal.age(this._age);
  set nama(String value) {
    _name = value;
  }

  String get weight => _name;

  void eat() {
    print('$_name is eating.');
    _weight = _weight + 0.2;
  }

  void sleep() {
    print('$_name is sleeping.');
  }

  void poop() {
    print('$_name is pooping.');
    _weight = _weight - 0.1;
  }
}

class Sayur {
  String _sayur = '';
  Sayur.nama(this._sayur);
  set sayur(String value) {
    _sayur = value;
  }

  String get nama => _sayur;
}
