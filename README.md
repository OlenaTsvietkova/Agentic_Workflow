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
