import streamlit as st

# Kolom input
IHCP_2022 = st.slider('IHCP Tahun 2022', min_value=1, max_value=300, value=150)
IHCP_2023 = st.slider('IHCP Tahun 2023', min_value=1, max_value=300, value=160)

# Rumus Inflasi
Inflasi = ((IHCP_2023 - IHCP_2022) / IHCP_2022) * 100

# Rumus Deflasi
Deflasi = ((IHCP_2022 - IHCP_2023) / IHCP_2022) * 100

# Tampilkan hasil menggunakan Streamlit
st.title('Perhitungan Tingkat Inflasi dan Deflasi')
st.write(f'Terdapat tingkat inflasi sebesar {Inflasi:.2f}%, menunjukkan kenaikan harga umum dari tahun 2022 ke tahun 2023.')
st.write(f'Terdapat tingkat deflasi sebesar {Deflasi:.2f}%, menunjukkan potensi penurunan harga umum dari tahun 2022 ke tahun 2023.')
