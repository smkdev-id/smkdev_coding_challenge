<div align=center>
    <h1>Happy Number</h1>
    <p>Weekly Coding Challenge <b>advanced-oct-07-2023</b></p>
</div>

## Permasalahan

Lingkaran angka terinisiasi pada suatu kotak dengan kolom dan baris tak terhingga dan berisi angka dengan kotak kiri atasnya mempunyai angka 1. Berikut adalah lima lapisan spiral pertama:

![Number Spiral](https://cses.fi/file/bba36f2601b99c7edc15865aa2a49e680a271075f30e86aa0e4e18d00a779c21)

Tugas kamu adalah menemukan angka yang tepat pada baris `y` dan kolom `x`.

## Input

Baris input pertama berisi bilangan bulat `t`: jumlah input.

Setelah ini, ada `t` baris, masing-masing berisi bilangan bulat `y` dan `x` yang mewakili masing-masing baris dan kolom.

## Output

Untuk setiap tes, cetak nomor yang berada pada baris `y` dan kolom `x` pada setiap input pada `t` baris. Contoh output yang diharapkan akan sebagai berikut:

`Input:`

```
3
2 3
1 1
4 2
```

`Output:`

```
8
1
15
```

## Kriteria Penilaian

- Nilai Testing peserta akan disortir secara DESC (tertinggi ke terendah)
- Dokumentasi kode yang baik, seperti:
  - TODO setiap baris kode solusi
  - Ringkas, namun tepat
  - Penjelasan mandiri mengenai Time Complexity dan Space Complexity yang diimplementasikan pada solusi yang diberikan
