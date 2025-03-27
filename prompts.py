from langchain.prompts import ChatPromptTemplate

RESUME_IMPROVEMENT_PROMPT = """
    The candidate is applying for {job_title} at {company}. 
    Here is their resume:
    {resume}
    Here is the job description:
    {job_description}
    Give suggestions to improve the resume by identifying key skills and experience that align with this role, and suggest specific modifications to highligt these matches.Focus on using relevant keywords and quantifiable achievements. Return only in the form of an array of strings.
    """

RESUME_IMPROVEMENT_TEMPLATE = ChatPromptTemplate.from_template(RESUME_IMPROVEMENT_PROMPT)

JOB_TITLE_EXTRACTION_PROMPT = """
    The job description the candidate is applying for is the following. Extract the job title from the job description and return it in one line string:
    {job_description}
    """

JOB_TITLE_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(JOB_TITLE_EXTRACTION_PROMPT)

COMPANY_EXTRACTION_PROMPT = """
    The job description the candidate is applying for
    {job_description}
    Extract the company name from the job description and return it in one line string.
    """

COMPANY_NAME_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(COMPANY_EXTRACTION_PROMPT)

KEYWORD_EXTRACTION_PROMPT = """
    The job is {position} at {company}. 
    Here is the job description: 
    {job_description}. 
    Extract the keywords that should be in the applicants' resume to match the job description. The keywords should include each and every hard and soft skills that should be highlighted in the application form so that the applicant matches the job description perfectly. Return only in the form of comma separated strings and no special characters and proper captialization. 
    """

KEYWORD_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(KEYWORD_EXTRACTION_PROMPT)

TO_BE_NOTED_EXTRACTION_PROMPT = """
    The job is {position} at {company}.
    Here is the job description: 
    {job_description}. 
    Extract all the vital information (if any) that the candidate must note while applying for this role. This includes extra information like visa sponsorship, relocation assistance, salary or compensation details, work-mode, office location, etc to name a few.
    Return only in the form of comma separated strings and no special characters and proper captialization. 
    """

TO_BE_NOTED_EXTRACTION_TEMPLATE = ChatPromptTemplate.from_template(TO_BE_NOTED_EXTRACTION_PROMPT)

COVER_LETTER_GENERATION_PROMPT = """
    Here is the job description: 
    {job_description}. 
    Here is the resume: 
    {resume}. 
    Craft a compelling cover letter for {position} at {company} which the above mentioned job description and resume fit. Focus on highlighting the skills and experience that connects the candidate's specific achievements to the role and company needs for the role. Focus on showing genuine interest in their company and demonstrating cultural fit. 
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
    Judge the cover letter based on the job description and resume and provide exact improvements only without being vague or too general. Judge it on the basis of the how the cover letter gives the candidate the best chance of getting the job, shows his cultural fit, and shows genuine interest in the company. Answer should be in the form of comma separated strings only avoiding commas within the strings. 
    """

COVER_LETTER_IMPROVEMENT_TEMPLATE = ChatPromptTemplate.from_template(COVER_LETTER_IMPROVEMENT_PROMPT)