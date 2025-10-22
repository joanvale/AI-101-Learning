from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Question(BaseModel):
    question: str
    options: list[str]
    correct_answer: str

class Answer(BaseModel):
    question_number: int
    user_answer: str

# Sample data (replace with a database or other storage in a real application)
questions = [
    Question(
        question="Which of the following is an example of AI?",
        options=[
            "A) A calculator performing basic math",
            "B) Google Search recommending articles based on your past searches",
            "C) A microwave heating food",
            "D) A simple alarm clock",
        ],
        correct_answer="B",
    ),
    
    Question(
        question="Which of the following best describes Narrow AI",
        options=[
            "A) AI that is capable of performing a wide range of tasks like a human",
            "B) AI specialized in a specific task, such as voice assistants or recommendation systems",
            "C) AI that surpasses human intelligence in all aspects",
            "D) AI that does not require training data",
        ],
        correct_answer="B",
    ),

    Question(
        question="What is General AI?",
        options=[
            "A) AI that can perform any intellectual task like a human",
            "B) AI that only works for specific tasks",
            "C) AI that does not use machine learning.",
            "D) AI limited to speech recognition.",
        ],
        correct_answer="A",
    ),

    Question(
        question="What is Super AI?",
        options=[
            "A) AI that is used in superhero movies",
            "B) AI that surpasses human intelligence in all cognitive tasks",
            "C) AI that only functions in self-driving cars",
            "D) AI with limited problem-solving abilities",
        ],
        correct_answer="B",
    ),

    Question(
        question="How is AI different from traditional programming?",
        options=[
            "A) AI follows strict, pre-programmed rules without learning.",
            "B) AI does not require data to function.",
            "C) Traditional programming and AI are the same.",
            "D) AI can learn from data and improve over time, whereas traditional.",
        ],
        correct_answer="D",
    ),

    Question(
        question="What is an example of AI in real-world applications?",
        options=[
            "A) Virtual assistants like Siri and Alexa",
            "B) Online recommendation systems",
            "C) Self-driving cars",
            "D) All of the above",
        ],
        correct_answer="D",
    ),

    Question(
        question="Which of the following is a disadvantage of AI?",
        options=[
            "A) High implementation costs and job displacement",
            "B) Increased efficiency and automation",
            "C) Faster data analysis",
            "D) Improved accuracy in decision-making",
        ],
        correct_answer="A",
    ),

    Question(
        question="How do AI systems improve their performance over time?",
        options=[
            "A) By rewriting their own source code manually",
            "B) By asking humans for corrections every time",
            "C) By using feedback and data to adjust their models",
            "D)By staying the same after initial training",
        ],
        correct_answer="C",
    ),

    Question(
        question="What role does big data play in AI development?",
        options=[
            "A) It provides a large amount of information that AI models use to learn patterns.",
            "B) It slows down AI training due to excessive data.",
            "C) AI does not require big data to function.",
            "D) Big data is only useful for human analysts, not AI.",
        ],
        correct_answer="A",
    ),

    Question(
        question="How might AI impact the future of work?",
        options=[
            "A) AI will replace all human jobs completely.",
            "B) AI will create new job opportunities while automating certain tasks.",
            "C) AI will have no impact on jobs or industries.",
            "D) AI will only be used in research and not in businesses.",
        ],
        correct_answer="B",
    ),

    Question(
        question="Which of the following is an application of AI in healthcare?",
        options=[
            "A) Performing manual surgery",
            "B) Selling prescription drugs",
            "C) Managing hospital staff",
            "D) Analyzing medical images for disease detection",
        ],
        correct_answer="D",
    ),

    Question(
        question="How does AI contribute to the finance industry?",
        options=[
            "A) By replacing human bank tellers entirely",
            "B) By creating fake credit scores",
            "C) By analyzing financial history to predict creditworthiness",
            "D) By blocking all online transactions",
        ],
        correct_answer="C",
    ),

    Question(
        question="Which of the following industries benefits from AI-powered product recommendations?",
        options=[
            "A) Retail",
            "B) Agriculture",
            "C) Construction",
            "D) Aviation",
        ],
        correct_answer="A",
    ),
    Question(
        question="What role does AI play in customer service?",
        options=[
            "A) It eliminates the need for human employees",
            "B) It powers chatbots that answer customer questions",
            "C) It prevents customers from making complaints",
            "D) It replaces human supervisors",
        ],
        correct_answer="B",
    ),

    Question(
        question="Which of the following is a challenge in AI development?",
        options=[
            "A) AI systems are always perfectly fair and unbiased",
            "B) AI systems require vast amounts of high-quality data",
            "C) AI can work without any computational resources",
            "D) AI never faces security threats",
        ],
        correct_answer="B",
    ),

    Question(
        question="Why is interpretability and explainability a challenge in AI?",
        options=[
            "A) AI systems always provide clear explanations for their decisions",
            "B) AI never makes mistakes, so explainability is not important",
            "C) AI systems sometimes make decisions that are difficult to understand",
            "D) AI decisions are always self-explanatory",
        ],
        correct_answer="C",
    ),

    Question(
        question="How does AI contribute to autonomous vehicles?",
        options=[
            "A) By allowing cars to navigate without human input",
            "B) By slowing down traffic deliberately",
            "C) By eliminating the need for roads",
            "D) By preventing all car accidents",
        ],
        correct_answer="A",
    ),

    Question(
        question="What ethical concern arises from AI’s use in surveillance?",
        options=[
            "A) AI surveillance is always 100% accurate",
            "B) AI eliminates the need for human law enforcement",
            "C) AI can be misused for mass surveillance and invasion of privacy",
            "D) AI removes the need for cybersecurity",
        ],
        correct_answer="C",
    ),

    Question(
        question="How does AI contribute to personalized learning?",
        options=[
            "A) By replacing teachers entirely",
            "B) By making all students learn at the same pace",
            "C) By preventing students from asking questions",
            "D) By providing customized educational content based on student needs",
        ],
        correct_answer="D",
    ),

    Question(
        question="What is a potential risk of AI in decision-making?",
        options=[
            "A) AI always makes the best decisions without any issues",
            "B) AI decisions may be biased based on the data it was trained on",
            "C) AI never requires human oversight",
            "D) AI eliminates the need for ethical considerations",
        ],
        correct_answer="B",
    ),
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "main.html", 
        {"request": request, "questions": questions, "enumerate": enumerate}
    )

@app.get("/questions/{question_number}")
async def get_question(question_number: int):
    if 1 <= question_number <= len(questions):
        return questions[question_number - 1]
    else:
        raise HTTPException(status_code=404, detail="Question not found")

@app.post("/check_answer")
async def check_answer(answer: Answer):
    if 1 <= answer.question_number <= len(questions):
        correct_answer = questions[answer.question_number - 1].correct_answer
        is_correct = answer.user_answer == correct_answer
        return {"is_correct": is_correct, "correct_answer": correct_answer}
    else:
        raise HTTPException(status_code=404, detail="Question not found")

@app.get("/all_questions")
async def get_all_questions():
    return questions