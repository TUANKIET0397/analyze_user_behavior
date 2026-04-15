const API_URL = "http://127.0.0.1:8000"

export async function predict(data) {
    const res = await fetch(`${API_URL / api / predictions}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    return res.json()
}

export async function getAllPredictions() {
    const res = await fetch(`${API_URL}/predictions`)
    return res.json()
}

export async function getPredictions(prediction_id) {
    const res = await fetch(`${API_URL}/predictions/${prediction_id}`)
    return res.json()
}
