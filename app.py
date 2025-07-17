import streamlit as st
import requests
import os

    
def coletaDados(searchPokemon):
    source = "https://pokeapi.co/api/v2/pokemon"
    url = f"{source}/{searchPokemon}"

    try:    
        response = requests.get(url)

        response.raise_for_status()
        data = response.json()

        # st.write(data)
        st.image(data['sprites']['front_default'])
        st.write(f'|   Nome: {data["name"].capitalize()}')
        st.write(f'|   Número da Pokédex: {data['id']}')
        st.write(f'|   Habilidade: {data['abilities'][0]['ability']['name'].capitalize()}')
        if len(data['abilities']) > 1:
            for i in range(1, len(data['abilities'])):
                st.write(f'|   Habilidade: {data['abilities'][i]['ability']['name'].capitalize()}')
        st.write(f'|   Tipo: {data['types'][0]['type']['name'].capitalize()}')
        if len(data['types']) > 1:
            st.write(f'|   Tipo: {data['types'][1]['type']['name'].capitalize()}')
        st.write(f"|    HP: {data['stats'][0]['base_stat']}")
        st.write(f"|    Ataque: {data['stats'][1]['base_stat']}")
        st.write(f"|    Defesa: {data['stats'][2]['base_stat']}")
        st.write(f"|    Ataque Especial: {data['stats'][3]['base_stat']}")
        st.write(f"|    Defesa Especial: {data['stats'][4]['base_stat']}")
        st.write(f"|    Velocidade: {data['stats'][5]['base_stat']}")

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao coletar dados: {e}")
        return None
    except ValueError as e:
        st.error(f"Erro ao decodificar JSON: {e}")
        return None

def clearSearch():
    st.session_state["searchBar"] = ""

st.title("Pokédex do Fujita")
st.divider()

col1, col2 = st.columns(2)

with col1:
    searchBar = st.text_input("Pesquisar", type="default", placeholder="Pikachu", icon=":material/chevron_right:", key="searchBar")

with col2:
    searchButton = st.button("Pesquisar", icon=":material/search:")
    clearButton = st.button("Limpar", icon=":material/clear:", on_click=clearSearch)

st.divider()

if searchButton:
    coletaDados(searchBar)