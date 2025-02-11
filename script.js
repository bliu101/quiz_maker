async function generateQuiz() {
    const num_q = document.getElementById("num_q").value;
    const unit_num = document.getElementById("unit_num").value;

    if (!num_q || !unit_num) {
        alert("Please enter valid inputs.");
        return;
    }

    const query = `Give me a multiple choice question quiz based on the given unit that is delimited by triple astriks ***${unit_num}*** to test the students on their knowledge after learning. The number of questions is delimited by triple quotes """${num_q}"""`;

    const system_constant = `Evaluate if the number of questions is a valid number.
    If not, reprompt the number of questions. Evaluate if the unit number is a valid number.
    If not, reprompt the unit number. Answer in a format of question, 4 answer choices. 
    And after all questions, give the key. In the key explain each answer like a helpful tutor, 
    assuming no previous knowledge.`;

    const requestBody = {
        model: "4o-mini",
        system: system_constant,
        query: query,
        temperature: 0.0,
        lastk: 0,
        session_id: "bridgette-rag-test",
        rag_usage: true,
        rag_threshold: "0.2",
        rag_k: 4
    };

    try {
        const response = await fetch("YOUR_BACKEND_URL", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        document.getElementById("quizOutput").textContent = JSON.stringify(data, null, 4);
    } catch (error) {
        document.getElementById("quizOutput").textContent = "Error generating quiz.";
    }
}
