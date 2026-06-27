import glob
for f in glob.glob('*.html'):
    if f == 'laporan_barang_masuk_admin.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace(
        '<a href="#" class="nav-link">Laporan Barang Masuk</a>',
        '<a href="laporan_barang_masuk_admin.html" class="nav-link">Laporan Barang Masuk</a>'
    )
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    else:
        print(f"No change in {f}")
