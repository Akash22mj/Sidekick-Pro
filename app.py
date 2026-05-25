# import gradio as gr
# from sidekick import Sidekick


# async def setup():
#     sidekick = Sidekick()
#     await sidekick.setup()
#     return sidekick


# async def process_message(sidekick, message, success_criteria, history):
#     results = await sidekick.run_superstep(message, success_criteria, history)
#     return results, sidekick


# async def reset():
#     new_sidekick = Sidekick()
#     await new_sidekick.setup()
#     return "", "", None, new_sidekick


# def free_resources(sidekick):
#     print("Cleaning up")
#     try:
#         if sidekick:
#             sidekick.cleanup()
#     except Exception as e:
#         print(f"Exception during cleanup: {e}")


# with gr.Blocks(title="Sidekick", theme=gr.themes.Default(primary_hue="emerald")) as ui:
#     gr.Markdown("## Sidekick Personal Co-Worker")
#     sidekick = gr.State(delete_callback=free_resources)

#     with gr.Row():
#         chatbot = gr.Chatbot(label="Sidekick", height=300, type="messages")
#     with gr.Group():
#         with gr.Row():
#             message = gr.Textbox(show_label=False, placeholder="Your request to the Sidekick")
#         with gr.Row():
#             success_criteria = gr.Textbox(
#                 show_label=False, placeholder="What are your success critiera?"
#             )
#     with gr.Row():
#         reset_button = gr.Button("Reset", variant="stop")
#         go_button = gr.Button("Go!", variant="primary")

#     ui.load(setup, [], [sidekick])
#     message.submit(
#         process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
#     )
#     success_criteria.submit(
#         process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
#     )
#     go_button.click(
#         process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
#     )
#     reset_button.click(reset, [], [message, success_criteria, chatbot, sidekick])


# ui.launch(inbrowser=True)





# Alternative one


# import gradio as gr
# from sidekick import Sidekick
# import os
# import time
# import glob

# # --- CORE LOGIC ---

# async def setup():
#     """Initializes the Sidekick agent and browser resources."""
#     sidekick_instance = Sidekick()
#     await sidekick_instance.setup()
#     return sidekick_instance

# async def process_message(sidekick_obj, message, success_criteria, history):
#     """Processes commands and captures files generated ONLY during this prompt."""
#     start_time = time.time() 
    
#     # Run the agent logic
#     results = await sidekick_obj.run_superstep(message, success_criteria, history)
    
#     # Filter sandbox: show ONLY files created during THIS specific request
#     all_files = glob.glob('sandbox/*')
#     current_task_files = [
#         f for f in all_files 
#         if os.path.getmtime(f) >= start_time
#     ]
#     current_task_files.sort(key=os.path.getmtime, reverse=True)
    
#     return results, sidekick_obj, current_task_files if current_task_files else None

# async def reset():
#     """Refreshes the AI session without deleting physical file history on disk."""
#     new_sidekick = Sidekick()
#     await new_sidekick.setup()
#     return "", "", [], new_sidekick, None

# def free_resources(sidekick_obj):
#     """Safely closes browser instances and clears memory on exit."""
#     print("System Shutdown: Releasing resources.")
#     try:
#         if sidekick_obj:
#             sidekick_obj.cleanup()
#     except Exception as e:
#         print(f"Exception during cleanup: {e}")

# # --- UI DESIGN ---

# custom_css = """
# #header { text-align: center; padding: 10px; border-bottom: 2px solid #10b981; margin-bottom: 15px; }
# #info-box { background-color: #ecfdf5; border-left: 5px solid #10b981; padding: 15px; margin-bottom: 20px; border-radius: 8px; }
# #timer-note { color: #b45309; font-weight: bold; margin-top: 10px; display: block; }
# """

# with gr.Blocks(title="Sidekick AI", theme=gr.themes.Default(primary_hue="emerald"), css=custom_css) as ui:
    
#     sidekick_state = gr.State(delete_callback=free_resources)

#     with gr.Row(elem_id="header"):
#         with gr.Column():
#             gr.Markdown("# 🛡️ SIDEKICK: Autonomous Intelligence Orchestrator")
#             gr.Markdown("### Professional AI Engineering Solution | Akash M J - 2026")

#     # PROFESSIONAL SYSTEM GUIDANCE
#     with gr.Row(elem_id="info-box"):
#         with gr.Column():
#             gr.Markdown("""
#             🚀 **Direct Web Navigation:** You can command the agent to visit any website directly. 
#             *Example: "Please take me to langchain.com"* — the agent will immediately navigate, analyze, and report back.
            
#             ⏳ <span id="timer-note">System Note: High-intelligence missions involve complex multi-agent reasoning and may take 2-3 minutes. Please do not refresh.</span>
#             """)

#     with gr.Row():
#         # LEFT COLUMN: Mission Control
#         with gr.Column(scale=3):
#             chatbot = gr.Chatbot(label="System Operational Feed", height=500, type="messages")
            
#             with gr.Group():
#                 message_input = gr.Textbox(
#                     label="Command Input",
#                     placeholder="Enter your strategic mission (e.g. Please take me to langchain.com and summarize it)",
#                     lines=2
#                 )
#                 criteria_input = gr.Textbox(
#                     label="Objective Definition",
#                     placeholder="Specify deliverables (e.g. .md report and .png visual verification...)"
#                 )
            
#             with gr.Row():
#                 reset_button = gr.Button("🔄 Reset Engine", variant="stop")
#                 go_button = gr.Button("🚀 Execute Mission", variant="primary")

#         # RIGHT COLUMN: Intelligence Center
#         with gr.Column(scale=2):
#             with gr.Tabs():
#                 with gr.TabItem("🛠️ Capabilities"):
#                     gr.Markdown("""
#                     ### **Active Toolsets**
#                     * **🛰️ Web Navigation:** Direct site access & analysis via Playwright.
#                     * **📸 Visual Capture:** High-res UI/UX screenshot engine.
#                     * **🎓 Academic Core:** ArXiv API scientific research.
#                     * **💻 GitHub Scout:** Technical repository & trend analysis.
#                     * **🗣️ Community Intel:** Reddit sentiment mapping.
#                     * **📂 Document Engine:** Professional Markdown (.md) reports.
#                     * **📺 Media Extraction:** YouTube technical content search.
#                     * **🔔 Secure Push:** Administrative alerts sent exclusively to **Akash M J**.
#                     """)

#                 with gr.TabItem("📋 Templates"):
#                     gr.Markdown("""
#                     ### **Operational Mission Templates**
#                     **1. 🛰️ Direct Navigation & Analysis**
#                     > "Please take me to the website of **langchain.com**. Analyze their latest feature announcement and capture a screenshot."

#                     **2. 🎓 Academic Deep-Dive (ArXiv + Admin Alert)**
#                     > "Research 2026 ArXiv papers on 'Agentic RAG'. Save findings to 'Research_Brief.md' and alert Akash via push."

#                     **3. 💻 GitHub & Sentiment Scouting**
#                     > "Scout GitHub for trending 'React AI' projects. Cross-reference Reddit for sentiment and save to 'Scout_Report.md'."
#                     """)

#                 with gr.TabItem("📂 Output Gallery"):
#                     file_output = gr.File(
#                         label="Mission Assets", 
#                         file_count="multiple", 
#                         interactive=False
#                     )
#                     gr.Markdown("*Assets from the latest command appear here.*")

#     # --- EVENT BINDING ---
#     ui.load(setup, [], [sidekick_state])
    
#     event_inputs = [sidekick_state, message_input, criteria_input, chatbot]
#     event_outputs = [chatbot, sidekick_state, file_output]

#     message_input.submit(process_message, event_inputs, event_outputs)
#     criteria_input.submit(process_message, event_inputs, event_outputs)
#     go_button.click(process_message, event_inputs, event_outputs)
#     reset_button.click(reset, [], [message_input, criteria_input, chatbot, sidekick_state, file_output])

# if __name__ == "__main__":
#     ui.launch(inbrowser=True)



# UI developeed working code

import gradio as gr
from sidekick import Sidekick
import os
import time
import glob
import subprocess


# --- ADD THIS AROUND LINE 40 ---
js_open_url = """
function(chat_history) {
    if (chat_history && chat_history.length > 0) {
        // Handle all possible Gradio data structures
        const lastTurn = chat_history[chat_history.length - 1];
        let content = "";
        
        // Extract content whether it's a message object or a tuple
        if (typeof lastTurn === 'object' && lastTurn !== null) {
            content = lastTurn.content || (Array.isArray(lastTurn) ? lastTurn[1] : "");
        }
        
        console.log("Checking for trigger in:", content); // Debugging
        
        if (content && content.includes("REDIRECT_TRIGGER:")) {
            const url = content.split("REDIRECT_TRIGGER:")[1].trim();
            console.log("Attempting to open:", url);
            
            // This is the physical trigger
            const win = window.open(url, '_blank');
            if (!win) {
                alert("Please ALLOW POP-UPS for this site to enable direct navigation!");
            }
        }
    }
    return chat_history;
}
"""

# --- Hugging Face Playwright Fix ---
try:
    # This command downloads the Chromium executable to the /root/.cache folder
    subprocess.run(["playwright", "install", "chromium"], check=True)
    # This command installs the system dependencies (libs) needed to run it
    subprocess.run(["playwright", "install-deps", "chromium"], check=True)
except Exception as e:
    print(f"Playwright setup skipped or handled by system: {e}")
# -----------------------------------
# ─────────────────────────────────────────
#  CORE LOGIC  (untouched)
# ─────────────────────────────────────────

async def setup():
    sidekick_instance = Sidekick()
    await sidekick_instance.setup()
    return sidekick_instance

async def process_message(sidekick_obj, message, success_criteria, history):
    start_time = time.time()
    results = await sidekick_obj.run_superstep(message, success_criteria, history)
    all_files = glob.glob('sandbox/*')
    current_task_files = [
        f for f in all_files
        if os.path.getmtime(f) >= start_time
    ]
    current_task_files.sort(key=os.path.getmtime, reverse=True)
    return results, sidekick_obj, current_task_files if current_task_files else None

async def reset():
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", [], new_sidekick, None

def free_resources(sidekick_obj):
    print("System Shutdown: Releasing resources.")
    try:
        if sidekick_obj:
            sidekick_obj.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")

# ─────────────────────────────────────────
#  CSS  — layout only, no Gradio internals
# ─────────────────────────────────────────

css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Force the container to handle the emerald aesthetic */
.gradio-container { background-color: #f8fafc !important; }

/* Custom Chatbot Styling */
#sk-chatbot { 
    height: 500px !important; 
    border: 2px solid #10b981 !important; 
    border-radius: 12px !important; 
    background: white !important;
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1) !important;
}

/* Header Styling */
#header { 
    text-align: center !important; 
    padding: 30px !important; 
    background: linear-gradient(135deg, #064e3b 0%, #10b981 100%) !important; 
    color: white !important; 
    border-radius: 12px !important; 
    margin-bottom: 25px !important; 
}

/* Template Cards */
.tpl-card { 
    background: white !important; 
    border: 1px solid #e5e7eb !important; 
    padding: 15px !important; 
    border-radius: 10px !important; 
    margin-bottom: 12px !important; 
    transition: all 0.2s ease !important;
}
.tpl-card:hover { 
    border-color: #10b981 !important; 
    box-shadow: 0 10px 15px -3px rgb(16 185 129 / 0.1) !important; 
    transform: translateY(-2px) !important;
}

body, .gradio-container {
    font-family: 'Inter', sans-serif !important;
    background: #f0f2f5 !important;
}
footer { display: none !important; }

/* ── Top bar ── */
#sk-topbar {
    background: #0d1f3c !important;
    padding: 7px 0 !important;
    text-align: center !important;
    border-radius: 0 !important;
}
#sk-topbar p {
    color: rgba(255,255,255,0.35) !important;
    font-size: 10px !important;
    font-weight: 500 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    margin: 0 !important;
}

/* ── Header ── */
#sk-header {
    background: #0d1f3c !important;
    padding: 22px 48px !important;
    border-radius: 0 !important;
    border-bottom: 1px solid rgba(255,255,255,0.07) !important;
}
#sk-brand p {
    font-size: 22px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin: 0 !important;
    letter-spacing: -0.3px !important;
}
#sk-byline p {
    font-size: 12px !important;
    color: rgba(255,255,255,0.38) !important;
    margin: 4px 0 0 !important;
}
#sk-online p {
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #34d399 !important;
    background: rgba(52,211,153,0.15) !important;
    border: 1px solid rgba(52,211,153,0.30) !important;
    border-radius: 100px !important;
    padding: 5px 16px !important;
    margin: 0 !important;
    text-align: right !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

/* ── Warning bar ── */
#sk-warn {
    background: #fffbeb !important;
    border-bottom: 1px solid #fde68a !important;
    padding: 10px 48px !important;
    border-radius: 0 !important;
}
#sk-warn p {
    font-size: 12.5px !important;
    color: #92400e !important;
    font-weight: 500 !important;
    margin: 0 !important;
}

/* ── Page body ── */
#sk-body {
    padding: 28px 48px 56px !important;
    background: #f0f2f5 !important;
    gap: 22px !important;
    align-items: flex-start !important;
}

/* ── Left panel card ── */
#sk-left-panel {
    background: #ffffff !important;
    border: 1px solid #e2e5ea !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    overflow: hidden !important;
}

/* ── Right panel card ── */
#sk-right-panel {
    background: #ffffff !important;
    border: 1px solid #e2e5ea !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    overflow: visible !important;
}

/* ── Section labels ── */
#feed-header p, #input-header p {
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: #9ca3af !important;
    margin: 0 !important;
    padding: 12px 20px !important;
    background: #f8f9fb !important;
    border-bottom: 1px solid #e2e5ea !important;
    display: block !important;
}

/* ── Input area ── */
#sk-inputs {
    padding: 18px 20px 20px !important;
}

/* ── Buttons ── */
#btn-execute {
    background: #0d1f3c !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 12px 20px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: background 0.15s !important;
}
#btn-execute:hover { background: #162d52 !important; }

#btn-reset {
    background: #ffffff !important;
    color: #374151 !important;
    border: 1.5px solid #d1d5db !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 12px 20px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.15s !important;
}
#btn-reset:hover {
    background: #f0f2f5 !important;
    border-color: #9ca3af !important;
}

/* ── Tabs: make all tab text visible ── */
#sk-right-panel .tab-nav button,
#sk-right-panel button[role="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #6b7280 !important;
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    border-radius: 0 !important;
    padding: 13px 18px !important;
}
#sk-right-panel .tab-nav button.selected,
#sk-right-panel button[role="tab"][aria-selected="true"] {
    color: #0d1f3c !important;
    border-bottom: 2px solid #0d1f3c !important;
    font-weight: 700 !important;
}
#sk-right-panel .tab-nav button:not(.selected),
#sk-right-panel button[role="tab"][aria-selected="false"] {
    color: #6b7280 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

/* Tab panel content background */
#sk-right-panel .tabitem,
#sk-right-panel [role="tabpanel"] {
    background: #ffffff !important;
}

/* ── Capability rows ── */
.cap-row {
    padding: 14px 20px !important;
    border-bottom: 1px solid #f3f4f6 !important;
    background: #ffffff !important;
}
.cap-row p {
    font-size: 13.5px !important;
    color: #374151 !important;
    margin: 0 !important;
    line-height: 1.55 !important;
}
.cap-row p strong {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* ── Template cards ── */
.tpl-card {
    margin: 14px 18px 0 !important;
    background: #f8f9fb !important;
    border: 1px solid #e2e5ea !important;
    border-left: 3px solid #0d1f3c !important;
    border-radius: 8px !important;
    padding: 14px 16px !important;
}
.tpl-card p {
    font-size: 13px !important;
    color: #374151 !important;
    margin: 0 !important;
    line-height: 1.6 !important;
}
.tpl-card p strong {
    display: block !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #9ca3af !important;
    margin-bottom: 5px !important;
}

.tpl-card { 
    background: #ffffff; 
    border: 1px solid #e5e7eb; 
    padding: 10px; 
    border-radius: 8px; 
    margin-bottom: 10px; 
}

/* ── File zone ── */
.file-zone {
    padding: 20px !important;
    background: #ffffff !important;
}
.file-zone p {
    font-size: 12.5px !important;
    color: #9ca3af !important;
    margin-top: 8px !important;
}

/* ── Footer ── */
#sk-footer {
    background: #ffffff !important;
    border-top: 1px solid #e2e5ea !important;
    padding: 18px 48px !important;
    border-radius: 0 !important;
    text-align: center !important;
}
#sk-footer p {
    font-size: 11.5px !important;
    color: #9ca3af !important;
    margin: 0 !important;
}
"""

# ─────────────────────────────────────────
#  THEME  — use Soft which forces light mode
# ─────────────────────────────────────────

theme = gr.themes.Soft(
    primary_hue="blue",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Inter"),
).set(
    body_background_fill="#f0f2f5",
    body_text_color="#111827",
    block_background_fill="#ffffff",
    block_border_color="#e2e5ea",
    block_border_width="1px",
    block_radius="10px",
    button_primary_background_fill="#0d1f3c",
    button_primary_text_color="#ffffff",
    button_secondary_background_fill="#ffffff",
    button_secondary_text_color="#374151",
    input_background_fill="#f8f9fb",
    input_border_color="#e2e5ea",
    input_border_width="1.5px",
    input_radius="8px",
)

# ─────────────────────────────────────────
#  UI LAYOUT
# ─────────────────────────────────────────

# with gr.Blocks(theme=theme, css=css, title="Sidekick AI") as ui:

# 1. Create the Blocks object with NO arguments
ui = gr.Blocks()

# Assign properties directly (The Gradio 6.0 way)
ui.css = css
ui.theme = theme
ui.title="Sidekick Pro"
ui.fill_height = True  # This makes it look like a full-screen dashboard

with ui:
    sidekick_state = gr.State(delete_callback=free_resources)

    # Top bar
    with gr.Row(elem_id="sk-topbar"):
        gr.Markdown("Sidekick Intelligence Platform · Authorized Personnel Only · All Sessions Monitored")

    # Header
    with gr.Row(elem_id="sk-header"):
        with gr.Column(scale=5):
            gr.Markdown("Sidekick", elem_id="sk-brand")
            gr.Markdown("Autonomous Intelligence Orchestrator &nbsp;·&nbsp; Akash M J — 2026", elem_id="sk-byline")
        with gr.Column(scale=1, min_width=160):
            gr.Markdown("● &nbsp; System Online", elem_id="sk-online")

    # Warning bar
    with gr.Row(elem_id="sk-warn"):
        gr.Markdown("⏳ High-intelligence missions involve multi-agent reasoning and may take 2–3 minutes. Do not refresh during execution.")

    # Main layout
    with gr.Row(elem_id="sk-body", equal_height=False):

        # LEFT — Chat + Inputs
        with gr.Column(scale=6, elem_id="sk-left-panel"):

            gr.Markdown("Operational Feed", elem_id="feed-header")

            chatbot = gr.Chatbot(
                label="",
                height=500,
                # type="messages",                
                elem_id="sk-chatbot",
                show_label=False,
                avatar_images=(None, "https://api.dicebear.com/7.x/bottts/svg?seed=Akash") # Optional: adds a pro bot icon
            )

            gr.Markdown("Mission Input", elem_id="input-header")

            with gr.Column(elem_id="sk-inputs"):
                message_input = gr.Textbox(
                    label="Command",
                    placeholder="e.g. Navigate to langchain.com and summarize their latest feature announcement",
                    lines=2,
                    show_label=True,
                )
                criteria_input = gr.Textbox(
                    label="Success Criteria",
                    placeholder="e.g. Deliver a .md report and .png screenshot as verification",
                    lines=1,
                    show_label=True,
                )
                with gr.Row():
                    reset_button = gr.Button("↺  Reset Session", elem_id="btn-reset")
                    go_button    = gr.Button("→  Execute Mission", variant="primary", elem_id="btn-execute")

        # RIGHT — Info panel
        with gr.Column(scale=4, elem_id="sk-right-panel"):

            with gr.Tabs():

                with gr.TabItem("Capabilities"):
                    gr.Markdown("**🛰 Web Navigation** — Direct site access & analysis via Playwright", elem_classes=["cap-row"])
                    gr.Markdown("**📸 Visual Capture** — High-resolution UI/UX screenshot engine", elem_classes=["cap-row"])
                    gr.Markdown("**🎓 Academic Core** — ArXiv API for scientific research retrieval", elem_classes=["cap-row"])
                    gr.Markdown("**💻 GitHub Scout** — Repository trend analysis & intelligence", elem_classes=["cap-row"])
                    gr.Markdown("**🗣 Community Intel** — Reddit sentiment mapping & analysis", elem_classes=["cap-row"])
                    gr.Markdown("**📂 Document Engine** — Structured Markdown report generation", elem_classes=["cap-row"])
                    gr.Markdown("**📺 Media Extraction** — YouTube content search & summarization", elem_classes=["cap-row"])
                    gr.Markdown("**🔔 Secure Push** — Encrypted alerts sent to Akash M J only", elem_classes=["cap-row"])

                # with gr.TabItem("Templates"):
                #     gr.Markdown("**🛰 Navigation & Analysis**\nNavigate to langchain.com, analyze their latest feature and capture a screenshot.", elem_classes=["tpl-card"])
                #     gr.Markdown("**🎓 Academic Deep-Dive**\nResearch 2026 ArXiv papers on Agentic RAG. Save to Research_Brief.md and alert Akash.", elem_classes=["tpl-card"])
                #     gr.Markdown("**💻 GitHub & Sentiment Scout**\nScout GitHub for trending React AI projects, cross-reference Reddit, save to Scout_Report.md.", elem_classes=["tpl-card"])
                #     gr.Markdown("")

                with gr.TabItem("📋 Strategic Templates"):
                    # gr.Markdown("### 🛡️ Operational Mission Templates")
                    # gr.Markdown("*Copy and paste these into the Command Input for a full system demonstration.*")
                    
                    gr.Markdown(
                        "**🛰️ Mission 1: Navigation & Technical Research**\n"
                        "> \"Please **take me to the website of langchain.com**. Analyze their latest documentation, then search **GitHub** for their top integration repos. Finally, cross-reference **ArXiv** for 2026 papers on 'LangGraph architectures'. Summarize all findings into 'LangChain_Intelligence.md' and alert Akash via push.\"",
                        elem_classes=["tpl-card"]
                    )
                    
                    gr.Markdown(
                        "**📸 Mission 2: Visual Market Intelligence**\n"
                        "> \"Navigate to the **IPL official website** and capture a **screenshot** of the current points table. Then, find the latest **YouTube** highlights of the **CSK match**. Check **Reddit** for public sentiment on the match results. Save the links and sentiment data to 'IPL_Match_Brief.md' and notify Akash.\"",
                        elem_classes=["tpl-card"]
                    )
                    
                    gr.Markdown(
                        "**💻 Mission 3: Developer Ecosystem Scouting**\n"
                        "> \"Scout **GitHub** for the top-starred 'AI Agent' frameworks of 2026. Use **Community Sentiment** to find what Reddit developers think of 'CrewAI' vs 'LangGraph'. Research **ArXiv** for new papers regarding 'Multi-Agent Autonomy'. Compile a professional deep-dive report into 'Agent_Ecosystem.md'.\"",
                        elem_classes=["tpl-card"]
                    )
                    
                    gr.Markdown("---")
                    # gr.Markdown("💡 *Note: These complex missions utilize the full multi-agent orchestration and require 2-3 minutes for deep synthesis.*")

                with gr.TabItem("Output Gallery"):
                    with gr.Column(elem_classes=["file-zone"]):
                        file_output = gr.File(
                            label="Mission Assets",
                            file_count="multiple",
                            interactive=False,
                        )
                        gr.Markdown("Files from the latest mission appear here automatically.")

    # Footer
    with gr.Row(elem_id="sk-footer"):
        gr.Markdown("Sidekick Intelligence Platform &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; Developed by Akash M J &nbsp;·&nbsp; All Rights Reserved")

    # ─────────────────────────────────────
    #  EVENT BINDING  (untouched)
    # ─────────────────────────────────────

    ui.load(setup, [], [sidekick_state])

    event_inputs  = [sidekick_state, message_input, criteria_input, chatbot]
    event_outputs = [chatbot, sidekick_state, file_output]

    message_input.submit(process_message, event_inputs, event_outputs)
    criteria_input.submit(process_message, event_inputs, event_outputs)
    go_button.click(process_message, event_inputs, event_outputs)
    reset_button.click(reset, [], [message_input, criteria_input, chatbot, sidekick_state, file_output])
    chatbot.change(fn=None, inputs=[chatbot], outputs=None, js=js_open_url)

if __name__ == "__main__":
    ui.launch(inbrowser=True)