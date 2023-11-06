<div align=center>
    <h1>Happy Number</h1>
    <p>Weekly Coding Challenge <b>advanced-oct-07-2023</b></p>
</div>

## Permasalahan

Tulislah algoritma untuk menentukan apakah suatu bilangan n **bahagia**.

Angka **bahagia** adalah angka yang ditentukan oleh proses berikut:

- Dimulai dengan bilangan bulat positif apa pun, ganti bilangan tersebut dengan jumlah kuadrat angka-angkanya.
- Ulangi proses ini sampai angkanya sama dengan 1 (di mana angka tersebut akan tetap ada), atau angka tersebut berputar tanpa henti dalam siklus yang tidak menyertakan 1.
- Angka-angka yang proses ini berakhir dengan 1 adalah angka-angka bahagia.

return `true` jika n adalah angka **bahagia**, dan `false` jika tidak.

## Input

Input yang diberikan hanya memiliki tipe data integer untuk `n`

## Output

Output yang diharapkan akan seperti berikut:

`Input:`

`19`

`Output:`

`true`

`Penjelasan`

```
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

## Kriteria Penilaian

- Nilai Testing peserta akan disortir secara DESC
- Dokumentasi kode yang baik
- Memberikan penjelasan mandiri mengenai Time Complexity dan Space Complexity yang diimplementasikan pada solusi yang diberikan
