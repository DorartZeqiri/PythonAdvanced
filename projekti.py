import pandas as pd
import streamlit as st


FILE_NAME = "librat.csv"


def initialize_data():
    try:

        pd.read_csv(FILE_NAME)
    except FileNotFoundError:

        df = pd.DataFrame(columns=["ID", "Titulli", "Autori", "Viti", "Kopjet"])
        df.to_csv(FILE_NAME, index=False)


def load_data():
    return pd.read_csv(FILE_NAME)


def save_data(df):
    df.to_csv(FILE_NAME, index=False)


def shto_liber(titulli, autori, viti, kopjet):
    df = load_data()
    new_id = df["ID"].max() + 1 if not df.empty else 1
    new_book = {"ID": new_id, "Titulli": titulli, "Autori": autori, "Viti": viti, "Kopjet": kopjet}
    df = df.append(new_book, ignore_index=True)
    save_data(df)


def fshij_liber(book_id):
    df = load_data()
    df = df[df["ID"] != book_id]
    save_data(df)


def kerko_liber(keyword):
    df = load_data()
    return df[df["Titulli"].str.contains(keyword, case=False, na=False) |
              df["Autori"].str.contains(keyword, case=False, na=False)]

st.title("Menaxhimi i Librave")


initialize_data()


menu = st.sidebar.selectbox("Meny", ["Shfaq Librat", "Shto Libër", "Fshij Libër", "Kërko Libër"])


if menu == "Shfaq Librat":
    st.header("Lista e Librave")
    df = load_data()
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("Nuk ka libra të regjistruar.")


elif menu == "Shto Libër":
    st.header("Shto Libër")
    titulli = st.text_input("Titulli i librit")
    autori = st.text_input("Autori")
    viti = st.number_input("Viti i botimit", min_value=0, max_value=2100, step=1)
    kopjet = st.number_input("Numri i kopjeve", min_value=1, step=1)

    if st.button("Shto Libër"):
        if titulli and autori:
            shto_liber(titulli, autori, viti, kopjet)
            st.success("Libri u shtua me sukses!")
        else:
            st.error("Ju lutem plotësoni të gjitha fushat!")

# Funksionaliteti për fshirjen e një libri
elif menu == "Fshij Libër":
    st.header("Fshij Libër")
    df = load_data()
    if not df.empty:
        book_id = st.number_input("Shkruaj ID-në e librit", min_value=1, step=1)
        if st.button("Fshij Libër"):
            if book_id in df["ID"].values:
                fshij_liber(book_id)
                st.success("Libri u fshi me sukses!")
            else:
                st.error("ID nuk ekziston!")
    else:
        st.info("Nuk ka libra për të fshirë.")


elif menu == "Kërko Libër":
    st.header("Kërko Libër")
    keyword = st.text_input("Shkruaj titullin ose autorin")
    if st.button("Kërko"):
        if keyword:
            results = kerko_liber(keyword)
            if not results.empty:
                st.dataframe(results)
            else:
                st.warning("Nuk u gjet asnjë libër.")
        else:
            st.error("Ju lutem shkruani një fjalë kyç!")
