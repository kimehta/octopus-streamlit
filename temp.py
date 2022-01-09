import streamlit as st

st.text("""steps to reproduce
1. click b0 & b1 to ensure both b0_expander & b1_expander are collapsed
2. click b0 & expand b0_expander
3. click b1
4. b1_expander should be collapsed but is expanded.

5. same issue with expanding b1_expander before b0_expander
""")

b0 = st.button("b0")
b1 = st.button("b1")

if b0:
    with st.expander("b0_expander", expanded=False):
        st.write("b0_write")

if b1:
    with st.expander("b1_expander", expanded=False):
        st.write("b1_write")