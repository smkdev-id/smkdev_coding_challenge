<div align=center>
    <h1>Optimal Route Planner</h1>
    <p>Weekly Coding Challenge <b>advanced-dec-05-2023</b></p>
</div>

## Permasalahan

Anda diberikan daftar kota beserta koordinatnya `(x, y)` pada bidang 2D. Tulis program untuk mencari rute optimal yang mengunjungi semua kota tepat sekali dan kembali ke kota awal, dengan meminimalkan total jarak yang ditempuh

## Input

Masukan terdiri dari bilangan bulat N `(2 <= N <= 10)` yang mewakili jumlah kota, diikuti oleh N baris, masing-masing berisi dua bilangan bulat x dan y `(0 <= x, y <= 100)` yang mewakili koordinat sebuah kota.

Output yang diharapkan akan seperti berikut:

`Input:`

```
4
0 0
0 2
2 2
2 0
```

`Output:`

```
Output: Optimal Route: City 1 -> City 2 -> City 3 -> City 4 -> City 1
Total Distance: 8.0 units
```

**Penjelasan**: Rute optimal dalam kasus ini adalah persegi, mengunjungi setiap kota sekali dan kembali ke kota awal, dengan total jarak 8 unit.

## Kriteria Penilaian

- Nilai Testing peserta akan disortir secara DESC (tertinggi ke terendah)
- Dokumentasi kode yang baik, seperti:
  - TODO setiap baris kode solusi
  - Ringkas, namun tepat
  - Penjelasan mandiri mengenai Time Complexity dan Space Complexity yang diimplementasikan pada solusi yang diberikan
