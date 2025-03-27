from flask import Flask, request, jsonify
from gemini_loader import get_chat_model
from langchain.prompts import ChatPromptTemplate
from prompts import *
from PyPDF2 import PdfReader
from flask_cors import CORS
import os
from io import BytesIO
import json

app = Flask(__name__)
CORS(app)
chatbot = get_chat_model()

@app.route("/generate-embeddings", methods=["POST"])
def generate_embeddings():
    # if "resume" not in request.files:
    #     return jsonify({"error": "No resume file provided"}), 400

    # resume_file = request.files["resume"]
    # resume_text = extract_text_from_pdf(resume_file)  # Function to extract text from PDF

    # # Generate embeddings using Gemini 2.0 Flash
    # embeddings = llm_client.generate_embeddings(resume_text)
    # return jsonify({"embeddings": embeddings})
    pass

@app.route("/process-job-description", methods=["POST"])
def process_job_description():

    data = request.get_json()

    if "jd" not in data:
        return jsonify({"error": "No job description provided"}), 400

    job_description_text = data["jd"]

    prompt = JOB_TITLE_EXTRACTION_TEMPLATE.format(job_description=job_description_text)
    job_title = chatbot.generate_content(contents=prompt).text
    prompt = COMPANY_NAME_EXTRACTION_TEMPLATE.format(job_description=job_description_text)
    company_name = chatbot.generate_content(contents=prompt).text
    prompt = KEYWORD_EXTRACTION_TEMPLATE.format(position=job_title, company=company_name, job_description=job_description_text)
    keywords = chatbot.generate_content(contents=prompt).text
    keywords = keywords.split(",")
    prompt = TO_BE_NOTED_EXTRACTION_TEMPLATE.format(position=job_title, company=company_name, job_description=job_description_text)
    notes = chatbot.generate_content(contents=prompt).text
    notes = notes.split(",")
    
    return jsonify({
        "title": job_title,
        "company": company_name,
        "keywords": keywords,
        "notes": notes
    })

@app.route("/summarize-resume", methods=["POST"])
def summarize_resume():

    prompt_context = """
        Summarise this resume:
        {context}
    """

    resume = request.files['resume']
    # print(resume)
    print("Recieved resume")
    resume_text = get_resume_text(resume)
    prompt_template = ChatPromptTemplate.from_template(prompt_context)
    prompt = prompt_template.format(context=resume_text)
    summary = chatbot.generate_content(contents=prompt)
    # print(summary.text)
    return jsonify({"summary": summary.text})

@app.route("/generate-cover-letter", methods=["POST"])
def generate_cover_letter():

    # data = request.get_json()

    if "resume" not in request.files:
        return jsonify({"error": "No resume provided"}), 400
    elif "jd" not in request.form:
        return jsonify({"error": "No job description provided"}), 400
    elif "position" not in request.form:
        return jsonify({"error": "Job description not processed to get job title"}), 400
    elif "company" not in request.form:
        return jsonify({"error": "No job description provided to get company name"}), 400
    
    resume = request.files['resume']
    resume_text = get_resume_text(resume)
    # jd = data["jd"]
    jd = request.form.get("jd")
    # position = data["position"]
    position = request.form.get("position")
    # company = data["company"]
    company = request.form.get("company")

    prompt = COVER_LETTER_GENERATION_TEMPLATE.format(position=position, company=company, job_description=jd, resume=resume_text)
    # print(prompt)
    cover_letter_json = chatbot.generate_content(contents=prompt).text
    cover_letter_json = cover_letter_json.replace("```", "")
    cover_letter_json = cover_letter_json[4:]
    # print(cover_letter_json)
    cover_letter = json.loads(cover_letter_json)
    # print(cover_letter)

    prompt = COVER_LETTER_IMPROVEMENT_TEMPLATE.format(position=position, company=company, job_description=jd, resume=resume_text, cover_letter=cover_letter)
    improvements = chatbot.generate_content(contents=prompt).text
    improvements = improvements.split(",")
    return jsonify({"cover_letter": cover_letter, "improvements": improvements})

def get_resume_text(resume):
    pdf_reader = PdfReader(BytesIO(resume.read()))
    text = ""
    # print(pdf_reader.metadata)
    for page_num, page in enumerate(pdf_reader.pages):
        text += f"\n ======= Page {page_num+1} ====== \n" + page.extract_text()
    return text

# @app.route('/')
# def start_to_run():
#     return "The server has started!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])