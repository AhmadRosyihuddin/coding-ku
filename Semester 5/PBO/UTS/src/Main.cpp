#include <iostream>
using namespace std;

class Prodi
{
private:
    string kode, nama_prodi;

public:
    Prodi(string kode, string nama_prodi)
    {
        this->kode = kode;
        this->nama_prodi = nama_prodi;
    };
};

class Constructor
{
    // Enksapsulasi
private:
    string nama, nim, alamat;
    Prodi *pd;

public:
    // Default Constructor
    Constructor()
    {
        this->nama = "Ahmad Rosyihuddin";
        this->nim = "200411100126";
        this->alamat = "Gresik";
    };

    // User-Defined Consturctor
    Constructor(string nama, string nim, string alamat, Prodi *pd)
    {
        this->nama = nama;
        this->nim = nim;
        this->alamat = alamat;
    };
    // Destructor
    ~Constructor();

    string getNama()
    {
        return this->nama;
    };
};

// Inheritance
class Matkul : Constructor
{
public:
    string kode, nama_matkul;
    Matkul(string kode, string nama_matkul)
    {
        this->kode = kode;
        this->nama_matkul = nama_matkul;
    };
};

// Polymorpishm 
class Fakultas
{
public:
    string namaFak;
    void getData()
    {
        cout << "FAKULTAS TEKNIK" << endl;
    }
};
class Prodi : public Fakultas
{
public:
    string namaPro;
    void getData()
    {
        cout << "TEKNIK INFORMATIKA" << endl;
    }
};

int main(int argc, char const *argv[])
{
    Prodi pd = Prodi("TIF", "TEKNIK INFORMATIKA");
    Constructor mhs = Constructor("Ahmad Rosyihuddin", "200411100126", "Gresik", &pd);
    cout << mhs.getNama() << endl;

    return 0;
}
