biodata1 = {f'Nama' : 'Endang',
            'Umur' : 59,
            'Pekerjaan' : 'Ibu Rumah Tangga',
            'Golongan' : 'Tidak Mampu',
            'Pendapatan' : 500000
           }
biodata2 = {f'Nama' : 'Siroh',
            'Umur' : 61,
            'Pekerjaan' : 'Pedagang',
            'Golongan' : 'Tidak Mampu',
            'Pendapatan' : 2500000,
           }
biodata3 = {f'Nama' : 'Gocip',
            'Umur' : 55,
            'Pekerjaan' : 'Purna PNS',
            'Golongan' : 'Mampu',
            'Pendapatan' : 1700000,
          }
biodata4 = {f'Nama' : 'Udin',
            'Umur' : 70,
            'Pekerjaan' : 'Kuli',
            'Golongan' : 'Tidak Mampu',
            'Pendapatan' : 400000,
           }
biodata5 = {f'Nama' : 'Waridi',
            'Umur' : 75,
            'Pekerjaan' : 'Wiraswasta',
            'Golongan' : 'Tidak Mampu',
            'Pendapatan' : 450000,
            }

nama = str(input('Masukan Nama : '))
umur = int(input('Masukan Umur :'))
pekerjaan = str(input('Masukan Pekerjaan :'))
golongan = str(input('Masukan Golongan : '))
pendapatan = int(input('Masukan Jumlah Pendapatan : '))
mampu = False
tidak_mampu = True
pekerjaan_yang_tidak_mendapatkan_bantuan = {'wiraswasta','pedagang','purna_pns'}

if (umur >= 60) and (pekerjaan not in pekerjaan_yang_tidak_mendapatkan_bantuan) and mampu or tidak_mampu and (pendapatan <= 1000000):
    hasil = ('Mendapatkan Distribusi Umroh')
else:
    hasil = ('Tidak Mendapatkan Distribusi Umroh')

print('Nama : ', nama)
print('Umur : ', umur)
print('Pekerjaan : ', pekerjaan)
print('Golongan : ', golongan)
print('Pendapatan : ', pendapatan)
print('Klasifikasi : ', hasil)