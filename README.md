# Capstone2

**Business Understanding**:

Latar Belakang:
Perusahaan AWS (Amazon Web Service) yang berfokus pada fitur SaaS adalah perusahaan yang menjual perangkat lunak penjualan dan pemasaran ke perusahaan lain (B2B). AWS SaaS menyediakan berbagai layanan untuk mendukung pengembangan dan implementasi perangkat lunak, termasuk AWS Lambda (komputasi tanpa server), Amazon S3 (penyimpanan objek), Amazon RDS (basis data manajemen hubungan), dan banyak lagi. 

Pernyataan Masalah:
Sebuah Perusahaan AWS ingin mengetahui **tren penjualan perusahaan dari waktu ke waktu**. Analisis tren penjualan dan profitabilitas adalah salah satu analisis data yang paling penting bagi sebuah perusahaan. Analisis ini dapat memberikan wawasan tentang kinerja penjualan dan pemasaran perusahaan, serta mengetahui produk dan layanan apa yang paling menguntungkan atau bahkan mengalami kerugian. Informasi ini dapat membantu untuk memahami bagaimana kinerja perusahaan telah berkembang selama periode waktu tertentu, dan membantu menentukan langkah selanjutnya dalam melakukan strategi pemasaran dan penjualan.

1. Berapa persentase profit yang berasal dari produk atau layanan tertentu?
2. Produk apa yang menghasilkan profit paling rendah atau bahkan mengalami kerugian?
3. Produk apa yang menghasilkan profit paling tinggi?
4. Bagaimana tren penjualan dan profitabilitas perusahaan pada periode waktu tertentu?
5. Bagaimana pengaruh diskon terhadap profit yang dihasilkan?

Tujuan:
1. Mengetahui persentase profit yang berasal dari produk atau layanan tertentu.
2. Mengetahui produk yang menghasilkan profit paling rendah.
3. Mengetahui produk yang menghasilkan profit paling tinggi.
4. Mengetahui tren penjualan dan profitabilitas perusahaan pada periode waktu tertentu.
5. Mengetahui seberapa besar pengaruh diskon terhadap profit.

Stakeholders: Stakeholder dalam analisis ini adalah manajer dan eksekutif di AWS SaaS yang bertanggung jawab atas strategi operasional.

Pendekatan Analisis:
Langkah pertama dalam analisis ini adalah memeriksa dataset untuk mengidentifikasi karakteristik penting dari daftar yang memainkan peran penting dalam menentukan harga, keuntungan, dan jumlah diskon yang diberikan oleh AWS SaaS. Kami akan menganalisis data secara deskriptif untuk mendapatkan pemahaman dasar, diikuti dengan analisis statistik inferensial untuk mengidentifikasi pola dan hubungan. Berdasarkan analisis ini, kami akan mengembangkan rekomendasi untuk membantu AWS SaaS membuat keputusan yang lebih tepat dalam menentukan strategi penjualan.

Evaluasi Metrik:
Untuk mengevaluasi keberhasilan analisis ini, kami akan menggunakan metrik sebagai berikut:

1. Akurasi dalam mengidentifikasi transaksi yang mengalami kerugian.
2. Dampak potensial dari rekomendasi terhadap peningkatan profit dan penurunan kerugian.


### README for AWS SaaS Capstone Project 2

---

#### Gambaran Umum
Proyek ini melakukan analisis data yang komprehensif pada layanan SaaS di platform AWS. Tujuan kami adalah mengekstrak wawasan yang berarti dari kumpulan data untuk membantu perusahaan dan penyedia layanan SaaS dalam membuat keputusan strategis. Dengan memahami faktor-faktor yang memengaruhi penjualan dan keuntungan secara keseluruhan, proyek ini berupaya mengoptimalkan strategi pemasaran, mengurangi kerugian, dan pada akhirnya meningkatkan penjualan dan keuntungan AWS SaaS.

---

#### Fitur-fitur Utama:

- **Business Understanding**: Mendalami konteks dan permasalahan yang dihadapi oleh AWS SaaS, menentukan tujuan dan langkah analisis.
- **Descriptive Statistical Analysis**: Memeriksa dataset untuk mengidentifikasi profit yang bernilai negaif / kerugian dan hubungannya dengan nilai diskon.
- **Factors Influencing Performance**: Mengidentifikasi dan menganalisis variabel yang memengaruhi keuntungan perusahaan.
- **Recommendation Development**: Berdasarkan analisis, merumuskan rekomendasi yang dapat ditindaklanjuti oleh AWS SaaS untuk meningkatkan profit mereka.
- **Stakeholder Focus**: Menyesuaikan wawasan dan rekomendasi dengan kebutuhan tim pemasaran dan tim bisnis perusahaan.

---

#### Teknologi yang Digunakan:

- **Python**: Primary language for data analysis and manipulation.
- **Pandas**: For efficient data processing and manipulation.
- **Matplotlib and Seaborn**: Visualizing data and uncovering trends.
- **Jupyter Notebook**: Interactive development environment used for the analysis.
- **Numpy**: Used for numerical operations and array manipulations.
- **Tabulate**: Utilized for presenting data in table formats.
- **Scipy**: Employed for scientific computations, including the Anderson-Darling test for statistical analysis.


---

#### Hasil Utama:

- **Pengaruh Harga dan Diskon**: Menunjukkan bagaimana diskon yang berlaku dapat mempengaruhi jumlah keuntungan.
- **Strategi Penetapan keuntungan Optimal**: Memberikan wawasan tentang faktor-faktor yang mempengaruhi keuntungan.
- **Rekomendasi Diskon**: Menawarkan saran yang dapat ditindaklanjuti dalam melakukan strategi diskon
- **Pemahaman Dinamika Keuntungan**: Menunjukkan dinamika keuntungan, membantu perencanaan strategis.

---

#### Saran:

- **Penyesuaian Harga Diskon**: Menyesuaikan harga diskon pada produk-produk tertentu yang mengalami kerugian.
- **Menentukan Harga Dinamis**: Menerapkan harga dinamis, dengan memanfaatkan wawasan dari analisis data.
- **Analisis Pasar Berkelanjutan**: Memperbarui analisis secara teratur untuk mengikuti perubahan kondisi dan tren pasar.
- **Keterlibatan Pemangku Kepentingan**: Menjaga komunikasi aktif dengan para pemangku kepentingan untuk memastikan analisis sesuai dengan kebutuhan AWS SaaS yang terus berkembang.

---

#### Cara Menjalankan Proyek

1. Pastikan aplikasi yang dibutuhkan sudah di-install.
2. Clone project repository ke device Anda.
3. Buka Jupyter Notebook dan buka directory yang sudah di-clone.
4. Buka notebook `Capstone Project 2.ipynb` untuk melihat analisis dan hasilnya.

