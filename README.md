# Resume Optimizer Pro

Resume Optimizer Pro is a web application that helps job seekers improve their resumes by evaluating them against job descriptions using advanced AI techniques. The app leverages Google Gemini API to analyze the resume and job description, and then provides recommendations to enhance the resume's visibility and relevance in competitive job markets.

## Features

- Upload your resume in PDF format
- Analyze the resume based on a given job description
- Receive feedback including a percentage match, missing keywords, and a profile summary
- Easy-to-use interface powered by Streamlit.

## Tech Stack

- **Streamlit**: Web application framework
- **Google Gemini API**: Used for generative AI to analyze resumes
- **PyPDF2**: For extracting text from PDF resumes
- **dotenv**: To manage environment variables securely

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/resume-optimizer-pro.git
    ```

2. Navigate to the project directory:
    ```bash
    cd resume-optimizer-pro
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file to store your Google Gemini API key:
    ```bash
    touch .env
    ```

5. Add your API key to the `.env` file:
    ```
    GOOGLE_API_KEY=your_google_gemini_api_key
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501`.

3. Enter the job description and upload your resume in PDF format.

4. Click **Submit** to receive a detailed analysis of your resume, including a percentage match, missing keywords, and suggestions to optimize your profile.

## Example Output

```json
{
  "JD Match": "85%",
  "MissingKeywords": ["Python", "Data Science", "Machine Learning"],
  "Profile Summary": "Your resume closely matches the job description. Consider adding more details on data science projects to improve visibility."
}
