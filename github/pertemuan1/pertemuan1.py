import time
mulai_waktu = time.time()
print("Menghitung (Jumlah Perhitungan)")
h = raw_input("Masukan angka h : ")
e = raw_input("Masukan angka e : ")
r = raw_input("masukan angka r : ")
l = raw_input("Masukan angka l : ")
n = raw_input("Masukan angka n : ")
if h == 'satu':
	h=1
if h == 'dua':
	h=2
if h == 'tiga':
	h=3
if h == 'empat':
	h=4
if h == 'lima':
	h=5
if h == 'enam':
	h=6
if h == 'tujuh':
	h=7
if h == 'delapan':
	h=8
if h == 'sembilan':
	h=9
if h == 'nol':
	h=0

if e == 'satu':
	e=1
if e == 'dua':
	e=2
if e == 'tiga':
	e=3
if e == 'empat':
	e=4
if e == 'lima':
	e=5
if e == 'enam':
	e=6
if e == 'tujuh':
	e=7
if e == 'delapan':
	e=8
if e == 'sembilan':
	e=9
if e == 'nol':
	e=0

if r == 'satu':
	r=1
if r == 'dua':
	r=2
if r == 'tiga':
	r=3
if r == 'empat':
	r=4
if r == 'lima':
	r=5
if r == 'enam':
	r=6
if r == 'tujuh':
	r=7
if r == 'delapan':
	r=8
if r == 'sembilan':
	r=9
if r == 'nol':
	r=0

if l == 'satu':
	l=1
if l == 'dua':
	l=2
if l == 'tiga':
	l=3
if l == 'empat':
	l=4
if l == 'lima':
	l=5
if l == 'enam':
	l=6
if l == 'tujuh':
	l=7
if l == 'delapan':
	l=8
if l == 'sembilan':
	l=9
if l == 'nol':
	l=0

if n == 'satu':
	n=1
if n == 'dua':
	n=2
if n == 'tiga':
	n=3
if n == 'empat':
	n=4
if n == 'lima':
	n=5
if n == 'enam':
	n=6
if n == 'tujuh':
	n=7
if n == 'delapan':
	n=8
if n == 'sembilan':
	n=9
if n == 'nol':
	n=0
Jumlah = (h*e)/((r-l)+n)
print("Jumlah Perhitungan", Jumlah)
print("Waktu Menghitung : %s detik " % (time.time() - mulai_waktu))