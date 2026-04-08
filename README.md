Step 1: search papers
Step 2: extract 5 URLs
Step 3: download all PDFs
Step 4: extract text
Step 5: analyze each paper
Step 6: merge into literature review


# 1. LLM init
chat_generator = ...

# 2. search tool
def web_search(...)

# 3. download tool
def download_pdf(...)

# 4. PDF text extraction
def extract_pdf_text(...)

# 5. 🧠 THIS GOES HERE
def analyze_paper(...)

# 6. pipeline tool
def process_paper(...)

# 7. agent
agent = ToolCallingAgent(...)
✅ Tool-Calling Agent
kann Tools aufrufen
hat web_search
hat process_paper
hat add
✅ RAG Pipeline für Papers
web_search → PDF download → text extraction → LLM analysis


True

ChatMessage(_role=<ChatRole.USER: 'user'>, _content=[TextContent(text='Find papers about agentic AI and download them')], _name=None, _meta={})
ChatMessage(_role=<ChatRole.ASSISTANT: 'assistant'>, _content=[ReasoningContent(reasoning_text='The user wants papers about agentic AI and download them. According to the workflow: 1) call web_search first. 2) Then call download_from_search. 3) Then produce final answer.\n\nWe need to search for papers about agentic AI. Use web_search. Then download PDFs from the search results. The tool is download_pdfs_from_page. We need to provide the URL. We need to call web_search with query "agentic AI papers". Then download PDFs from the search result. But we need to specify the URL of the page containing PDFs. We might need to search for each paper individually. But the workflow says: "download_from_search(search_result)". The tool is download_pdfs_from_page, which takes a URL. So we need to provide a URL that contains PDFs. We could search for "agentic AI" and get a Google Scholar result page. But we need to download PDFs from that page. The tool might download all PDFs from that page. But we need to provide the URL of the page. So we can search for "agentic AI" and get a search result page. Then call download_pdfs_from_page with that URL. That might download PDFs from that page. But we need to ensure we provide a URL that contains PDFs. For example, a Google Scholar search result page. But the tool might not support Google Scholar. We could use arXiv search. For example, search for "agentic AI" on arXiv. Then download PDFs from that page. But we need to provide a URL that contains PDFs. We could use the arXiv search results page. But the tool might not be able to download from that page. Alternatively, we could search for "agentic AI pdf" and get a page that contains PDF links. Then download from that page.\n\nWe need to produce final answer after downloading. The final answer should include the list of downloaded PDFs. We need to provide the PDFs? The user wants to download them. We can provide the PDFs as attachments? The tool might return the PDFs. But we need to produce final answer. The final answer might include the PDF files or links. But the instructions: "Only then produce final answer." So we need to produce final answer after downloading. The final answer might list the titles and authors of the papers and maybe provide the PDF files or links.\n\nWe need to call web_search first. Then call download_pdfs_from_page. Then produce final answer.\n\nLet\'s do web_search with query "agentic AI papers".', extra={}), ToolCall(tool_name='web_search', arguments={'query': 'agentic AI papers'}, id=None, extra=None)], _name=None, _meta={'model': 'gpt-oss:20b', 'done': True, 'total_duration': 22479843300, 'load_duration': 3374149900, 'prompt_eval_duration': 112122600, 'eval_duration': 18263707100, 'logprobs': None, 'finish_reason': 'stop', 'completion_start_time': '2026-04-08T09:48:57.0855966Z', 'usage': {'completion_tokens': 542, 'prompt_tokens': 189, 'total_tokens': 731}})
ChatMessage(_role=<ChatRole.TOOL: 'tool'>, _content=[ToolCallResult(result="{'papers': [{'title': '[2510.25445] Agentic AI: A Comprehensive Survey of Architectures ...', 'url': 'https://arxiv.org/abs/2510.25445'}, {'title': 'Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and ...', 'url': 'https://arxiv.org/html/2601.12560v1'}, {'title': 'Efficient and Scalable Agentic AI with Heterogeneous Systems - arXiv', 'url': 'https://arxiv.org/abs/2507.19635'}, {'title': '[2507.21206] Agentic Web: Weaving the Next Web with AI Agents', 'url': 'https://arxiv.org/abs/2507.21206'}, {'title': 'Securing Agentic AI: A Comprehensive Threat Model and Mitigation ...', 'url': 'https://arxiv.org/abs/2504.19956'}]}", origin=ToolCall(tool_name='web_search', arguments={'query': 'agentic AI papers'}, id=None, extra=None), error=False)], _name=None, _meta={})
ChatMessage(_role=<ChatRole.ASSISTANT: 'assistant'>, _content=[ReasoningContent(reasoning_text='We have a list of papers. We need to download them. We need to call download_pdfs_from_page with a URL. But the tool expects a URL that contains PDFs. We could use the arXiv abstract page, but that page doesn\'t contain the PDF link directly? Actually, arXiv abstract page has a PDF link. But the tool might download all PDFs from that page. We can call download_pdfs_from_page for each URL. But the workflow says "download_from_search(search_result)". The search result is the list of papers. But the tool expects a URL. We might need to call download_pdfs_from_page for each URL. But the workflow says "Only then produce final answer". So we need to call download_pdfs_from_page for each paper. Let\'s do that.\n\nWe need to call download_pdfs_from_page for each URL. Let\'s do for the first paper: https://arxiv.org/abs/2510.25445. Then for the second: https://arxiv.org/html/2601.12560v1. But that is an HTML page, not PDF. But we can get the PDF link from that page. But the tool might not handle that. We can use the PDF link: https://arxiv.org/pdf/2601.12560v1.pdf. But the tool expects a URL that contains PDFs. So we can provide the PDF link directly. But the tool might download the PDF. Let\'s try for each paper.\n\nWe need to call download_pdfs_from_page for each PDF link. Let\'s do for each.\n\nBut the tool expects a URL that contains PDFs. We can provide the PDF link directly. Let\'s do that.\n\nWe\'ll call download_pdfs_from_page for each PDF link.\n\nLet\'s do for the first paper: https://arxiv.org/pdf/2510.25445.pdf\n\nSecond: https://arxiv.org/pdf/2601.12560v1.pdf\n\nThird: https://arxiv.org/pdf/2507.19635.pdf\n\nFourth: https://arxiv.org/pdf/2507.21206.pdf\n\nFifth: https://arxiv.org/pdf/2504.19956.pdf\n\nLet\'s call download_pdfs_from_page for each.', extra={}), ToolCall(tool_name='download_pdfs_from_page', arguments={'url': 'https://arxiv.org/pdf/2510.25445.pdf'}, id=None, extra=None)], _name=None, _meta={'model': 'gpt-oss:20b', 'done': True, 'total_duration': 17614325600, 'load_duration': 125195200, 'prompt_eval_duration': 166376800, 'eval_duration': 16744924700, 'logprobs': None, 'finish_reason': 'stop', 'completion_start_time': '2026-04-08T09:49:15.4094162Z', 'usage': {'completion_tokens': 491, 'prompt_tokens': 942, 'total_tokens': 1433}}) instraction   are very important I had chanched tool name, but didnt change it in instruction and Agent dont know what to do  instructions: str = """
You are an autonomous research agent.

TOOLS:
- web_search(query)
- download_from_search(search_result)

WORKFLOW:
1. Always call web_search first
2. Then call download_from_search
3. Only then produce final answer

"""
download_pdfs_from_page("https://arxiv.org/pdf/2510.25445.pdf")
that function expects an HTML page
NOT a direct PDF URL
You need to separate responsibilities:
web_search(query) -> search_result
extract_pdf_links(search_result) -> pdf_urls
download_pdf(url)
LLM ↔ tools ↔ LLM ↔ tools … until goal is satisfied
1. web_search (ONCE)
        ↓
2. extract PDF links
        ↓
3. download ALL PDFs (ONCE)
        ↓
4. LOOP over local files:
       - load PDF
       - process / summarize / extract
       - refine insights
        ↓
5. final report
6. Manual pipeline for critical steps
Tool-calling for exploration steps
LLM → extract_pdf_links → download_pdfs
LLM decides everything
↓
web_search (Tavily)
↓
LLM reads results
↓
LLM directly calls download_pdfs(urls)
