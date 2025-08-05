# import streamlit as st
# import httpx

# st.set_page_config(page_title="🧠 Medical Chatbot", layout="centered")
# st.markdown("<h1 style='text-align: center;'>💬 PubMed Chatbot</h1>", unsafe_allow_html=True)

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "last_response" not in st.session_state:
#     st.session_state.last_response = {}

# # ⬆️ Chat input at top
# with st.container():
#     prompt = st.chat_input("Ask your question from PubMed...")

# # Tabs for chat & references
# tab1, tab2 = st.tabs(["💬 Chat", "📚 References"])

# with tab1:
#     # Show previous messages
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"], unsafe_allow_html=True)

#     # Process input if any
#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.chat_message("assistant"):
#             with st.spinner("🔍 Searching..."):
#                 try:
#                     response = httpx.get(
#                         "http://127.0.0.1:8000/api/summarize",
#                         params={"q": prompt},
#                         headers={"accept": "application/json"},
#                         timeout=200.0
#                     )
#                     response.raise_for_status()
#                     data = response.json()

#                     summary = data.get("summary", "No summary available.")
#                     references = data.get("Reference_links", [])

#                     # Save last result for reference tab
#                     st.session_state.last_response = {
#                         "summary": summary,
#                         "references": references
#                     }

#                     # Show summary
#                     st.markdown("### 📝 Summary")
#                     st.markdown(summary)

#                     # Append to chat history
#                     st.session_state.messages.append({
#                         "role": "assistant",
#                         "content": f"### 📝 Summary\n{summary}\n\n📚 {len(references)} reference(s) listed."
#                     })

#                 except Exception as e:
#                     st.error(f"❌ Failed to fetch: {e}")
#                     st.session_state.messages.append({
#                         "role": "assistant",
#                         "content": f"❌ Error: {e}"
#                     })

# with tab2:
#     references = st.session_state.last_response.get("references", [])
#     if references:
#         st.markdown("### 📚 All References")
#         for i, ref in enumerate(references, 1):
#             title = ref.get("title", f"Reference {i}")
#             abstract = ref.get("abstract", "No abstract available.")
#             links = []

#             # Collect links
#             if "link" in ref:
#                 links.append(ref["link"])
#             if "reference" in ref:
#                 links += [
#                     {"link": r.get("link"), "Name": r.get("Reference")}
#                     for r in ref["reference"] if r.get("link")
#                 ]

#             with st.expander(f"{i}. {title}"):
#                 st.markdown(f"**🧾 Abstract:** {abstract}")
#                 if links:
#                     for j in links:
#                         if isinstance(j, str):
#                             st.markdown(f"🔗 [Link]({j})")
#                         else:
#                             st.markdown(f"🔗 [{j['Name']}]({j['link']})")
#                 else:
#                     st.markdown("🔗 No links available.")
#     else:
#         st.info("No references to display yet. Ask something in the Chat tab.")


# import streamlit as st
# import httpx

# st.set_page_config(page_title="🔍 PubMed Search Engine", layout="centered")
# st.markdown("<h1 style='text-align: center;'>🔍 PubMed Search Engine</h1>", unsafe_allow_html=True)

# # Initialize session state variables only once
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "last_response" not in st.session_state:
#     st.session_state.last_response = {}

# if "last_prompt" not in st.session_state:
#     st.session_state.last_prompt = None

# # Chat input stays on top
# with st.container():
#      user_input = st.chat_input("Ask your question from PubMed...")

# # Tabs for Chat and References
# tab1, tab2 = st.tabs(["💬 Chat", "📚 References"])

# with tab1:
#     # Show previous messages
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"], unsafe_allow_html=True)

#     # Handle new user input only if changed
#     if user_input and user_input != st.session_state.last_prompt:
#         st.session_state.last_prompt = user_input
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         with st.chat_message("assistant"):
#             with st.spinner("🔍 Searching..."):
#                 try:
#                     response = httpx.get(
#                         "http://127.0.0.1:8000/api/summarize",
#                         params={"UserQuery": user_input},
#                         headers={"accept": "application/json"},
#                         timeout=200.0
#                     )
#                     response.raise_for_status()
#                     data = response.json()

#                     summary = data.get("summary", "No summary available.")
#                     references = data.get("Reference_links", [])

#                     # Save data for references tab
#                     st.session_state.last_response = {
#                         "summary": summary,
#                         "references": references
#                     }

#                     # Display summary
#                     st.markdown("### 📝 Summary")
#                     st.markdown(summary)

#                     # Add to chat history
#                     st.session_state.messages.append({
#                         "role": "assistant",
#                         "content": f"### 📝 Summary\n{summary}\n\n📚 {len(references)} reference(s) listed."
#                     })

#                 except Exception as e:
#                     st.error(f"❌ Failed to fetch: {e}")
#                     st.session_state.messages.append({
#                         "role": "assistant",
#                         "content": f"❌ Error: {e}"
#                     })

# with tab2:
#     references = st.session_state.last_response.get("references", [])
#     if references:
#         st.markdown("### 📚 All References")
#         for i, ref in enumerate(references, 1):
#             title = ref.get("title", f"Reference {i}")
#             abstract = ref.get("abstract", "No abstract available.")
#             links = []

#             # Collect all link formats
#             if "link" in ref:
#                 links.append(ref["link"])
#             if "reference" in ref:
#                 links += [
#                     {"link": r.get("link"), "Name": r.get("Reference")}
#                     for r in ref["reference"] if r.get("link")
#                 ]

#             with st.expander(f"{i}. {title}"):
#                 st.markdown(f"**🧾 Abstract:** {abstract}")
#                 if links:
#                     for j in links:
#                         if isinstance(j, str):
#                             st.markdown(f"🔗 [Link]({j})")
#                         else:
#                             st.markdown(f"🔗 [{j['Name']}]({j['link']})")
#                 else:
#                     st.markdown("🔗 No links available.")
#     else:
#         st.info("No references to display yet. Ask something in the Chat tab.")

import streamlit as st
import httpx

# Configure page
st.set_page_config(page_title="🔍 PubMed Search Engine", layout="centered")
st.markdown("<h1 style='text-align: center;'>🔍 PubMed Search Engine</h1>", unsafe_allow_html=True)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response" not in st.session_state:
    st.session_state.last_response = {}
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None
if "search_count" not in st.session_state:
    st.session_state.search_count = 0

# Chat input stays on top
with st.container():
    user_input = st.chat_input("Ask your question from PubMed...")

# Handle new user input
if user_input and user_input != st.session_state.last_prompt:
    # Clear previous results if this is a new search
    if st.session_state.search_count > 0:
        st.session_state.messages = []
    
    st.session_state.last_prompt = user_input
    st.session_state.search_count += 1
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Process the query
    with st.spinner("🔍 Searching PubMed..."):
        try:
            response = httpx.get(
                "http://127.0.0.1:8000/api/summarize",
                # "http://127.0.0.1:8000/api/summarize/test",
                params={"UserQuery": user_input},
                headers={"accept": "application/json"},
                timeout=200.0
            )
            response.raise_for_status()
            data = response.json()

            summary = data.get("summary", "No summary available.")
            references = data.get("Reference_links", [])

            # Save data for references tab
            st.session_state.last_response = {
                "summary": summary,
                "references": references
            }
            # Add assistant response to history
            if data.get("Status")==404:
               st.session_state.messages.append({
                "role": "assistant",
                "content": f"### No Article's Found \n{summary}\n\n📚 {len(references)} reference(s) found."
                })
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"### 📝 Summary\n{summary}\n\n📚 {len(references)} reference(s) found."
                })

        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"❌ Error: Failed to fetch results - {str(e)}"
            })

# Tabs for Chat and References
tab1, tab2 = st.tabs(["ALL", "📚 References"])

with tab1:
    # Display current conversation (only showing the current search)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"], unsafe_allow_html=True)

with tab2:
    references = st.session_state.last_response.get("references", [])
    if references:
        st.markdown("### 📚 Articles Found")
        st.markdown(f"Showing references for: *{st.session_state.last_prompt}*")
        
        for i, ref in enumerate(references, 1):
            title = ref.get("title", f"Reference {i}")
            abstract = ref.get("abstract", "No abstract available.")
            links = []

            # Collect all link formats
            # if "link" in ref:
            #     links.append({"link":ref["link"],"Name":"PubMed Link"})

            # if "Similar_articles" in ref:
            #     links += [{"link":ref["Similar_articles"],"Name" : "Similar articles"}]
            if "reference" in ref:
                links += [
                    {"link": r.get("link"), "Name": r.get("Reference")}
                    for r in ref["reference"] if r.get("link")
                ]
            

            with st.expander(f"{i}. {title}"):
                st.markdown(f"📅 **Published:** `{ref['published_date']}` | 🔄 **Updated:** `{ref['last_updated']}`")
                st.markdown(f"**Abstract:** {abstract}")
                authors = ref.get("author", [])
                if authors:
                   author_list = ", ".join(authors)
                   st.markdown(f"**👨‍🔬 Authors:** {author_list}")
                   if "link" in ref:
                       st.link_button("🔗 PubMed Link", ref["link"])
                   if "Similar_articles" in ref:
                       st.link_button("🧬 Similar Articles", ref["Similar_articles"])
                # if links:
                #     st.markdown("**Links:**")
                #     for j in links:
                #         # if isinstance(j, str):
                #         #     st.markdown(f"- [PubMed Link]({j})")
                #         # else:
                #         st.markdown(f"- [{j['Name']}]({j['link']})")
                if links:
                    with st.expander("🔗 References"):
                        for j in links:
                            # st.markdown(f"- [{j['Name']}]({j['link']})")
                            st.link_button(f"{j['Name']}", f"{j['link']}")
                else:
                    st.markdown("No links available for this reference.")
    else:
        if st.session_state.last_prompt:
            st.info("No references found for your last query.")
        else:
            st.info("Submit a query in the Chat tab to see references here.")
