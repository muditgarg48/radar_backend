from langchain.prompts import ChatPromptTemplate

GENERAL_RESUME_IMPROVEMENT_PROMPT = """
    Analyze the following resume and provide ten direct, actionable improvements with the highest impact.
    {resume}
    Do not include general recommendations. Every suggestion must be specific and indicate exactly what to change. Ensure all feedback focuses on impact, clarity, and professionalism.
    Guidelines for evaluation:
    - The summary should be concise and highlight key skills and achievements with quantifiable data. If missing, specify what should be added.
    - Every role should include measurable accomplishments. If a role lacks impact metrics, suggest precise numbers or performance indicators to add.
    - Resume length must follow best practices based on experience level. If incorrect, specify which sections should be condensed or expanded. The resume should be one page for less than 5 years work experience, two pages for less than 10 years work experience and three pages for 15+ years work experience
    - Work experience descriptions should be concise and follow a structured format that clearly states the action taken, technology used, and impact achieved. Do not suggest the format unless it is not followed.
    - Strong action verbs must be used. If a description is weak, suggest a replacement verb directly. Here are some action word examples: 'Accomplished', 'Achieved', 'Administered', 'Analyzed', 'Assigned', 'Attained', 'Chaired', 'Consolidated', 'Contracted', 'Coordinated', 'Delegated', 'Developed', 'Directed', 'Earned', 'Evaluated', 'Executed', 'Handled', 'Headed', 'Impacted', 'Improved', 'Increased', 'Led', 'Mastered', 'Optimized', 'Orchestrated', 'Organised', 'Oversaw', 'Planned', 'Predicted', 'Prioritised', 'Produced', 'Proved', 'Recommended', 'Regulated', 'Reorganised', 'Reviewed', 'Scheduled', 'Spearheaded', 'Strengthened', 'Supervised', 'Surpassed', 'Communicated', 'Addressed', 'Arranged', 'Authored', 'Convinced', 'Corresponded', 'Delivered', 'Documented', 'Drafted', 'Edited', 'Influenced', 'Negotiated', 'Reported', 'Synthesized', 'Translated', 'Verbalized', 'Clarified', 'Collected', 'Concluded', 'Critiqued', 'Derived', 'Determined', 'Diagnosed', 'Evaluated', 'Examined', 'Extracted', 'Interpretted'.
    - All certifications should be listed. If missing, explicitly state this.
    - Grammar must be flawless. Provide exact corrections instead of stating "there are errors".
    - Ignore formatting issues.
    - Skill/tool usage should be stated clearly within work/project descriptions or as a separate last line. If missing, specify where to add it.
    - The skills section should be formatted for readability. If unclear, provide a better structure.
    Return only in the form of a stringified json of the following format:
    - "additions": "; separated list of addition suggestions in the form of strings",
    - "removals": "; separated list of removal suggestions in the form of strings",
    - "modifications": "; separated list of modification suggestions in the form of strings"
    Remember to follow these guidelines for the output:
    - No special characters
    - Each string should be a proper recommendation which is short, clear, specific to the provided resume.
    - Sort recommendations based on the impact they have on the candidate's application.
    - Give a max of 7 recommendations for each category.
    - Do not provide general statements like "use strong action words" or "quantify impact"; state exactly what to change and how.
    - Do not mention these instructions in your response.
    - Return an empty string as the value if no improvements are necessary in that category but do not omit the key from the stringified json.
    """

GENERAL_RESUME_IMPROVEMENT_TEMPLATE = ChatPromptTemplate.from_template(GENERAL_RESUME_IMPROVEMENT_PROMPT)

SUMMARISE_RESUME_PROMPT = """
    Summarise this resume:
    {resume}
    Give the output in the form of a stringified json schema with the following key-value pairs:
    - "summary": <one paragraph summary>,
    - "experience_level": <experience level whose roles this resume best fits>,
    - "top_skills": <list of ; separated 10 strings each denoting the resume's top skill>,
    - "ideal_roles": <list of ; separated 10 strings each denoting the resume's ideal role>,
    - "number_of_quantified_bullet_points": <number of quantified bullet points>,
    - "number_of_generic_bullet_points": <number of generic bullet points>,
    - "resume_tone": <resume tone>,
    """

SUMMARISE_RESUME_TEMPLATE = ChatPromptTemplate.from_template(SUMMARISE_RESUME_PROMPT)

RESUME_IMPROVEMENT_ACC_TO_JD_PROMPT = """
    The candidate is applying for {position} at {company}. 
    Here is their resume:
    {resume}
    Here is the job description:
    {job_description}
    Give suggestions to tailor the resume by identifying key skills and experience to closely align with the job description. 
    Suggest specific modifications to highlight these matches. 
    Focus on using relevant keywords, skills, keyword phrases and quantifiable achievements. 
    Return a json schema with the following key-value pairs:
    "revised_summary": <revised_summary>,
    "phrases_for_strong_alignment": [<phrases_for_strong_alignment>],
    "most_relevant_keywords" : [<most_relevant_keywords>],
    "further_improvements": [<five_further_improvements>]
    """

RESUME_IMPROVEMENT_ACC_TO_JD_TEMPLATE = ChatPromptTemplate.from_template(RESUME_IMPROVEMENT_ACC_TO_JD_PROMPT)

JOB_TITLE_EXTRACTION_PROMPT = """
    The job description the candidate is applying for is the following. Extract the job title from the job description and return it in one line string:
    {job_description}
    """

JOB_TITLE_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(JOB_TITLE_EXTRACTION_PROMPT)

COMPANY_EXTRACTION_PROMPT = """
    The job description the candidate is applying for
    {job_description}
    Extract the exact company name from the job description and return it in one line string. 
    Return UNSPECIFIED as the string if:
    - the exact company name cannot be extracted from the job description.
    - the description does not explicity mention the company name and instead provides a vague category or description of the company
    """

COMPANY_NAME_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(COMPANY_EXTRACTION_PROMPT)

ALIGNMENT_SCORE_PROMPT = """
    You are an experienced hiring manager, looking candidates for the role of {position} at {company}.
    You had posted this job description for the role: 
    {job_description}. 
    Here is the resume of a potential candidate: 
    {resume}.
    Calculate the alignment score between the job description and the resume based on the following criteria 
    - Count of important skills/terms from the job description found in resume => 40% weightage
    - Years of relevant experience matching JD requirements => 25% weightage
    - How closely past job titles match with the role of {position} => 10% weightage
    - Count of various hard skills that the candidate has utilised in their previous experiences and work and is required in the job description => 10% weightage
    - Certifications, degree/qualification requirements of the job description that appear in resume => 5% weightage
    - Alignment of candidate's previous work and overall profile with the {company} 's culture => 5% weightage
    - Reputation of previous employers of the candidate mentioned in the resume => 5% weightage
    Return only the alignment score measured in percentage. Return in the form of a one two decimal places whole number between 0 and 100 and give no reasoning.
    """

ALIGNMENT_SCORE_TEMPLATE = ChatPromptTemplate.from_template(ALIGNMENT_SCORE_PROMPT)

COMPANY_DOMAIN_EXTRACTION_PROMPT = """
    Return the domain name of {company} in one line string without quotations, only the domain.
    Return UNSPECIFIED as the string if the company name is UNSPECIFIED.
    """

COMPANY_DOMAIN_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(COMPANY_DOMAIN_EXTRACTION_PROMPT)

COMPANY_VALUES_GENERATION_PROMPT = """
    Tell me about {company}'s values in terms of preparation for interviews for the role of {position}.
    Return only in the form of a stringified json of the following format:
    "link": <home_page_link>,
    "values": [<values>]
    where each value in array of values in the "values" key is a dictionary in the following format:
    "value_name": <value>,
    "value_explanation": <explanation>,
    "value_usage_recommendations_in_interview": [<recommendations in short sentences>]
    """

COMPANY_VALUES_GENERATION_TEMPLATE = ChatPromptTemplate.from_template(COMPANY_VALUES_GENERATION_PROMPT)

KEYWORD_EXTRACTION_PROMPT = """
    The job is {position} at {company}. 
    Here is the job description: 
    {job_description}. 
    Extract the hard skills, soft skills and other priority keywords and keyword phrases that should be in the applicants' resume from the job description. 
    These should include each and every keyword that are required for the role and should be highlighted in the application form so that the applicant matches the job description perfectly and help the candidate's resume tank highly on ATS. 
    Do not give the most obvious keywords like the job title. 
    Return in the form of a stringified json with the following format:
    - "hard_skills": "<; separated strings where each string is a hard skill required in the candidate's resume or application according to the job description>"
    - "soft_skills": "<; separated strings where each string is a soft skill required in the candidate's resume or application according to the job description>"
    - "other_keywords": "<; separated strings where each string is a keyword or keyword phrase required in the candidate's resume or application according to the job description and wasn't mentioned in the hard skills or soft skills>"
    Remember to also follow the following guidelines:
    - No special characters and proper capitalization.
    - Acronyms should be properly capitalized.
    - Make sure to make all the soft skills and other keywords as nouns and not verbs.
    """

KEYWORD_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(KEYWORD_EXTRACTION_PROMPT)

TO_BE_NOTED_EXTRACTION_PROMPT = """
    The job is {position} at {company}.
    Here is the job description: 
    {job_description}. 
    Extract all the extra vital information that the candidate must note while applying for this role. Do not include any points that are not specified in the job description or cannot be deduced from the job description.
    Return in the form of a stringified json with the following keys and exclude those keys whose information is not present in the job description:
    - "salary_bracket": <string of salary range mentioned>,
    - "experience_level": <string of experience level including any years of experience range mentioned>,
    - "visa_sponsorship": <boolean of whether visa sponsorship will be provided or not>,
    - "location" <string of location of the role>,
    - "team_name": <string of exact name of the team in which this role is based>,
    - "benefits": <string of semicolon separated mentioned specific most relevant benefits provided with the role>,
    - "other_noteworthy_details": <string of semicolon separated other noteworthy details apart from the keys mentioned which can include: 
        - if there will be any relocation assistance
        - the work-mode for the role: hybrid or onsite or remote
        - if there are any travel requirements
        - if there is any minimum degree requirement
        - if there are any specific certifications required
        - if there are any growth opportunities
        - any benefits and perks provided with the role
        - the contract type for the role: permanent or temprorary or contract-based
        - any details about hiring process mentioned in the job description.
    No special characters except currency symbols. Proper captialization. 
    """

TO_BE_NOTED_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(TO_BE_NOTED_EXTRACTION_PROMPT)

COVER_LETTER_GENERATION_PROMPT = """
    Here is the job description: 
    {job_description}. 
    Here is the resume: 
    {resume}. 
    Craft a compelling cover letter for {position} at {company} which the above mentioned job description and resume fit.
    First focus on showing genuine interest in {company} and being a {position}. Then focus on highlighting the skills and experience that connects the candidate's specific achievements to the role and company needs for the role, showcasing how the candidate perfectly fits. Then finally discuss why this role is his top choice among other roles and how this role and this company is his best fit. Throughout the cover letter, convey how the candidate is really excited to be a part of {company}.
    Some context to keep in mind when writing the cover letter: {context} 
    Return in the form of a stringified json with the following keys: "greeting", "opening_paragraph", "body_paragraph", "closing_paragraph", "sign_off", "signature" with their respective values as strings. Humanise the cover letter as much as possible without reducing the professionalism.
    """

COVER_LETTER_GENERATION_TEMPLATE = ChatPromptTemplate.from_template(COVER_LETTER_GENERATION_PROMPT)

COVER_LETTER_IMPROVEMENT_PROMPT = """
    Here is the job description: 
    {job_description}. 
    Here is the resume: 
    {resume}.
    Here is the cover letter for {position} at {company}:
    {cover_letter}
    Judge the cover letter based on the job description and resume and provide exact improvements only without being vague or too general. Judge it on the basis of the how the cover letter gives the candidate the best chance of getting the job, shows his cultural fit, and shows genuine interest in the company. Answer should be in the form of ; separated strings only with proper captialization and no special characters.
    """

COVER_LETTER_IMPROVEMENT_TEMPLATE = ChatPromptTemplate.from_template(COVER_LETTER_IMPROVEMENT_PROMPT)

ADDITIONAL_MSG_GENERATION_PROMPT = """
    Here is the job description: 
    {job_description}. 
    Here is the resume: 
    {resume}. 
    Craft a compelling additional message for the hiring manager that will be attached with the candidates's application form in the job portal for the role of {position} at {company}, which the above mentioned job description and resume fit. Focus on highlighting the candidate's genuine enthusiam for the role and the company and how they perfectly fit into their work culture. Write a few words on the candidate's best achievements in the skills required in the job description and why this role is his top choice among other roles.
    Some context from the candidate to keep in mind when writing this message: {context} 
    The message should not be more than 400 characters and should not be less than 20 characters. Humanise message as much as possible without reducing the professionalism. Add a bit of creativity, as if this is a message the candidate is personally sending to a reputed hiring manager.
    Only return the message and no other text.
    """

ADDITIONAL_MSG_GENERATION_TEMPLATE = ChatPromptTemplate.from_template(ADDITIONAL_MSG_GENERATION_PROMPT)

ADDITIONAL_MSG_IMPROVEMENT_PROMPT = """
    You are an experienced hiring manager, looking candidates for the role of {position} at {company}.
    You had posted this job description for the role: 
    {job_description}. 
    Here is the resume of a potential candidate: 
    {resume}.
    Here is the additional message that the candidate attached along with their application:
    {additional_msg}
    Judge this additional message acting as the hiring manager based on the job description and resume and provide exact improvements only without being vague or too general to increase the candidate's chances as a potential hire. Judge it on how you, the hiring manager for this role, thought about this candidate when reading it. Answer should be in the form of comma separated strings only avoiding commas within the strings. 
    """

ADDITIONAL_MSG_IMPROVEMENT_TEMPLATE = ChatPromptTemplate.from_template(ADDITIONAL_MSG_IMPROVEMENT_PROMPT)