<div align=center>
    <h1>Grid Paths</h1>
    <p>Weekly Coding Challenge <b>advanced-oct-14-2023</b></p>
</div>

## Permasalahan

Pertimbangkan sebuah kotak dengan ukuran `n * n` yang kotaknya mungkin memiliki jebakan(disini akan disimbolkan sebagai `#`). Dan kamu tidak diperbolehkan pindah ke kotak yang ada jebakan.

Tugas kamu adalah menghitung jumlah jalur yang memungkinkan dari kotak kiri atas ke kotak kanan bawah. Kamu hanya bisa bergerak ke kanan atau ke bawah.

## Input

Baris input pertama memiliki bilangan bulat `n`: sebagai informasi dari ukuran kotak tersebut.

Setelahnya, ada `n` baris yang menggambarkan kotak tersebut. Setiap `n` baris memiliki karakter `.` menunjukkan sel kosong, dan `#` menunjukkan jebakan.

## Output

Cetak jumlah jalur optimal yang dapat dilakukan. Contoh output akan seperti berikut:

`Input:`

```
4
....
.*..
...*
*...
```

`Output:`

`3`

## Kriteria Penilaian

- Nilai Testing peserta akan disortir secara DESC (tertinggi ke terendah)
- Dokumentasi kode yang baik, seperti:
  - TODO setiap baris kode solusi
  - Ringkas, namun tepat
  - Penjelasan mandiri mengenai Time Complexity dan Space Complexity yang diimplementasikan pada solusi yang diberikan
