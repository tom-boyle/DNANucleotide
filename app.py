import pandas as pd
import streamlit as st
import altair as alt

st.write("""
# DNA Nucleotide Count

This app counts the nucleotide composition of query DNA.

***
""")

st.header('Enter DNA sequence')

sequence_input = """
TCATAAGACTAAAGAAACCAGGATATGCCCACATCATGCAGCACCTTCAGCGGGTAACTC
AAGAGTACAAGAAGTGTCGTATCGCATCTGAGTATTGGTTCTCAGAAAGCCGAGAGGAAC
ACAGTCGGAAGAACATAGCTGTGGGAAATAACACTAGAAACTGTAACTTGATATAAGGCA
TATATACCAAACAACGACTCCCCCGAAGAATTGTACGCAACACTCGAACGTTAGAGTATC
TTCAAGTTGT
"""

sequence = st.text_area("Sequence input", sequence_input, height=250)

st.write("""
***
""")

#Print the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

#DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X

st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + 'Adenine (A)')
st.write('There are ' + str(X['T']) + 'Thymine (T)')
st.write('There are ' + str(X['G']) + 'Adenine (Guanine)')
st.write('There are ' + str(X['C']) + 'Thymine (Cytosine)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) # controls width of bars
)
st.write(p)
