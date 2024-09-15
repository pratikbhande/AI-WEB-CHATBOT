import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_openai

# Streamlit UI
st.title("AI Web Chatbot")
url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        try:
            # Scrape the website
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the cleaned DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

            # Display the DOM content in an expandable text box
            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)
        except Exception as e:
            st.error(f"Error during scraping: {e}")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            try:
                # Parse the content with OpenAI
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_openai(dom_chunks, parse_description)

                # Display the parsed result
                st.write("Parsed Result:")
                st.write(parsed_result)
            except Exception as e:
                st.error(f"Error during parsing: {e}")
